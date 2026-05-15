"""基础数学运算模块"""

def add(a: float, b: float) -> float:
    """加法运算

    Args:
        a: 第一个数
        b: 第二个数

    Returns:
        两数之和
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """减法运算

    Args:
        a: 被减数
        b: 减数

    Returns:
        两数之差
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """乘法运算

    Args:
        a: 第一个数
        b: 第二个数

    Returns:
        两数之积
    """
    return a * b


def divide(a: float, b: float) -> float:
    """除法运算

    Args:
        a: 被除数
        b: 除数

    Returns:
        两数之商

    Raises:
        ZeroDivisionError: 当除数为0时抛出
    """
    if b == 0:
        raise ZeroDivisionError("除数不能为0")
    return a / b