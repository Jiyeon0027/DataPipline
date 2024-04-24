#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request as req
import re

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')
news = soup.select_one("#content > div.section_news > div > ul")
# print(news)
href_reg = re.compile(r"^/news/")
li = news.find_all(href= href_reg)

for e in li:
    print("https://n.new.naver.com"+e.attrs['href'])