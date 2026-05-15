"""测试数学运算模块"""

import sys
sys.path.insert(0, 'D:\\Code\\PyCode\\MetaX')

from metax.base.math import basic


def test_add():
    assert basic.add(10, 5) == 15
    assert basic.add(-1, 1) == 0
    print("加法测试通过")


def test_subtract():
    assert basic.subtract(10, 5) == 5
    assert basic.subtract(5, 10) == -5
    print("减法测试通过")


def test_multiply():
    assert basic.multiply(10, 5) == 50
    assert basic.multiply(-2, 3) == -6
    print("乘法测试通过")


def test_divide():
    assert basic.divide(10, 5) == 2.0
    assert basic.divide(7, 2) == 3.5
    print("除法测试通过")


if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("所有测试通过！")