import requests
from bs4 import BeautifulSoup

# url = 'https://hualsy.com/book/79/76031.html'
# html = requests.get(url).text.encode('iso-8859-1')
# bfs = BeautifulSoup(html,'lxml')
# title = bfs.select_one('#content > div.page-header.text-center > h1').text
# text = bfs.select_one('#htmlContent').text
# print(title)
# print(text)

url = 'https://hualsy.com/book/79.html'
html = requests.get(url).text.encode('iso-8859-1')
bfs = BeautifulSoup(html,'lxml')
dl = bfs.select_one('#list-chapterAll > dl')
list_dd = dl.find_all(name='dd')
list_a = []
for dd in list_dd:
    a = dd.a['href']
    list_a.append('https://hualsy.com/'+a)
i = 1
for url_a in list_a :
    html_a = requests.get(url_a).text.encode('iso-8859-1')
    bfs_a = BeautifulSoup(html_a,'lxml')
    title = bfs_a.select_one('#content > div.page-header.text-center > h1').text
    text = bfs_a.select_one('#htmlContent').text
    with open('douluo.txt','a',encoding='utf-8') as file :
        file.write(title+'\n'+text+'\n'+''
        '-----------------------------------------------------------------------------------------\n')
    print('第'+str(i)+'章下载完毕')
    i = i+1


#list-chapterAll > dl > dd:nth-child(1)
#list-chapterAll > dl > dd:nth-child(2)
#list-chapterAll > dl
