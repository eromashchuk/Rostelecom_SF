Финальный проект для курса "Тестировщик - автоматизатор на PYTHON"

Тестирование формы авторизации Личного кабинета Ростелеком https://b2c.passport.rt.ru

Ссылка на требования по проекту - https://docs.google.com/document/d/14TRuoYG8JXlLCMXuesBXrbNK7OefVxMW/edit?usp=share_link&ouid=102111731768085493149&rtpof=true&sd=true

Ссылка на тестирование требований, тест-кейсы, баг-репорты: 
https://docs.google.com/spreadsheets/d/1HX-lFI71BCHktzbxNOhFDt7CL5gVvJwAk125W1hbKYw/edit?usp=sharing

base_page.py - базовый класс, функции
reg_page.py - класс для страницы регистрации
locators.py - локаторы для автотестов
settings.py - данные для тестовых сценариев
config.py - файл с фикстурами

test_rt_login.py - набор автотестов для страницы авторизации
test_rt_reg.py - набор автотестов для страницы регистрации


Запуск тестов:

Установить все внешние зависимости командой
pip install -r requirements.txt

Скачать версию Selenium WebDriver для Chrome 108 версии

Запустить тесты можно командой:
python -m pytest -v --driver Firefox --driver-path <Путь до вебдрайвера>\geckodriver.exe
python -m pytest -v --driver Chrome --driver-path <Путь до вебдрайвера>\chromedriver.exe
