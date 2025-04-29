from gettext import find
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup



options = webdriver.ChromeOptions()
#options.add_argument('--disable-extensions')  # Отключение расширений
#options.add_argument('--headless')  # Запуск в фоновом режиме (без окна браузера)
driver = webdriver.Chrome(options=options)

url = f"https://raceyou.ru/memberlist.php?&pp=100&order=asc&sort=username&ltr=A&page=1"

headers = {
"accept":"*/*",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

driver.get(url)
# Найдём поля для ввода логина и пароля
username_input = driver.find_element(By.NAME, "vb_login_username")
password_input = driver.find_element(By.NAME, "vb_login_password")

# Вводим логин и пароль
username_input.send_keys("mihski")  # Заменить на свой логин
password_input.send_keys("rrd")  # Заменить на свой пароль

# Найдём кнопку для отправки формы и кликаем по ней
submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Вход']")
submit_button.click()

# Ждём несколько секунд для успешной авторизации
time.sleep(2)

WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "alt2"))  # Заменить на правильный класс
)
page_source = driver.page_source


with open("raceyou.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

soup = BeautifulSoup(page_source, "lxml")

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
    list_piter_name=[]        
    # Выводим, если есть имя и город
    if username and city:
        if city == "Санкт-Петербург"\
        or city == "Питер"\
        or city == "78"\
        or city == "SPB"\
        or city == "СПб"\
        or city == "Спб"\
        or city == "Spb"\
        or city == "spb":
            print(f"{username} — {city}")
            list_piter_name=list_piter_name.append(username)
    print(list_piter_name)
input("Нажми Enter для закрытия браузера...")