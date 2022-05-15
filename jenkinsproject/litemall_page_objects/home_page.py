# Author：Pathfinder
# 文件名: home_page
# IDE ：PyCharm
import logging

import allure
from selenium.webdriver.common.by import By

from litemall_page_objects.base_page import BasePage

"""
litemall首页
提供菜单的跳转
"""


class HomePage(BasePage):
    _MENU_GOODS_MANAGE = (By.XPATH, "//*[contains(text(),'商品管理')]")
    _MENU_GOODS_LAUNCH = (By.XPATH, "//*[contains(text(),'商品上架')]")
    _MENU_GOODS_LIST = (By.XPATH, "//*[contains(text(),'商品列表')]")
    _MENU_GOODS_COMMENTS = (By.XPATH, "//*[contains(text(),'商品评论')]")

    def go_to_goods_launch(self):
        """
        跳转到商品上架页
        :return:
        """
        # 点击商品管理菜单
        logging.info("2.菜单栏商品管理-商品上架")
        with allure.step("步骤2：菜单栏商品管理-商品上架"):
            # 点击菜单管理
            logging.info("-点击菜单管理")
            self.button_click(*self._MENU_GOODS_MANAGE)
            # 点击商品上架
            logging.info("-点击商品上架")
            self.button_click(*self._MENU_GOODS_LAUNCH)

        from litemall_page_objects.goods_launch_page import GoodsLaunchPage
        # 跳转到商品上架页
        return GoodsLaunchPage(self.driver)

    def go_to_goods_list(self):
        """
        跳转到商品列表页
        :return:
        """
        # 点击商品管理菜单
        logging.info("2.菜单栏商品管理-商品列表")
        with allure.step("步骤2：菜单栏商品管理-商品列表"):
            logging.info("-点击菜单管理")
            self.button_click(*self._MENU_GOODS_MANAGE)
            # 点击商品列表
            logging.info("-点击商品列表")
            self.button_click(*self._MENU_GOODS_LIST)

        from litemall_page_objects.goods_list_page import GoodsListPage
        # 跳转到商品列表
        return GoodsListPage(self.driver)

    def go_to_goods_comments(self):
        """
        跳转到商品评论页
        :return:
        """
        # 点击商品管理菜单
        logging.info("2.菜单栏商品管理-商品评论")
        with allure.step("步骤2：菜单栏商品管理-商品评论"):
            logging.info("-点击菜单管理")
            self.button_click(*self._MENU_GOODS_MANAGE)
            # 点击商品评论
            logging.info("-点击商品评论")
            self.button_click(*self._MENU_GOODS_COMMENTS)

        from litemall_page_objects.goods_comments_page import GoodsCommentsPage
        # 跳转到商品评论页面
        return GoodsCommentsPage(self.driver)
