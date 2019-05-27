import allure


class Test002:
    def test_add_png(self):
        with open("C:\\Users\\bob1994\\Desktop\\day_009\\scripts\\abc.png", "rb")as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
