#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("AUTH_URL") or 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

        # self.login = web_driver.find_element(*MainPageLocators.LOGIN)
        # self.password = web_driver.find_element(*MainPageLocators.PASSWORD)
        # self.submit_btn = web_driver.find_element(*MainPageLocators.SUBMIT_BTN)
        # self.forgot = web_driver.find_element(*MainPageLocators.FORGOT_BTN)
        # self.register = web_driver.find_element(*MainPageLocators.REGISTER)
        # self.placeholder = web_driver.find_element(*MainPageLocators.PLACEHOLDER)
        # self.contract = web_driver.find_element(*MainPageLocators.CONTRACT)
        # self.vk_btn = web_driver.find_element(*MainPageLocators.VK_BTN)
        # self.ok_btn = web_driver.find_element(*MainPageLocators.OK_BTN)
        # self.mailru_btn = web_driver.find_element(*MainPageLocators.MAILRU_BTN)
        # self.google_btn = web_driver.find_element(*MainPageLocators.GOOGLE_BTN)
        # self.ya_btn = web_driver.find_element(*MainPageLocators.YA_BTN)

    # Tabs for the auth form
    by_phone = WebElement(id='t-btn-tab-phone')
    by_email = WebElement(id='t-btn-tab-mail')
    by_login = WebElement(id='t-btn-tab-login')
    by_LS = WebElement(id='t-btn-tab-ls')

    # Input fields of the auth form
    login = WebElement(id='username')
    login_value = WebElement(css_selector='div.tabs-input-container__login > div > div.rt-input__input-value')
    password = WebElement(id='password')
    placeholder_login = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    placeholder_pswrd = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]')
    show_hide_pswrd = WebElement(css_selector='.rt-input__eye > path')
    typed_pswrd = WebElement(xpath='//span[@class="rt-input__mask-start" and @xpath="1"]')

    # Another elements of the auth form
    check_box = WebElement(class_name='rt-checkbox__label')
    submit_btn = WebElement(id='kc-login')

    forgot_pswrd = WebElement(id='forgot_password')
    forgot_orange = WebElement(
        css_selector='.rt-link.rt-link--orange.login-form__forgot-pwd.login-form__forgot-pwd--animated')
    contract = WebElement(id='rt-footer-agreement-link')

    register = WebElement(id='kc-register')

    #Auth by social medias
    vk_btn = WebElement(id='oidc_vk')
    ok_btn = WebElement(id='oidc_ok')
    mailru_btn = WebElement(id='oidc_mail')
    google_btn = WebElement(id='oidc_google')
    ya_btn = WebElement(id='oidc_ya')

    #Erorr messages for page
    error_empty_login = WebElement(class_name='.rt-input-container__meta.rt-input-container__meta--error')
