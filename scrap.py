from bs4 import BeautifulSoup as bs
import urllib3
 

x = open('a.txt','a')

http = urllib3.PoolManager()
list =[]
def fun(urll):
    r = http.request('GET',urll)
    soup = bs(r.data , 'html.parser')

    for link in soup.find_all('a'):
   # print(link.get('href'))
        x.write(link.get('href')+"\n")
        list.append(link.get('href'))
        print(link.get('href'))





user = raw_input("Enter URL:")

fun(user)
for fu in list:
    fun(fu)
    print(fu)
