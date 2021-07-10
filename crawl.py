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
conn = None
reqf = []


def crawl(url):
     global req
     req = requests.get(url, headers=headers, timeout=6).json()
pass

con = sqlite3.connect('M:\Blispi-video\db\leg.db')  #填入你准备存放数据库文件的路径（数据库名必须是leg.db）
cu = con.cursor()
cur = con.execute("SELECT mid,num from leg")
conn = sqlite3.connect('M:\Blispi-video\db\data.db')  #填入你准备存放数据库文件的路径（数据库名必须是data.db）
c = conn.cursor()

for row in cur:
    mid = str(row[0])
    num = str(row[1])
    num1 = int(row[1])
    urls = "https://api.bilibili.com/x/space/arc/search?mid=" + mid + "&ps=" + num + "&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp"
    #reqd = req.content
    crawl(urls)
    #conn = sqlite3.connect('*********\data.db')   这个不用改
    for i in range(num1):
        reqd = req['data']
        reqe = reqd['list']
        reqf = reqe['vlist']
        try:
            rec = reqf[i]["aid"]   #av号
            red = reqf[i]["bvid"]  #bv号
            nck = reqf[i]["author"]   #作者昵称
            tme = reqf[i]["created"]  #发布时间戳
            c = conn.cursor()
            c.execute("INSERT INTO UINFO (aid,bvid,nick,time1) \
            VALUES(%d,'%s','%s',%d)" % (rec,red,nck,tme))
            print (rec)
            print (red)
            print (num1)
        except:
            pass
conn.commit()
conn.close()
con.commit()
con.close()