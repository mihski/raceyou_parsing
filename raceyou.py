from bs4 import BeautifulSoup
import requests
import string
import urllib.parse as urlparse
from func import CounterPages

liter_list = list(string.ascii_uppercase)  
list_name_liter=[""]
page =1
for litera in range(1,2): 
    url = f"https://raceyou.ru/memberlist.php?&pp=100&order=asc&sort=username&ltr={litera}&page={page}"
    headers = {
    "accept":"*/*",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }
    cookies = {    
    "bbpassword":"5daad476b8e45e36ae45d0956e94efad",
    "bbsessionhash":"4269eca55221a1b677cad9fe1795ec8b",
    "bbuserid":"12638"
    }                         
    req=requests.get(url,headers=headers,cookies=cookies)

    if req.status_code != 200:
        print(f"Ошибка при загрузке страницы ")  

    src =  req.text
    page=CounterPages()

    for i in range(1,(page+1)):
        url = f"https://raceyou.ru/memberlist.php?&pp=100&order=asc&sort=username&ltr={litera}&page={1}"
        scr=requests.get(url,headers=headers,cookies=cookies).text
        soup = BeautifulSoup(src,"lxml")
        user= soup.find_all()

