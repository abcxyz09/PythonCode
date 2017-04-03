import requests
page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
#page = requests.get('')

#print page.status_code

#print page.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(page,'html.parser')
#print soup.prettify()
#li =[type(item) for item in list(soup.children)]
#html = list(soup.children)[2]

#print [type(item) for item in list(html.children)]
#p = list(body.children)[1]

#print p.get_text()
#a = soup.find_all('a') 
#for x in a:
#	print x

#print soup.get_text()