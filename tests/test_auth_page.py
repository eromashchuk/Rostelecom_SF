# !/usr/bin/python3
# -*- encoding=utf8 -*-
import time

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chromedriver.exe tests/*


import pytest

from generators import *
from pages.auth_page import AuthPage


class TestAuthPositive:
    ''' Positive tests for Auth page test cases '''

    # TK-004 Проверка смены вкладок авторизации и смену подсказок в инпуте
    def test_auth_tabs_default(self, web_browser):
        page = AuthPage(web_browser)
        assert page.placeholder_login.get_text() == 'Мобильный телефон' #(TK-005 вкладка по телефону по-умолчанию)
        assert page.placeholder_pswrd.get_text() == 'Пароль'
        page.by_email.click()
        assert page.placeholder_login.get_text() == 'Электронная почта'
        page.by_login.click()
        assert page.placeholder_login.get_text() == 'Логин'
        page.by_LS.click()
        assert page.placeholder_login.get_text() == 'Лицевой счёт'

    # TK-006 Проверка автосмены вкладок при вводе логина
    def test_autochange_of_auth_tabs(self, web_browser):
        page = AuthPage(web_browser)
        # Input phone_number to the login field
        page.login.send_keys('79787569117')
        page.password.send_keys('')
        assert page.placeholder_login.get_text() == 'Мобильный телефон'
        page.login.clear()

        # Input email to the login field
        page.login.send_keys('test@test.io')
        page.password.send_keys('')
        assert page.placeholder_login.get_text() == 'Электронная почта'
        page.login.clear()

        # Input login to the login field
        page.login.send_keys('login')
        page.password.send_keys('')
        assert page.placeholder_login.get_text() == 'Логин'
        page.login.clear()

    # TK-010 Успешная авторизация по email (не стала делать параметризацию, но подразумеваю)
    def test_successful_login_by_email(self, web_browser, email='chudin.v@gmail.com', password='A123456789a'):
        page = AuthPage(web_browser)
        page.login.send_keys(email)
        page.password.send_keys(password)
        page.check_box.click()
        page.submit_btn.click()
        next_page = page.get_current_url()
        assert 'https://b2c.passport.rt.ru/account_b2c/page' in next_page

    # TK-007, TK-008, TK-009 Упешная авторизация по номеру телефона, нельзя ввести более 11 символов:
    @pytest.mark.parametrize("phone", ['79787569117', '89787569117', '797875691171']
        , ids=['valid phone starts from 7', 'valid phone starts from 8', 'valid phone +1']) #Тут можно добавить номер для +375, но у меня нет
    def test_successful_login_by_phone(self, web_browser, phone, password='A123456789a'):
        page = AuthPage(web_browser)
        page.login.send_keys(phone)
        page.password.send_keys(password)
        page.check_box.is_clickable()
        page.submit_btn.click()
        next_page = page.get_current_url()
        assert 'https://b2c.passport.rt.ru/account_b2c/page' in next_page

    #Проверка валидации ввода в поле Логина, принимает любые символы
    @pytest.mark.skip(reason='too much time need to check, but it work')
    @pytest.mark.xfail(reason='Known bug: phone-login field not allow some special characters')
    @pytest.mark.parametrize("login", [generate_string(255), alphabet_chars(), alphabet_chars().upper()
        , russian_chars(), russian_chars().upper()
        , chinese_chars(), special_chars(), '0123456789']
        , ids=['255 symbols', 'english', 'ENGLISH', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
    def test_successful_input_for_login(self, web_browser, login, password='1'):
        page = AuthPage(web_browser)
        page.login.send_keys(login)
        page.password.send_keys(password)
        text = page.login_value.get_attribute(attr_name='innerHTML')
        assert str(login) in text

    # ТК-023 Проверка ссылки пользовательского соглашения
    @pytest.mark.xfail(reason='Known bug for naming of agreement, need capital letter')
    def test_successful_redirect_to_contract(self, web_browser):
        page = AuthPage(web_browser)
        text = page.auth_policy.get_attribute(attr_name='innerHTML')
        assert 'Пользовательского Соглашения' in text
        assert page.auth_policy.is_clickable()
        page.auth_policy.click()
        next_page = page.auth_policy.get_attribute(attr_name='href')
        assert 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html' in next_page

    # Проверка перехода в форму восстановления пароля("Забыл пароль")
    def test_fogot_password_link(self, web_browser):
        page = AuthPage(web_browser)
        page.forgot_pswrd_link.click()
        assert page.forgot_password_form.is_presented()
        assert page.forgot_password_form.get_attribute(attr_name='innerHTML') == 'Восстановление пароля'

    # Проверка перехода в форму Регистрации
    def test_register_link(self, web_browser):
        page = AuthPage(web_browser)
        page.register.click()
        assert page.register_form.is_presented()
        assert page.register_form.get_attribute(attr_name='innerHTML') == 'Регистрация'

    # TK-017, TK-018, TK-019, TK-020, TK-021 Проверка авторизации церез oauth соц.сети
    def test_auth_by_social_services(self, web_browser):
        page = AuthPage(web_browser)
        # Авторизация через Вконтакте
        page.vk_btn.click()
        assert 'oauth.vk.com' in page.get_page_source()
        page.go_back()

        # Авторизация через Одноклассники
        page.ok_btn.click()
        assert 'connect.ok.ru' in page.get_current_url()
        page.go_back()

        # Авторизация через Мэил.ру
        page.mailru_btn.click()
        assert 'connect.mail.ru' in page.get_current_url()
        page.go_back()

        # Авторизация через Гугл
        page.google_btn.click()
        assert 'accounts.google.com' in page.get_current_url()
        page.go_back()

        # Авторизация через Яндекс
        page.ya_btn.click()
        assert 'passport.yandex.ru' in page.get_current_url()



class TestAuthNegative:
    ''' Negative tests for Auth page test cases '''

    #TK-011, TK-013, TK-015 Нельзя авторизоваться с неверным номером телефона, имейлом, логином, лицевым счетом
    @pytest.mark.parametrize("login"
        , ['shumak@gmail.com', 'test@test', '7978756911', 'w_login']
        , ids=['existing email', 'wrong email', 'wrong phone number', 'wrong login'])
    #@pytest.mark.parametrize("password", ['A123456789a', '*'], ids=['existing password for other profile', 'wrong password'])
    def test_unsuccessful_login_by_wrong_login_password(self, web_browser, login, password='*'):
        page = AuthPage(web_browser)
        page.login.send_keys(login)
        page.password.send_keys(password)
        page.submit_btn.click()
        next_page = page.get_current_url()
        assert 'https://b2c.passport.rt.ru/account_b2c/page' not in next_page
        assert 'https://b2c.passport.rt.ru/auth/realms/b2c/' in next_page
        assert page.invalid_login_message.is_presented()
        assert page.forgot_orange_link.is_presented()
        assert page.forgot_pswrd_link.is_presented()

    # TK-022 Проверка сообщения об ошибке для пустого логина (для пароля не реализовано BUG-07)
    def test_message_for_empty_login(self, web_browser):
        page = AuthPage(web_browser)
        page.submit_btn.click()
        assert page.error_empty_login.is_presented()


