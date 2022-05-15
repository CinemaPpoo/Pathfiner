# Author：Pathfinder
# 文件名: test_goods_launch
# IDE ：PyCharm




class TestGoodsLaunch:
    def setup(self):
        self.loginpage = LoginPage()

    def teardown(self):
        self.loginpage.driver.quit()

    # 创建商品
    def test_goods_launch(self):
        name = self.loginpage.user_login().go_to_goods_launch().goods_launch().get_goods_name()
        assert name == "Pathfinder"
