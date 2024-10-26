# Перед использованием в терминальчик закинь эту команду ->  pip install selenium
# У тебя скачалось расширение для работы с кодом.
# Дальше запусти через терминал наш код командой py parser.py или, если у тебя установлена другая библиотека, то - python parser.py
# В терминале появится окошко для того, чтобы ты ввел ссылку на пост из которого нужно спарсить ссылки.

# Powered by TvxyLxrd
# Check out my github - https://github.com/TvxyLxrd
# Profi.ru link - https://profi.ru/profile/BuvinMS


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_photo_links(post_url):
    # Настройка драйвера
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Закомментируйте эту строку для отладки
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=options)

    # Переход на страницу поста
    driver.get(post_url)
    time.sleep(10)  # Ждем, пока страница полностью загрузится

    # Извлекаем ссылки на фотографии
    photo_links = []
    photos = driver.find_elements(By.CSS_SELECTOR, 'div[data-task-click="WallPost/openPhoto"]')
    if photos:
        for photo in photos:
            photo_id = photo.get_attribute('data-photo-id')
            list_id = photo.get_attribute('data-list-id')
            if photo_id and list_id:
                photo_url = f"https://vk.com/photo{photo_id}?list={list_id}"
                photo_links.append(photo_url)
    else:
        print("Не найдены элементы с фотографиями.")

    # Закрытие браузера
    driver.quit()

    return photo_links

def main():
    # Ввод ссылки на пост из консоли
    post_url = input("Введите ссылку на пост ВКонтакте: ")

    # Получение ссылок на фотографии
    photo_links = get_photo_links(post_url)

    # Сохранение ссылок в текстовый файл
    with open('photo_links.txt', 'w') as file:
        for link in photo_links:
            file.write(link + '\n')

    print("Ссылки на фотографии сохранены в файл photo_links.txt")

if __name__ == "__main__":
    main()
