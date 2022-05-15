# Author：Pathfinder
# File_Name: goods_edit_page
# IDE ：PyCharm
import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from litemall_page_objects.base_page import BasePage

"""
商品编辑页面
提供页面的操作
编辑页面提交后跳转到商品列表页面
"""


class GoodsEditPage(BasePage):
    _INPUT_NAME_EDIT = (By.XPATH, "//label[@for='name']/..//input[@type='text']")
    _BUTTON_GOODS_UPDATE = (By.XPATH, "//div//button//span[contains(text(),'更新商品')]")
    _TEXT_FIRST_ROW_GOODS_NAME = (By.XPATH, "//tbody//tr[1]//td[3]/div")

    # 编辑商品
    def goods_update(self):
        """
        编辑商品名称，
        滑动页面到底部，
        点击更新商品
        :return:
        """
        logging.info("4.编辑商品名称")
        with allure.step("步骤4：编辑商品名称"):
            wait = WebDriverWait(self.driver, 5)
            # 等待商品名称文本框元素出现
            wait.until(expected_conditions.visibility_of_element_located(self._INPUT_NAME_EDIT))
            # 清空输入框，更改商品名
            logging.info("-清空输入框，更改商品名")
            self.form_send_keys(*self._INPUT_NAME_EDIT, "Mikoto")
            # 滚动页面到底部
            logging.info("-滚动页面到底部")
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            # 点击更新商品按钮
            logging.info("-点击更新商品按钮")
            self.button_click(*self._BUTTON_GOODS_UPDATE)

        from litemall_page_objects.goods_list_page import GoodsListPage
        # 返回商品列表
        return GoodsListPage(self.driver)
