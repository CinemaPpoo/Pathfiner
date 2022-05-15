# Author：Pathfinder
# File_Name: goods_comments_page
# IDE ：PyCharm
import logging

import allure
from selenium.webdriver.common.by import By

from litemall_page_objects.base_page import BasePage

"""
商品评论页面
提供页面操作
"""


class GoodsCommentsPage(BasePage):
    # 评论回复按钮定位
    _BUTTON_REPLY_COMMENT = (By.XPATH, "//tr[1][@class='el-table__row']/td[7]//span[contains(text(),'回复')]")
    # 评论删除按钮定位
    _BUTTON_DELETE_COMMENT = (By.XPATH, "//tr[1][@class='el-table__row']/td[7]//span[contains(text(),'删除')]")
    # 回复评论后，确定按钮
    _BUTTON_CONFIRM = (By.XPATH,
                       "//div[@class='dialog-footer']//button[@class='el-button el-button--primary el-button--mini']/span[contains(text(),'确定')]")
    # 评论回复失败TOAST
    _TOAST_REPLY_COMMENT_FAILURE = (By.XPATH, "//div[@class='el-notification__content']/p[contains(text(),'订单商品已回复！')]")
    # 评论回复成功TOAST
    _TOAST_REPLY_COMMENT_SUCCESS = (By.XPATH, "//div[@class='el-notification__content']/p[contains(text(),'回复成功')]")
    # 评论删除成功TOAST
    _TOAST_DELETE_COMMENT_SUCCESS = (By.XPATH, "//div[@class='el-notification__content']/p[contains(text(),'删除成功')]")
    # 回复评论输入框定位
    _INPUT_TEXTAREA = (By.XPATH, "//textarea[@class='el-textarea__inner']")
    # 回复失败标题
    _TEXT_TITTLE_FAILURE = (By.XPATH, "//h2[@class='el-notification__title'][contains(text(),'失败')]")
    # 回复成功标题
    _TEXT_TITTLE_SUCCESS = (By.XPATH, "//h2[@class='el-notification__title'][contains(text(),'成功')]")

    # 回复评论
    def reply_comment(self):
        """
        使用商品编码搜索对应的商品，
        点击编辑，
        填写内容，
        点击确定
        :return:
        """
        logging.info("3.回复评论")
        with allure.step("步骤3：回复评论"):
            # 回复评论文本框内容
            reply_text = '谢谢你的评论'
            # 点击回复
            logging.info("-点击回复")
            self.button_click(*self._BUTTON_REPLY_COMMENT)
            # 在回复评论文本框填写内容
            logging.info("-在回复评论文本框填写内容")
            self.form_send_keys(*self._INPUT_TEXTAREA, reply_text)
            # 点击确认
            logging.info("-点击确认")
            self.button_click(*self._BUTTON_CONFIRM)
            # 返回自己页面，继续调用页面方法
            return self

    # 删除评论
    def delete_comment(self):
        """
        点击删除商品按钮
        :return:
        """
        logging.info("3.删除评论")
        with allure.step("步骤3：删除评论"):
            self.button_click(*self._BUTTON_DELETE_COMMENT)

            return self

    # 获取删除成功toast
    def get_delete_success_toast(self):
        """
        获取删除评论成功的TOAST
        :return:
        """
        logging.info("4.获取删除成功toast")
        with allure.step("步骤4：获取删除成功toast"):
            result_toast = self.driver.find_element(*self._TOAST_DELETE_COMMENT_SUCCESS).get_attribute('innerText')

            return result_toast

    # 获取回复失败toast
    def get_reply_failure_toast(self):
        """
        获取回复评论失败的TOAST
        :return:
        """
        logging.info("4.获取回复失败toast")
        with allure.step("步骤4：获取回复失败toast"):
            result_toast = self.driver.find_element(*self._TOAST_REPLY_COMMENT_FAILURE).get_attribute('innerText')

            return result_toast
