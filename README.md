# **B站视频爬虫**  
## **依赖库:**  
sqlite3和requests  
## **用法介绍：**  
先用input.py、middle.py、result.py生成三个数据库（注意修改存放路径）  
其中leg.db是存放你要爬的up主的信息的，mid是指up的uid，可以看主页链接里面的那串数字，num是up主的视频数量，不超过100个  
leg.db需要自行编辑，我用的是SQLiteStudio  
修改bilibili-spider.py和crawl.py中数据库存放的路径，对应修改哈  
接下去，爬！给爷爬！  
## **以下是碎碎念：**  
说一下这次的爬虫项目吧，我用了sqlite3和requests这两个库，requests不用说了吧，爬虫项目必备库，sqlite3是我用于存储中间过程产生的数据以及最终结果的，大题思路前两天写代码过程已经阐述过了，分两个模块：UP主视频信息模块和视频数据爬取模块，中间产生的数据用一个数据库存储并起到传参的效果，部分代码用的github上关于B站爬虫的，大部分是自己手写的。为什么用两个模块，主要是考虑到好debug，本来这里面就有一堆变量，程序长了也不方便找哪个是哪个变量（本人变量随意命名派，什么奇怪的名字里面都有），UP主视频信息模块调用的接口是：https://api.bilibili.com/x/space/arc/search?mid=400218693&ps=100&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp  
mid是up主的uid，ps是要爬视频的数量，范围是1-100，是按时间顺序（也就是order里面的pubdate即public date），爬出来的数据写入列表再用小学二年级就学过的字段查找哈，挺简单的。  
视频信息爬取模块用的是老接口了，接口都泛滥了，随便哪个B站信息相关的爬虫都用这个：https://api.bilibili.com/x/web-interface/archive/stat?aid=418853104  
但是要注意这个接口的脾气比较奇怪，请求多了会封ip哈...中间蛮搞笑的是，我懒得写requests的代码就吧原先的代码保留了，但是为了保留代码我又自己写了全局变量，还对原先代码做了大量的调整，约等于没改lol...  
最终的数据输出到数据库里，然后用的sqlite studio把数据export出来的，不过有个bug，第二个模块写up主名称的时候会报错，所以我就顺手写了俩双引号，结果出来结果是row[2]，人都傻了...