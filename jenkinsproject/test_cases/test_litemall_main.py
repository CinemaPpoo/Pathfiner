# Author：Pathfinder
# File_Name: test_litrmall
# IDE ：PyCharm
import logging

import allure
import pytest

from litemall_page_objects.login_page import LoginPage

"""
测试页，通过链式调用实现业务操作后，断言
商品模块功能的自动化测试，商品搜索模块自动化测试，商品评论模块自动化测试
用例执行完，通过allure输出可视化测试报告
"""


@allure.feature("商品模块功能")
class TestGoodsModule:
    def setup(self):
        self.loginpage = LoginPage()

    def teardown(self):
        self.loginpage.driver.quit()

    # 创建商品

    @pytest.mark.run(order=1)
    @allure.story("商品上架测试")
    @pytest.mark.parametrize("goods_number,goods_name,goods_goods_counter_price", [["213132131", "Pathfinder", "8999"]])
    def test_goods_launch(self, goods_number, goods_name, goods_goods_counter_price):
        """
        1.账号登陆
        2.菜单栏点击商品上架
        3.上架商品
        4.获取上架商品的名称
        5.断言
        :return:
        """
        logging.info("用例1：商品上架测试开始--------------------------------------")
        name = self.loginpage.user_login() \
            .go_to_goods_launch() \
            .goods_launch(goods_number, goods_name, goods_goods_counter_price) \
            .get_goods_name()

        logging.info("5.断言")
        with allure.step("步骤5：断言"):
            assert name == "Pathfinder"

    @pytest.mark.run(order=2)
    @allure.story("编辑商品测试")
    def test_goods_edit(self):
        """
        1.账号登陆
        2.菜单栏点击商品列表
        3，用商品编码搜索对应商品，然后点击编辑按钮
        4。编辑商品名称，点击更新商品按钮
        5。获取编辑成功TOAST
        6.断言
        :return:
        """
        logging.info("用例2：编辑商品测试开始--------------------------------------")
        edit_success_toast = self.loginpage.user_login() \
            .go_to_goods_list() \
            .goods_edit() \
            .goods_update() \
            .get_edit_success_toast()

        logging.info("6.断言")
        with allure.step("步骤6：断言"):
            assert edit_success_toast == "编辑成功"

    @pytest.mark.run(order=6)
    @allure.story("删除商品测试")
    def test_delete_goods(self):
        """
        1.账号登陆
        2.菜单栏点击商品列表
        3.使用商品编码搜索出对应商品，点击删除
        4.获取删除成功TOAST
        5.断言
        :return:
        """
        logging.info("用例6：删除商品测试开始--------------------------------------")
        result_toast = self.loginpage.user_login() \
            .go_to_goods_list() \
            .goods_delete() \
            .get_delete_success_toast()

        logging.info("5.断言")
        with allure.step("步骤5：断言"):
            assert result_toast == "删除成功"


@allure.feature("商品搜索功能")
class TestSearch:
    def setup(self):
        self.loginpage = LoginPage()

    def teardown(self):
        self.loginpage.driver.quit()

    @pytest.mark.run(order=3)
    @allure.story("用商品id搜索商品测试")
    def test_search_by_goods_id(self):
        """
        1.账号登陆
        2.菜单栏点击商品列表
        3.用商品id搜索出对应商品
        4。断言
        :return:
        """
        logging.info("用例3：用商品id搜索商品测试开始--------------------------------------")
        result_name = self.loginpage.user_login() \
            .go_to_goods_list() \
            .search_by_goods_id()

        logging.info("4.断言")
        with allure.step("步骤4：断言"):
            assert result_name == "Mikoto"

    @pytest.mark.run(order=4)
    @allure.story("用商品名称搜索商品测试")
    def test_search_by_goods_name(self):
        """
        1.账号登陆
        2.菜单栏点击商品列表
        3.用商品名称搜索出对应商品
        4.断言
        :return:
        """
        logging.info("用例4：用商品名称搜索商品测试开始--------------------------------------")
        result_name = self.loginpage.user_login() \
            .go_to_goods_list() \
            .search_by_goods_name()

        logging.info("4.断言")
        with allure.step("步骤4：断言"):
            assert result_name == "Mikoto"

    @pytest.mark.run(order=5)
    @allure.story("用商品编码搜索商品测试")
    def test_search_by_goods_number(self):
        """
        1.账号登陆
        2.菜单栏点击商品列表
        3.用商品编码搜索出对应商品
        4.断言
        :return:
        """
        logging.info("用例5：用商品编码搜索商品测试开始--------------------------------------")
        result_name = self.loginpage.user_login() \
            .go_to_goods_list() \
            .search_by_goods_number()

        logging.info("4.断言")
        with allure.step("步骤4：断言"):
            assert result_name == "Mikoto"


@allure.feature("商品评论模块")
class TestReplyComment:

    def setup(self):
        self.loginpage = LoginPage()

    def teardown(self):
        self.loginpage.driver.quit()

    @pytest.mark.run(order=7)
    @allure.story("回复商品评论测试")
    def test_reply_comment(self):
        """
        1.账号登陆
        2.菜单栏点击商品评论
        3.点击回复
        4.获取回复失败TOAST
        5.断言
        :return:
        """
        logging.info("用例7：回复商品评论测试开始--------------------------------------")
        result_reply = self.loginpage.user_login() \
            .go_to_goods_comments() \
            .reply_comment() \
            .get_reply_failure_toast()

        logging.info("5.断言")
        with allure.step("步骤5：断言"):
            assert result_reply == "订单商品已回复！"

    @pytest.mark.run(order=8)
    @allure.story("删除商品评论测试")
    def test_delete_comment(self):
        """
        1.账号登陆
        2.删除商品评论
        3.获取删除评论成功TOAST
        4.断言
        :return:
        """
        logging.info("用例8：删除商品评论测试开始--------------------------------------")
        delete_toast = self.loginpage.user_login() \
            .go_to_goods_comments() \
            .delete_comment() \
            .get_delete_success_toast()

        logging.info("5.断言")
        with allure.step("步骤5：断言"):
            assert delete_toast == "删除成功"
