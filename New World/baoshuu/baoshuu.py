import requests
from lxml import etree
import rarfile
import os
from time import strptime


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0'}

def main(choose:str, date:str):
    _ = 'http://baoshuu.com/TXT/list2'
    if choose == '1':
        _ += '6_%s.html'
    if choose == '2':
        _ += '_%s.html'

    need_date = strptime(date, '%Y-%m-%d')
    for page in range(1, 10000):
        dom = etree.HTML(requests.get(_%page,headers = headers).text)
        book_list = dom.xpath('//*[@class="newDate"]')
        for book in book_list:
            public_date = strptime(book.xpath('./text()')[0].strip(), '%Y-%m-%d')
            if public_date > need_date:
                continue
            if public_date == need_date:
                url = 'http://baoshuu.com' + book.xpath('./../../h2/a/@href')[0].strip()
                filename = 下载(url)
                try:
                    解压(filename)
                except:
                    print('解压失败：',filename)
                    continue
                os.remove(filename)
            if public_date < need_date:
                exit()


def 下载(url):
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Cookie': 'ASPSESSIONIDSCRCBABA=FBFDIDJBOKIFOGOKLNFLAHBP',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Host': 'baoshuu.com',
    'Referer': url,
    'Upgrade-Insecure-Requests': '1'
    }
    dom = etree.HTML(requests.get(url,headers = headers).text)
    url = 'http://baoshuu.com' + dom.xpath('//ul[@class="downlistbox"]/li[2]/a/@href')[0].strip()
    url = requests.get(url,headers = headers, allow_redirects=False).headers['Location']
    filename = url.split('bookdown/')[1]

    headers = {
    'Host': '183.131.85.65:60',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://baoshuu.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
    }
    with open(filename,'wb') as  f:
        f.write(requests.get(url,headers = headers).content)
    return filename

def 解压(filename):
    rf = rarfile.RarFile(filename)
    rf.extractall('下载')



if __name__ == '__main__':
    choose = input('1.耽美\n2.热门\n请选择：')
    main(choose, date = input('输入日期：'))