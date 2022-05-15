# Author：Pathfinder
# 文件名: goods_list_page
# IDE ：PyCharm
import logging

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from litemall_page_objects.base_page import BasePage

"""
商品列表页面
提供页面的方法
"""


class GoodsListPage(BasePage):
    goods_name_edit = 'Mikoto'
    _TEXT_FIRST_ROW_GOODS_NAME = (By.XPATH, "//tbody//tr[1]//td[3]/div")
    _INPUT_GOODS_ID = (By.XPATH, "//input[@type='text'][@placeholder='请输入商品ID']")
    _INPUT_GOODS_NUMBER = (By.XPATH, "//input[@type='text'][@placeholder='请输入商品编号']")
    _INPUT_GOODS_NAME = (By.XPATH, "//input[@type='text'][@placeholder='请输入商品名称']")
    _GOODS_ID = (By.XPATH, f"//*[contains(text(),'{goods_name_edit}')]/../../td[2]/div")
    _GOODS_NAME = (By.XPATH, "//tr[@class='el-table__row current-row']//td[3]/div[@class='cell']")
    _BUTTON_GOODS_EDIT = (By.XPATH, "//tr[@class='el-table__row']//td[12]//span[contains(text(),'编辑')]")
    _BUTTON_GOODS_DELETE = (By.XPATH, "//tbody//tr[1]//td[12]//span[contains(text(),'删除')]")
    _BUTTON_SEARCH = (By.XPATH, "//i[@class='el-icon-search']")
    _TOAST_EDIT_SUCCESS = (By.XPATH, "//div[@class='el-notification__content']/p[contains(text(),'编辑成功')]")
    _TOAST_DELETE_SUCCESS = (By.XPATH, "//div[@class='el-notification__content']/p")

    # 获取商品名称
    def get_goods_name(self):
        # name = self.driver.find_element(*self._TEXT_GOODS_NAME).text
        # print(name)
        logging.info("4.获取上架商品名称")
        with allure.step("步骤4：获取上架商品名称"):
            wait = WebDriverWait(self.driver, 5)
            goods_name = wait.until(
                expected_conditions.visibility_of_element_located(self._TEXT_FIRST_ROW_GOODS_NAME)).text
            return goods_name

    # 获取删除成功toast
    def get_delete_success_toast(self):
        logging.info("4.获取删除成功TOAS")
        with allure.step("步骤4：获取删除成功TOAST"):
            result_toast = self.driver.find_element(*self._TOAST_DELETE_SUCCESS).get_attribute('innerText')
            return result_toast

    # 获取编辑成功toast
    def get_edit_success_toast(self):
        logging.info("5.获取编辑成功TOAST")
        with allure.step("步骤5：获取编辑成功TOAST"):
            result_toast = self.driver.find_element(*self._TOAST_EDIT_SUCCESS).get_attribute('innerText')
            return result_toast

    # 删除商品按钮
    def goods_delete(self):
        """
        商品删除按钮
        :return:
        """
        logging.info("3.用商品编码搜索商品，删除商品")
        with allure.step("步骤3：用商品编码搜索商品，删除商品"):
            # 用商品编码搜索出对应的商品
            logging.info("-用商品编码搜索商品")
            self.driver.find_element(*self._INPUT_GOODS_NUMBER).send_keys(f"{self.goods_number}")
            # 点击查找
            logging.info("-点击查找")
            self.button_click(*self._BUTTON_SEARCH)
            # 删除商品
            logging.info("-点击删除商品")
            self.button_click(*self._BUTTON_GOODS_DELETE)
            # 返回页面本身，继续调用页面的方法
            return self

    # 商品编辑按钮
    def goods_edit(self):
        """
        商品编辑按钮
        :return:
        """
        logging.info("3.用商品编码搜索出商品，点击编辑")
        with allure.step("步骤3：用商品编码搜索出商品，点击编辑"):
            # 用商品编码搜索出对应商品
            logging.info("-先用商品编码搜索出对应商品")
            self.driver.find_element(*self._INPUT_GOODS_NUMBER).send_keys(f"{self.goods_number}")
            # 点击查找按钮
            logging.info("-点击查找按钮")
            self.button_click(*self._BUTTON_SEARCH)
            # 点击编辑
            logging.info("-点击编辑")
            self.button_click(*self._BUTTON_GOODS_EDIT)
            from litemall_page_objects.goods_edit_page import GoodsEditPage
            # 跳转到商品编辑页面
            return GoodsEditPage(self.driver)

    # 用商品id搜索出对应商品
    def search_by_goods_id(self):
        """
        使用商品id搜索出对应商品
        :return:
        """
        logging.info("3.用商品id搜索对应商品")
        with allure.step("步骤3：用商品id搜索对应商品"):
            # 以商品名字定位对应的商品id
            logging.info("-获取商品名称的对应商品id")
            goods_id = self.driver.find_element(*self._GOODS_ID).get_attribute('innerText')
            # 搜索栏输入商品id
            logging.info("-搜索栏输入商品id")
            self.form_send_keys(*self._INPUT_GOODS_ID, goods_id)
            # 点击查找
            logging.info("-点击查找")
            self.button_click(*self._BUTTON_SEARCH)
            # 搜索出的商品
            logging.info("-获取搜索出的商品名称")
            wait = WebDriverWait(self.driver, 5)
            goods_id_search_result = wait.until(
                expected_conditions.visibility_of_element_located(self._TEXT_FIRST_ROW_GOODS_NAME)).text

            return goods_id_search_result

    # 用商品编码搜索出对应的商品
    def search_by_goods_number(self):
        """
        使用商品编码搜索出对应的商品
        :return:
        """
        logging.info("3.用商品编码搜索出对应的商品")
        with allure.step("步骤3：用商品编码搜索出对应的商品"):
            # 在搜索栏输入商品编码
            logging.info("-在搜索栏输入商品编码")
            self.form_send_keys(*self._INPUT_GOODS_NUMBER, self.goods_number)
            # 点击查找
            logging.info("-点击查找")
            self.button_click(*self._BUTTON_SEARCH)
            # 搜索出的商品
            logging.info("-获取搜索出的商品名称")
            wait = WebDriverWait(self.driver, 5)
            goods_number_search_result = wait.until(
                expected_conditions.visibility_of_element_located(self._TEXT_FIRST_ROW_GOODS_NAME)).text

            return goods_number_search_result

    # 用商品名搜索出对应的商品
    def search_by_goods_name(self):
        """
        使用商品名称搜索出对应的商品
        :return:
        """
        logging.info("3.用商品名搜索出对应的商品")
        with allure.step("步骤3：用商品名搜索出对应的商品"):
            # 在搜索栏输入商品名
            logging.info("-在搜索栏输入商品名")
            self.form_send_keys(*self._INPUT_GOODS_NAME, "Mikoto")
            # 点击查找
            logging.info("-点击查找")
            self.button_click(*self._BUTTON_SEARCH)
            # 搜索出的商品
            logging.info("-获取搜索出的商品名称")
            wait = WebDriverWait(self.driver, 5)
            goods_name_search_result = wait.until(
                expected_conditions.visibility_of_element_located(self._TEXT_FIRST_ROW_GOODS_NAME)).text

            return goods_name_search_result
