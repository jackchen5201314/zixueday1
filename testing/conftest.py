import pytest


@pytest.fixture()
def haha():
    print("我开始了,计算")
    yield
    print("测试结束123")
