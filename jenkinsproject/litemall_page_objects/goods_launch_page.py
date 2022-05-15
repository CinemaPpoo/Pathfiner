# Author：Pathfinder
# 文件名: goods_create_page
# IDE ：PyCharm
import logging
import time

import allure
from selenium.webdriver.common.by import By

from litemall_page_objects.base_page import BasePage

"""
上架商品页面
提供页面的操作
提交上架商品后跳转到商品列表

"""


class GoodsLaunchPage(BasePage):
    _INPUT_GOODS_Number = (By.XPATH, "//label[@for='goodsSn']/..//input[@class='el-input__inner']")
    _INPUT_GOODS_NAME = (By.XPATH, "//label[@for='name']/..//input[@type='text']")
    _INPUT_MARKET_PRICE = (By.XPATH, "//label[@for='counterPrice']/..//input[@class='el-input__inner']")
    _RADIO_HOT = (By.XPATH, "//span[contains(text(),'热卖')]")
    _BUTTON_LAUNCH = (By.XPATH, "//div[@class='op-container']//span[contains(text(),'上架')]")
    _Button_ADD = (By.XPATH, "//button//*[contains(text(),'+ 增加')]")
    _IMAGE_GOODS_MASTER = (By.XPATH, "//div[@class='el-upload el-upload--picture-card']//input[@type='file']")

    def goods_launch(self, goods_number: str, goods_name: str, goods_counter_price: str):
        """
        输入商品编号
        输入商品名称，
        输入市场价，
        点击热卖，
        上传商品主图
        滑动到页面底部，
        点击上架按钮
        :return:
        """
        logging.info("3.创建商品")
        with allure.step("步骤3:创建商品"):
            # 输入商品编号
            logging.info("-输入商品编号")
            self.form_send_keys(*self._INPUT_GOODS_Number, goods_number)
            # 输入商品名称
            logging.info("-输入商品名称")
            self.form_send_keys(*self._INPUT_GOODS_NAME, goods_name)
            # 输入商品市场价格
            logging.info("-输入商品市场价格")
            self.form_send_keys(*self._INPUT_MARKET_PRICE, goods_counter_price)
            # 点击热卖
            logging.info("-点击热卖")
            self.button_click(*self._RADIO_HOT)
            # 上传商品主图
            logging.info("-上传商品主图")
            self.upload_image(*self._IMAGE_GOODS_MASTER,
                              r"C:\Users\Toshiya\Desktop\shilaimu\reiki_a_strawberryblue_QM7hkc.jpg")

            time.sleep(3)
            # 滑动到页面底部
            logging.info("-滑动到页面底部")
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            # 点击上架按钮
            logging.info("-点击上架按钮")
            self.button_click(*self._BUTTON_LAUNCH)

        from litemall_page_objects.goods_list_page import GoodsListPage
        # 跳转到商品列表
        return GoodsListPage(self.driver)
