import urllib.request
import requests
from bs4 import BeautifulSoup
url = "https://dblp.uni-trier.de/search?q=stackoverflow" #key words
#r= "https://dblp.uni-trier.de/db/conf/icra/icra2019.html"    # 会议
# url = "https://dblp.uni-trier.de/db/journals/trob/trob35.html" #期刊
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
soup2 = soup.find_all('li',{"class":"entry"})   #y words

#soup2 = soup.find_all('li',{"class":"entry inproceedings"})   #会议
#entry informal toc
# soup2 = soup.find_all('li', {"class": "entry article"})   #期刊

fp = open('paperlink.txt', 'w')
for i in soup2:
    s = i.find('a')['href']+'\n'
    print(i)
    sci_link = 'https://sci-hub.ren/' + s
    fp.write(sci_link)
fp.close()

soup3 = soup.find_all('span', {"class": "title"})
fpname = open('papername.txt', 'w')
for i in soup3:
    s = i.string
    # print(s)
    s = i.text + '\n'
    print(s)
    fpname.write(s)
fpname.close()
