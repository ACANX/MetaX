"""高级数学运算模块"""

import math


def power(base: float, exponent: float) -> float:
    """幂运算

    Args:
        base: 底数
        exponent: 指数

    Returns:
        base的exponent次幂
    """
    return math.pow(base, exponent)


def sqrt(x: float) -> float:
    """开平方

    Args:
        x: 被开方数

    Returns:
        平方根

    Raises:
        ValueError: 当x为负数时抛出
    """
    if x < 0:
        raise ValueError("不能对负数开平方")
    return math.sqrt(x)


def cbrt(x: float) -> float:
    """开立方

    Args:
        x: 被开方数

    Returns:
        立方根
    """
    if x >= 0:
        return x ** (1/3)
    return -abs(x) ** (1/3)


def sin(x: float) -> float:
    """正弦函数

    Args:
        x: 弧度值

    Returns:
        正弦值
    """
    return math.sin(x)


def cos(x: float) -> float:
    """余弦函数

    Args:
        x: 弧度值

    Returns:
        余弦值
    """
    return math.cos(x)


def tan(x: float) -> float:
    """正切函数

    Args:
        x: 弧度值

    Returns:
        正切值
    """
    return math.tan(x)


def log(x: float, base: float = math.e) -> float:
    """对数函数

    Args:
        x: 真数
        base: 底数，默认为自然对数

    Returns:
        对数值

    Raises:
        ValueError: 当x<=0或base<=0或base==1时抛出
    """
    if x <= 0:
        raise ValueError("真数必须大于0")
    if base <= 0 or base == 1:
        raise ValueError("底数必须大于0且不等于1")
    return math.log(x, base)


def log10(x: float) -> float:
    """常用对数（以10为底）

    Args:
        x: 真数

    Returns:
        对数值
    """
    return math.log10(x)


def log2(x: float) -> float:
    """二进制对数（以2为底）

    Args:
        x: 真数

    Returns:
        对数值
    """
    return math.log2(x)


def abs(x: float) -> float:
    """绝对值

    Args:
        x: 数值

    Returns:
        绝对值
    """
    return math.fabs(x)


def round(x: float, ndigits: int = 0) -> float:
    """四舍五入

    Args:
        x: 数值
        ndigits: 保留小数位数，默认为0

    Returns:
        四舍五入后的值
    """
    return builtins.round(x, ndigits)


import builtins


def floor(x: float) -> int:
    """向下取整

    Args:
        x: 数值

    Returns:
        向下取整后的整数
    """
    return math.floor(x)


def ceil(x: float) -> int:
    """向上取整

    Args:
        x: 数值

    Returns:
        向上取整后的整数
    """
    return math.ceil(x)


def factorial(n: int) -> int:
    """阶乘

    Args:
        n: 非负整数

    Returns:
        n的阶乘

    Raises:
        ValueError: 当n为负数时抛出
    """
    return math.factorial(n)


def gcd(a: int, b: int) -> int:
    """最大公约数

    Args:
        a: 第一个整数
        b: 第二个整数

    Returns:
        最大公约数
    """
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """最小公倍数

    Args:
        a: 第一个整数
        b: 第二个整数

    Returns:
        最小公倍数
    """
    return abs(a * b) // math.gcd(a, b)
