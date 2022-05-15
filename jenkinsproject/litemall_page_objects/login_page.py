# Author：Pathfinder
# 文件名: login_page
# IDE ：PyCharm
import logging

import allure
from selenium.webdriver.common.by import By

from litemall_page_objects.base_page import BasePage

"""
账号登陆页面
提供账号登陆操作
"""


class LoginPage(BasePage):
    _INPUT_USER_NAME = (By.XPATH, "//*[@name='username']")
    _INPUT_PASSWORD = (By.XPATH, "//*[@name='password']")
    _BUTTON_LOGIN = (By.CSS_SELECTOR, "button.el-button")

    def user_login(self):
        """
        输入账号
        输入密码
        点击登陆
        :return:
        """
        # 输入登陆账号
        logging.info("1.账号登陆")
        with allure.step("步骤1：输入账号id和密码，点击登陆"):
            logging.info("-输入账号ID")
            self.form_send_keys(*self._INPUT_USER_NAME, "admin123")
            # 输入登陆密码
            logging.info("-输入账号密码")
            self.form_send_keys(*self._INPUT_PASSWORD, "admin123")
            # 点击登陆
            logging.info("-点击登陆")
            self.button_click(*self._BUTTON_LOGIN)

        from litemall_page_objects.home_page import HomePage
        # 跳转到首页
        return HomePage(self.driver)
