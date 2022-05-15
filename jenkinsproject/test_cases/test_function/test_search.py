# Author：Pathfinder
# File_Name: test_search
# IDE ：PyCharm
# 在商品列表用商品ID搜索商品
from litemall_page_objects.login_page import LoginPage


class TestSearch:
    def setup(self):
        self.loginpage = LoginPage()

    def teardown(self):
        self.loginpage.driver.quit()

    # 用商品ID查找商品
    def test_search_by_goods_id(self):
        result_name = self.loginpage.user_login().go_to_goods_list().search_by_goods_id()
        print(result_name)
        assert result_name == "Mikoto"

    # 用商品名称查找商品
    def test_search_by_goods_name(self):
        result_name = self.loginpage.user_login() \
            .go_to_goods_list() \
            .search_by_goods_name()
        assert result_name == "Mikoto"

    # 用商品编码查找商品
    def test_search_by_goods_number(self):
        result_name = self.loginpage.user_login() \
            .go_to_goods_list() \
            .search_by_goods_number()
        assert result_name == "Mikoto"
