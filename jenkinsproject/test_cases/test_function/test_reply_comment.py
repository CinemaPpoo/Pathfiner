# Author：Pathfinder
# File_Name: test_reply_comment
# IDE ：PyCharm
from selenium.webdriver.common.by import By

from litemall_page_objects.login_page import LoginPage


class TestReplyComment:

    def setup(self):
        self.loginpage = LoginPage()

    def teardown(self):
        self.loginpage.driver.quit()

    def test_reply_comment(self):
        result_reply = self.loginpage.user_login().go_to_goods_comments().reply_comment().get_reply_failure_toast()
        print(result_reply)
        assert result_reply == "订单商品已回复！"
