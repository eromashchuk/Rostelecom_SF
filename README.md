Финальный проект для курса "Тестировщик - автоматизатор на Python"

Тестирование формы авторизации Личного кабинета Ростелеком https://b2c.passport.rt.ru

Ссылка на требования по проекту - https://docs.google.com/document/d/14TRuoYG8JXlLCMXuesBXrbNK7OefVxMW/edit?usp=share_link&ouid=102111731768085493149&rtpof=true&sd=true

Ссылка на тестирование требований, тест-кейсы, баг-репорты: 
https://docs.google.com/spreadsheets/d/1HX-lFI71BCHktzbxNOhFDt7CL5gVvJwAk125W1hbKYw/edit?usp=sharing

base.py - базовый класс, методы для страницы
auth_page - описание класса и локаторов страницы авторизации
elements.py - базовый класс, методы, процедуры для элементов
settings.py - данные для тестовых сценариев
config.py - файл с фикстурами
locators.py - файл с локаторами, не применялся в данной модели
requirements.txt - файл с зависимостями
pytesy.ini - файл для маркировки тестов

test_auth_page.py - набор автотестов для страницы авторизации

Запуск тестов:

Установить все внешние зависимости командой
pip install -r requirements.txt

Скачать версию Selenium WebDriver для Chrome 108 версии

Запустить тесты можно командой:
python -m pytest -v --driver Firefox --driver-path <Путь до вебдрайвера>\geckodriver.exe
python -m pytest -v --driver Chrome --driver-path <Путь до вебдрайвера>\chromedriver.exe       
