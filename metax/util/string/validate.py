"""字符串验证工具"""

import re
from typing import Optional


def is_empty(text: str, ignore_whitespace: bool = False) -> bool:
    """判断是否为空字符串

    Args:
        text: 输入字符串
        ignore_whitespace: 是否忽略空白字符，默认为False

    Returns:
        是否为空
    """
    if ignore_whitespace:
        return len(text.strip()) == 0
    return len(text) == 0


def is_numeric(text: str) -> bool:
    """判断是否为数字

    Args:
        text: 输入字符串

    Returns:
        是否为数字
    """
    try:
        float(text)
        return True
    except ValueError:
        return False


def is_integer(text: str) -> bool:
    """判断是否为整数

    Args:
        text: 输入字符串

    Returns:
        是否为整数
    """
    try:
        int(text)
        return True
    except ValueError:
        return False


def is_alpha(text: str) -> bool:
    """判断是否只包含字母

    Args:
        text: 输入字符串

    Returns:
        是否只包含字母
    """
    return text.isalpha()


def is_alphanumeric(text: str) -> bool:
    """判断是否只包含字母和数字

    Args:
        text: 输入字符串

    Returns:
        是否只包含字母和数字
    """
    return text.isalnum()


def is_email(text: str) -> bool:
    """判断是否为有效邮箱

    Args:
        text: 输入字符串

    Returns:
        是否为有效邮箱
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, text))


def is_phone_cn(text: str) -> bool:
    """判断是否为中国大陆手机号

    Args:
        text: 输入字符串

    Returns:
        是否为有效手机号
    """
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, text))


def is_id_card_cn(text: str) -> bool:
    """判断是否为中国大陆身份证号

    Args:
        text: 输入字符串

    Returns:
        是否为有效身份证号
    """
    # 15位或18位身份证号
    pattern = r'^\d{15}|\d{17}[\dXx]$'
    return bool(re.match(pattern, text))


def is_url(text: str) -> bool:
    """判断是否为有效URL

    Args:
        text: 输入字符串

    Returns:
        是否为有效URL
    """
    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, text, re.IGNORECASE))


def is_ip(text: str) -> bool:
    """判断是否为有效IP地址

    Args:
        text: 输入字符串

    Returns:
        是否为有效IP地址
    """
    # IPv4
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(ipv4_pattern, text):
        parts = text.split('.')
        return all(0 <= int(part) <= 255 for part in parts)
    return False


def is_hex_color(text: str) -> bool:
    """判断是否为十六进制颜色值

    Args:
        text: 输入字符串

    Returns:
        是否为有效颜色值
    """
    pattern = r'^#?([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$'
    return bool(re.match(pattern, text))


def is_date(text: str, fmt: str = "%Y-%m-%d") -> bool:
    """判断是否为有效日期

    Args:
        text: 输入字符串
        fmt: 日期格式，默认为"%Y-%m-%d"

    Returns:
        是否为有效日期
    """
    from datetime import datetime
    try:
        datetime.strptime(text, fmt)
        return True
    except ValueError:
        return False


def is_chinese(text: str) -> bool:
    """判断是否只包含中文

    Args:
        text: 输入字符串

    Returns:
        是否只包含中文
    """
    pattern = r'^[一-龥]+$'
    return bool(re.match(pattern, text))


def contains_chinese(text: str) -> bool:
    """判断是否包含中文

    Args:
        text: 输入字符串

    Returns:
        是否包含中文
    """
    pattern = r'[一-龥]'
    return bool(re.search(pattern, text))


def length_between(text: str, min_len: int, max_len: int) -> bool:
    """判断字符串长度是否在指定范围内

    Args:
        text: 输入字符串
        min_len: 最小长度
        max_len: 最大长度

    Returns:
        长度是否在范围内
    """
    return min_len <= len(text) <= max_len


def matches(text: str, pattern: str) -> bool:
    """判断是否匹配正则表达式

    Args:
        text: 输入字符串
        pattern: 正则表达式

    Returns:
        是否匹配
    """
    return bool(re.match(pattern, text))
