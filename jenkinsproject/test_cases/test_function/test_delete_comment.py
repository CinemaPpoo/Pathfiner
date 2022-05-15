# Author：Pathfinder
# File_Name: test_delete_comment
# IDE ：PyCharm
from litemall_page_objects.login_page import LoginPage


class TestDeleteComment:
    def setup(self):
        self.loginpage = LoginPage()

    def teardown(self):
        self.loginpage.driver.quit()

    def test_delete_comment(self):
        delete_toast = self.loginpage.user_login().go_to_goods_comments().delete_comment().get_delete_success_toast()
        assert delete_toast == "删除成功"
