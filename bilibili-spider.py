import threading
import time
import sqlite3
import requests
from concurrent import futures

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
total = 1
result = []
lock = threading.Lock()
flag = None
conn = None
req = None
video = None
vew = int
dmu = int
rep = int
fav = int
coi = int
shr = int
ad = None
nck = str
def run(url):
    # 启动爬虫
    global total
    global req
    global video
    global vew
    global dmu
    global rep
    global fav
    global coi
    global shr

    req = requests.get(url, headers=headers, timeout=6).json()
    time.sleep(0.4)
    try:
        data = req['data']
        vew = data['view']
        dmu = data['danmaku']
        rep = data['reply']
        fav = data['favorite']
        coi = data['coin']
        shr = data['share']
        with lock:
            result.append(video)
            if total %250 == 0:
                print(total)
            total += 1
    except:
        pass

co = sqlite3.connect('*********\data.db')    #填入你准备存放数据库文件的路径（数据库名必须是data.db）
cu = co.cursor()
cur = co.execute("SELECT aid,bvid from UINFO")
cp = sqlite3.connect('*********\leg2.db')    #填入你准备存放数据库文件的路径（数据库名必须是leg2.db）
cr = cp.cursor()
#crr = cp.execute("SELECT aid,nick,view,danmu,reply,favorite,coin,share from result")
for row in cur:
    ad = str(row[0])
    bv = str(row[1])
    nck = row[2]
    urls = "http://api.bilibili.com/archive_stat/stat?aid=" + ad
    run(urls)
    cr.execute("INSERT INTO result (aid,nick,view,danmu,reply,favorite,coin,share) \
    VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (bv,nck,vew,dmu,rep,fav,coi,shr))
    print (vew)
    #print (video)
cp.commit()
cp.close()