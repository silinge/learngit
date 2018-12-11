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