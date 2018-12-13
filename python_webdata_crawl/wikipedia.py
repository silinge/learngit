# I made this one as first day and see how far can T get.
# The code belong to the book's author.
#part one
#-------------------------------------------------
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html, features='lxml')
# for link in bsObj.findAll("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

#get href from this link
#-------------------------------------------------
#part two
#-------------------------------------------------
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
# html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# bsObj = BeautifulSoup(html, features='lxml')
# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",
#                                                            href = re.compile("^(/wiki/)((?!:).)*$")):
#     #正则表达式 必须以/wiki/开头 结尾必须不是： 目前不清楚原因
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
#-------------------------------------------------
# part three
#-------------------------------------------------
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import datetime
# import random
# import re
#
# random.seed(datetime.datetime.now())
# def getLinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org" + articleUrl)
#     bsObj = BeautifulSoup(html, features='lxml')
#     return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
#                                                           href = re.compile("^(/wiki/)((?!:).)*$"))
# links = getLinks("/wiki/Kevin_Bacon") #links 得到了一个链接的列表 原始链接是 Kevin_Bacon的页面
# while len(links)>0:
#     newArticle = links[random.randint(0, len(links) - 1)].attrs['href'] #从这个列表当中随机提前一个链接再去获取链接下的一个链接列表，循环到手动停止或者遇到某一个链接页面包含链接为空。
#     print(newArticle)
#     links = getLinks(newArticle)

#-------------------------------------------------
# part four
# 循环遍历采集网站的所有链接
#-------------------------------------------------
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
# pages = set()
# def getLinks(pageUrl):
#     global pages
#     html = urlopen("http://en.wikipedia.org"+pageUrl)
#     bsObj = BeautifulSoup(html, features='lxml')
#     for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")): #查找所有a标签下 以/wiki/开头的链接
#         if 'href' in link.attrs: #抽取href
#             if link.attrs['href'] not in pages: # 判断这个链接在不在pages 集合里面 如果没有 则打印加入，如果有则跳过 这样去重
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
#
# getLinks("") #起始页就是网站的主页，

#-------------------------------------------------
# part five

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
# pages = set()
# def getLinks(pageUrl):
#     global pages
#     html = urlopen("http://en.wikipedia.org" + pageUrl)
#     bsObj = BeautifulSoup(html, features='lxml')
#     try:
#         print(bsObj.h1.get_text())
#         print(bsObj.find(id="mw-content-text").findAll("p")[0])
#         print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
#     except AttributeError:
#         print("页面缺少一些属性，不过没有大问题")
#
#     for link in bsObj.findAll("a", href = re.compile("^(/wiki/)")):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 newPage = link.attrs['href']
#                 print("deng deng deng deng\n"+newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
#
# getLinks("")

#-------------------------------------------------
# part six
#从一个网站开始获取所有的链接 随机选一个再次获取 循环
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#获取页面内所有链接的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    #找出所有“/”开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# 获取页面所有链接的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #找出所有“http" 和 ”www" 开头的且不包括当前url的链接
    for link in bsObj.findAll("a", href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, features='lxml')
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    # print("随机链接是："+externalLink)
    # followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")

# 收集网站上发现的所有外链列表 存起来
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("将要获得的链接url是：" + link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

getAllExternalLinks("http://oreilly.com")