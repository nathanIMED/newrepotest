import urllib
import re
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    #reg = r'src="(.+?\.jpg)"smallSrc '
    reg = r'src="(.+?\.png)" width'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.png' % x)
        x+=1


html = getHtml("http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1491707401723_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&f=3&oq=%E5%9B%BE%E7%89%87&rsp=0")
print html
print getImg(html)

