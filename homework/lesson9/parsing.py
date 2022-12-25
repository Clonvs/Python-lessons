from bs4 import BeautifulSoup as bs
import requests




url = 'https://mybook.ru/catalog/books/free/'
response = requests.get(url)
print(response)
soup = bs(response.text, "lxml")  
#print(soup)
teme = soup.find_all("div", class_="e4xwgl-5 dgfgnj")
#print(teme.text)
for temes in teme: 
    temes = temes.find("p", {'class':'lnjchu-1 dPgoNf'})
    print(temes.text)
    

  
