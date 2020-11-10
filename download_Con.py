import requests
from bs4 import BeautifulSoup

# FLAG
OPEN_KEYWORD_SEARCH = True
#   关键词
Key_word = 'Curriculum'
# 论文链接
lines = open('paperlink.txt').readlines()  # 一行一行读
f = open('paperlink.txt')

# 论文Title读进list里
fpname = open('papername.txt').readlines()
namelist = []
downloadlist = []
select_num = 0
for i in fpname:
    i = i[:-1]
    s = i.replace(':', '')
    namelist.append(s)
    # 关键词下载
    if OPEN_KEYWORD_SEARCH == False:
        if Key_word in s:
            downloadlist.append(select_num)
    else:
        downloadlist.append(select_num)
    select_num += 1
print(downloadlist)

count = 0
select_num = 0
for line in f:
    if count == downloadlist[select_num]:
        line = line[:-1]

        res = requests.get(line)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        news = soup.select('iframe')
        pdf = news[0]['src']
        out_fname = 'paper/' + namelist[count] + '.pdf'  #取名
        print(["downloading ...", namelist[count]])
        check_http = pdf[0:6]
        if check_http != "https:":
            pdf = "https:" + pdf
        r = requests.get(pdf)
        with open(out_fname, 'wb') as f2:
            f2.write(r.content)
        select_num += 1
        if select_num >= len(downloadlist):
            break
    count += 1
f.close()
