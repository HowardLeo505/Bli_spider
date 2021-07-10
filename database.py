import sqlite3
leg = sqlite3.connect('*********\db\leg.db') #填入你准备存放数据库文件的路径（数据库名必须是leg.db）
cleg = leg.cursor()
data = sqlite3.connect('M:\Blispi-video\db\data.db')   #填入你准备存放数据库文件的路径（数据库名必须是data.db）
cdata = data.cursor()
leg2 = sqlite3.connect('M:\Blispi-video\db\leg2.db')   #填入你准备存放数据库文件的路径（数据库名必须是leg2.db）
cleg2 = leg2.cursor()
cleg.execute('''CREATE TABLE leg
       (mid            INT     NOT NULL,
        num            INT     NOT NULL);''')
cdata.execute('''CREATE TABLE UINFO
       (aid            INT     NOT NULL,
        bvid            INT     NOT NULL,
        nick            STR     NOT NULL,
        time1            INT     NOT NULL);''')
cleg2.execute('''CREATE TABLE result
       (aid            STR     NOT NULL,
        nick            STR    NOT NULL,
        view           STR     NOT NULL,
        danmu          STR     NOT NULL,
        reply          STR     NOT NULL,
        favorite       STR     NOT NULL,
        coin           STR     NOT NULL,
        share          STR     NOT NULL);''')
leg.commit()
leg.close()
data.commit()
data.close()
leg2.commit()
leg2.close()