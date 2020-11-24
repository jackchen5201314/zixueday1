import os
import sys
import pytest
import allure
import yaml
from pythoncode.calcu import Calculator

print(sys.path.append(".."))


def test_add(haha):
    cal = Calculator()
    assert 6 == cal.add(1, 2, 3)


def test_add1(haha):
    cal = Calculator()
    assert 9 == cal.add(2, 3, 4)


def test_div():
    cal = Calculator()
    assert 5 == cal.div(10, 2)


@pytest.mark.parametrize("a,b,c", yaml.safe_load(open("../usrdata/data.yaml")))
def test_subtraction(a, b, c, haha):
    cal = Calculator()
    assert c == cal.subtraction(a, b)
