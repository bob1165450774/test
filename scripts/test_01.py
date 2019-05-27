import allure
import pytest


class Test001:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是测试步骤01")
    def test_001(self):
        print("llll")
        allure.attach("标题", "具体内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是测试步骤02")
    def test_002(self):
        print("2222")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是测试步骤02")
    def test_002(self):
        print("2222")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是测试步骤02")
    def test_002(self):
        print("2222")
        assert True