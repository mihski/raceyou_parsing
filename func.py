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

def autorization():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')  # Отключение расширений
    #options.add_argument('--headless')  # Запуск в фоновом режиме (без окна браузера)
    driver = webdriver.Chrome(options=options)

    url = f"https://raceyou.ru/memberlist.php?&pp=100&order=asc&sort=username&ltr=A&page=1"

    

    driver.get(url)
    # Найдём поля для ввода логина и пароля
    username_input = driver.find_element(By.NAME, "vb_login_username")
    password_input = driver.find_element(By.NAME, "vb_login_password")

    # Вводим логин и пароль
    username_input.send_keys("mihski")  
    password_input.send_keys("rrd")  
    # Найдём кнопку для отправки формы и кликаем по ней
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Вход']")
    submit_button.click()

    # Ждём несколько секунд для успешной авторизации
    time.sleep(2)
    selenium_cookies = driver.get_cookies()
    # Переводим cookies в формат для requests
    session_cookies = {cookie['name']: cookie['value'] for cookie in selenium_cookies}

    return session_cookies,driver
    
    
def count_namber_page_in_litera(cookies):

    url = f"https://raceyou.ru/memberlist.php?&pp=100&order=asc&sort=username&ltr=A&page=1"
    # cookies = {    
    #     "bbpassword":"5daad476b8e45e36ae45d0956e94efad",
    #     "bbsessionhash":"4269eca55221a1b677cad9fe1795ec8b",
    #     "bbuserid":"12638"
    #     }
    #cookies,driver = autorization() 
                        
    headers = {
    "accept":"*/*",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    req=requests.get(url,cookies=cookies,headers=headers,)
    if req.status_code != 200:
        print(f"Ошибка при загрузке страницы ") 

    src=req.text
    soup = BeautifulSoup(src,"lxml")         
    last_page_tag = soup.find("a", title=lambda t: t and "Последняя страница" in t)
    namber_pages=0
    if last_page_tag:
        href = last_page_tag['href']  
        page= re.search(r'page=(\d+)', href) # В href ищем цыфры после  page= 
        if page:
            namber_pages = int(page.group(1))
            print("Номер последней страницы:", namber_pages)
            # print(type(namber_pages))
        else:
            print("Не удалось найти номер страницы.")
    else:
        print("Не найден тег с последней страницей.")

    return int(namber_pages)  


def CounterPages(driver):

    WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "smallfont")) 
    )

    src= driver.page_source
    soup = BeautifulSoup(src,"lxml")         
    last_page_tag = soup.find("a", title=lambda t: t and "Последняя страница" in t)
    namber_pages=0
    if last_page_tag:
        href = last_page_tag['href']  
        page= re.search(r'page=(\d+)', href) # В href ищем цыфры после  page= 
        if page:
            namber_pages = int(page.group(1))
            print("Номер последней страницы:", namber_pages)
            # print(type(namber_pages))
        else:
            print("Не удалось найти номер страницы.")
    else:
        print("Не найден тег с последней страницей.")

    return namber_pages
        
  

def find_names_Piter(driver):
    WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "alt2"))  # Заменить на правильный класс
    )
    scr =driver.page_source
    soup = BeautifulSoup(scr, "lxml")
    list_piter_name=[] 

    for tr in soup.find_all("tr"):
        # Ищем имя пользователя
        username = ""
        user_td = tr.find("td", class_="alt1Active")
        if user_td:
            a_tag = user_td.find("a")
            if a_tag:
                username = a_tag.text.strip()
        # Ищем город — из всех <td class="alt2"> берём последний непустой
        city = ""
        alt2_tds = tr.find_all("td", class_="alt2")
        for td in reversed(alt2_tds):
            text = td.get_text(strip=True)
            if text and text != '\xa0':
                city = text
                break            
        # Выводим, если есть имя и город
        if username and city:
            if city in ("Санкт-Петербург",
                        "Питер", 
                        "78", 
                        "СПб", 
                        "Спб",
                        "спб",
                        "SPB",
                        "Spb",
                        "spb"):                
            # print(f"{username} — {city}")
                list_piter_name.append(username)
    print(list_piter_name)
    

if __name__=="__main__":
     
 driver =autorization()

 find_names_Piter(driver)

 input(("Нажми Enter, когда закончишь..."))
 driver.quit()








