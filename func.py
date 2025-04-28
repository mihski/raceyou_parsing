from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import lxml
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



options = webdriver.ChromeOptions()
options.add_argument('--headless')  # без открытия окна браузера
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
                     
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


url = f"https://raceyou.ru/memberlist.php?&pp=100&order=asc&sort=username&ltr=A&page=1"
headers = {
"accept":"*/*",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

cookies = {    
    "bbpassword":"5daad476b8e45e36ae45d0956e94efad",
    "bbsessionhash":"4269eca55221a1b677cad9fe1795ec8b",
    "bbuserid":"12638"
} 
driver.get(url)   
for name, value in cookies.items():
    driver.add_cookie({'name': name, 'value': value})
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//tbody/tr"))
)

# Получаем количество строк на странице
rows = driver.find_elements(By.XPATH, "//tbody/tr")

# Если строк больше 0, начинаем парсить
if len(rows) > 0:
    print(f"Загружено {len(rows)} строк. Можно начинать парсинг!")
else:
    print("Строки таблицы ещё не загружены.")

html= driver.page_source


# req=requests.get(url,cookies=cookies,headers=headers,)
# if req.status_code != 200:
#     print(f"Ошибка при загрузке страницы ") 



with open("raceyou.html","w", encoding="utf-8") as file:
    file.write(html)


# def CounterPages():

#     soup = BeautifulSoup(src,"lxml")         
#     last_page_tag = soup.find("a", title=lambda t: t and "Последняя страница" in t)

#     if last_page_tag:
#         href = last_page_tag['href']  
#         page= re.search(r'page=(\d+)', href) # В href ищем цыфры после  page= 
#         if page:
#             namber_pages = int(page.group(1))
#             # print("Номер последней страницы:", namber_pages)
#             # print(type(namber_pages))
#         else:
#             print("Не удалось найти номер страницы.")
#     else:
#         print("Не найден тег с последней страницей.")

#     return namber_pages    
  
# # # def get_sity():
# # soup = BeautifulSoup(src,"lxml")  
# # sity = soup.find("body","tr")


# # if __name__== "__main__":
# #     #print(CounterPages())
# #     print(sity)










# if last_page_tag:
#     print(last_page_tag)
# else:
#     print("Не найдено")

# print(last_page_tag)


