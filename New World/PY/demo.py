from bs4 import BeautifulSoup as BS

s = '''\
<h3>手机</h3>
<h3>电脑</h3>
<h3>平板</h3>
'''

soup = BS(s,'lxml')
h3s =  soup.find_all('h3')
for [i] in h3s:
    print(i)

print('*'*30)

for h3 in h3s:
    print(h3.string)


