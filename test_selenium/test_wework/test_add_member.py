from test_selenium.test_wework.index import Index
from selenium import webdriver


class TestAddmember:
    def setup(self):
        self.index = Index()

    def test_add_member(self):
        self.index.goto_add_member().add_member()
