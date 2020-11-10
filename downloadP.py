import requests
from bs4 import BeautifulSoup

# FLAG
OPEN_KEYWORD_SEARCH = False
#   关键词
Key_word = ''
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
    if OPEN_KEYWORD_SEARCH == True:
        if Key_word in s:
            downloadlist.append(select_num)
    else:
        downloadlist.append(select_num)
    select_num += 1
print(downloadlist)

count = 0
select_num = 0
def download_arxiv(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    # print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    soup2 = soup.find_all('meta', {"name": "citation_pdf_url"})  # y words
    print(soup2)
    s = soup2[0]
    #print(s)
    urll = str(s).split("\"")[1]
    print(urll)
    return urll


def notBoth(url):
    s1=url.find("//doi")
    s2=url.find("//arxiv")
    if(s1 ==-1 and s2==-1):
        return False
    else:
        return True
def downloadPaper():
    return
tr2="https://sci-hub.ren/"
for line in f:
    if count == downloadlist[select_num]:
        line = line[:-1]
        print()
        if line.find("//doi")!=-1:
            print("doi")
            res = requests.get(line)
            res.encoding = 'utf-8'
            #print(res.text)
            soup = BeautifulSoup(res.text, 'html.parser')
            news = soup.select('iframe')
            # print(news)
            print(news)

            if news== []:
                continue
            pdf_final = news[0]['src']
            #print(pdf_final)
            out_fname = 'paper/' + namelist[count] + '.pdf'  # 取名
            print(["downloading ...", namelist[count]])
            check_http = pdf_final[0:6]
            if check_http != "https:":
                pdf2 = "https:" + pdf_final
            r = requests.get(pdf2)
            with open(out_fname, 'wb') as f2:
                f2.write(r.content)

        elif line.find("//arxiv")!=-1:
            print("arx")
            line2=line.replace(tr2,'')
            pdf_final=str(download_arxiv(line2))
            #print(pdf_final)
            out_fname = 'paper/' + namelist[count] + '.pdf'  # 取名
            print(["downloading ...", namelist[count]])
            r = requests.get(pdf_final)
            with open(out_fname, 'wb') as f2:
                f2.write(r.content)
        else:
            print("else")
            continue

        select_num += 1
        if select_num >= len(downloadlist):
            break
    print("=============================================")
    count += 1

f.close()
