# VK Photo Link Extractor

Этот скрипт на Python использует Selenium для извлечения ссылок на фотографии из поста ВКонтакте и сохранения их в текстовый файл.

## Требования

Для работы скрипта вам потребуется:

- Python 3.x
- Selenium
- webdriver-manager
- ChromeDriver (соответствующий версии вашего браузера Chrome)

## Установка

1. Установите необходимые библиотеки с помощью pip:

```sh
            pip install selenium
            pip install webdriver-manager
```

2. Убедитесь, что у вас установлен ChromeDriver. Вы можете скачать его с официального сайта или использовать webdriver-manager для автоматической установки.

## Использование

1. Скачайте ZIP-архив и разархивируйте полностью папку в удобное вам место. 
2. Откройте папку в VSCode или другом редакторе.
3. Запустите скрипт и введите ссылку на пост ВКонтакте, когда будет предложено:

```sh
        python parser.py
```

4. Скрипт извлечет ссылки на фотографии и сохранит их в файл photo_links.txt.

5. После выполнения скрипта вы увидите сообщение:

```sh
Ссылки на фотографии сохранены в файл photo_links.txt
```