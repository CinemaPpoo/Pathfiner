# Author：Pathfinder
# File_Name: test_goods_edit
# IDE ：PyCharm
import time

from litemall_page_objects.login_page import LoginPage


class TestGoodsEdit:
    def setup(self):
        self.loginpage = LoginPage()

    def teardown(self):
        self.loginpage.driver.quit()

    def test_goods_edit(self):
        edit_success_toast = self.loginpage.user_login()\
            .go_to_goods_list()\
            .goods_edit()\
            .goods_update()\
            .get_edit_success_toast()
        print(edit_success_toast)
        assert edit_success_toast == "编辑成功"
