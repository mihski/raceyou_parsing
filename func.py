from bs4 import BeautifulSoup 
import requests
import lxml
import re


cookies = {    
    "bbpassword":"5daad476b8e45e36ae45d0956e94efad",
    "bbsessionhash":"4269eca55221a1b677cad9fe1795ec8b",
    "bbuserid":"12638"
}                         
url = f"https://raceyou.ru/memberlist.php?&pp=100&order=asc&sort=username&ltr=A&page=1"
headers = {
"accept":"*/*",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}
req=requests.get(url,cookies=cookies,headers=headers,)
if req.status_code != 200:
    print(f"Ошибка при загрузке страницы ") 

src=req.text

with open("raceyou.html","w",) as file:
    file.write(src)


def CounterPages():

    soup = BeautifulSoup(src,"lxml")         
    last_page_tag = soup.find("a", title=lambda t: t and "Последняя страница" in t)

    if last_page_tag:
        href = last_page_tag['href']  
        page= re.search(r'page=(\d+)', href) # В href ищем цыфры после  page= 
        if page:
            namber_pages = int(page.group(1))
            # print("Номер последней страницы:", namber_pages)
            # print(type(namber_pages))
        else:
            print("Не удалось найти номер страницы.")
    else:
        print("Не найден тег с последней страницей.")

    return namber_pages    
  
   

print(CounterPages())









# if last_page_tag:
#     print(last_page_tag)
# else:
#     print("Не найдено")

# print(last_page_tag)


