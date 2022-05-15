# Author：Pathfinder
# 文件名: base_page
# IDE ：PyCharm
import logging

import allure
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.by import By

"""
基类，让其他页面类继承其driver和基本操作方法
"""


class BasePage:
    _BASE_URL = "http://litemall.hogwarts.ceshiren.com/"

    def __init__(self, driver: WebDriver = None):
        """
        如果没有driver,创建一个driver,如果有driver就继续沿用
        :param driver:
        """

        if driver is None:

            self.driver = webdriver.Chrome()
            self.driver.get(self._BASE_URL)
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
        else:
            self.driver = driver

        # 商品编码
        self.goods_number = "213132131"

    # 点击按钮
    def button_click(self, by: By, locator: str):
        """
        :param by: 定位方式
        :param locator: 定位
        :return:
        """
        self.driver.find_element(by, locator).click()

    # 清空输入框后，填写内容
    def form_send_keys(self, by: By, locator: str, value: str):
        """
        :param by: 定位方式
        :param locator: 定位
        :param value: 输入的值
        :return:
        """
        el = self.driver.find_element(by, locator)
        # 清空输入框
        el.clear()
        # 输入值
        el.send_keys(value)

    # 上传图片
    def upload_image(self, by: By, locator: str, value: str):
        """
        :param by: 定位方式
        :param locator: 定位
        :param value: 图片本地路径，注意转义符
        :return:
        """
        self.driver.find_element(by, locator).send_keys(value)
