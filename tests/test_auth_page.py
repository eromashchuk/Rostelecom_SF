# !/usr/bin/python3
# -*- encoding=utf8 -*-

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
from settings import *


class TestAuthPositive:
    ''' Positive tests for Auth page test cases '''

    # Проверка смены вкладок авторизации и смену подсказок в инпуте(по телефону по-умолчанию)
    @pytest.mark.skip
    def test_auth_tabs_default(self, web_browser):
        page = AuthPage(web_browser)
        assert page.placeholder_login.get_text() == 'Мобильный телефон'
        assert page.placeholder_pswrd.get_text() == 'Пароль'
        page.by_email.click()
        assert page.placeholder_login.get_text() == 'Электронная почта'
        page.by_login.click()
        assert page.placeholder_login.get_text() == 'Логин'
        page.by_LS.click()
        assert page.placeholder_login.get_text() == 'Лицевой счёт'

    # Проверка автосмены вкладок при вводе логина
    @pytest.mark.skip
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

    # Упешная авторизация по email
    @pytest.mark.skip
    def test_successful_login_by_email(self, web_browser, exist_email_dot_in_name, valid_pass_ch_7_8):
        page = AuthPage(web_browser)
        page.login.send_keys(exist_email_dot_in_name)
        page.password.send_keys(valid_pass_ch_7_8)
        page.check_box.is_clickable()
        page.submit_btn.click()
        next_page = page.get_current_url()
        assert 'https://b2c.passport.rt.ru/account_b2c/page' in next_page

        # Упешная авторизация по номеру телефона:
    def test_successful_login_by_email(self, web_browser, exist_email_dot_in_name, valid_pass_ch_7_8):
        page = AuthPage(web_browser)
        page.login.send_keys(exist_email_dot_in_name)
        page.password.send_keys(valid_pass_ch_7_8)
        page.check_box.is_clickable()
        page.submit_btn.click()
        next_page = page.get_current_url()
        assert 'https://b2c.passport.rt.ru/account_b2c/page' in next_page

    @pytest.mark.skip
    @pytest.mark.parametrize("login", [generate_string(255), alphabet_chars(), alphabet_chars().upper()
        , russian_chars(), russian_chars().upper()
        , chinese_chars(), special_chars(), '0123456789']
        , ids=['255 symbols', 'english', 'ENGLISH', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])
    def test_successful_input_for_email(self, web_browser, login, password='1'):
        page = AuthPage(web_browser)
        page.login.send_keys(login)
        page.password.send_keys(password)
        assert login in page.placeholder.get_text()

class TestAuthNegative:
    @pytest.mark.skip
    def test_unsuccessful_login_by_wrong_password(self, web_browser, login, password):
        page = AuthPage(web_browser)
        page.login.send_keys(login)
        page.password.send_keys(password)
        page.check_box.is_clickable()
        page.submit_btn.click()
        next_page = page.get_current_url()
