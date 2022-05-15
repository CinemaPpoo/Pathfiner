# Author：Pathfinder
# File_Name: test_delete_goods
# IDE ：PyCharm
from litemall_page_objects.login_page import LoginPage


class TestDeleteGoods:
    def setup(self):
        self.loginpage = LoginPage()

    def teardown(self):
        self.loginpage.driver.quit()

    # 通过商品编码搜索对应的商品，点击删除
    def test_delete_goods(self):
        result_toast = self.loginpage.user_login()\
            .go_to_goods_list()\
            .goods_delete()\
            .get_delete_success_toast()
        # 断言
        assert result_toast == "删除成功"
