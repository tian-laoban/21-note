import requests
# http://baoshuu.com/TXT/list26_1.html
# http://baoshuu.com/TXT/list2_1.html
# https://www.txt99.org/html/list-xuanhuan-1.html
from lxml import etree


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0'}

def 耽美():
    dom = etree.HTML(requests.get('http://baoshuu.com/TXT/list26_1.html',headers = headers).text)
    book_list = dom.xpath('//*[@class="newDate"]')
    for book in book_list:
        public_date = book.xpath('./text()')[0].strip()
        if public_date == '2022-05-17':
            url = 'http://baoshuu.com' + book.xpath('./../../h2/a/@href')[0].strip()
            download(url)
            # depress()
            # print(book.xpath('./../../'))

    pass


def 热门():
    pass


def download(url):
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

def depress(filename):
    pass




耽美()
