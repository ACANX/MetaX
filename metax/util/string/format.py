"""字符串格式化工具"""

import re
from datetime import datetime
from typing import Any, Optional


def capitalize(text: str) -> str:
    """首字母大写

    Args:
        text: 输入字符串

    Returns:
        首字母大写的字符串
    """
    return text.capitalize()


def title(text: str) -> str:
    """每个单词首字母大写

    Args:
        text: 输入字符串

    Returns:
        每个单词首字母大写的字符串
    """
    return text.title()


def upper(text: str) -> str:
    """转大写

    Args:
        text: 输入字符串

    Returns:
        大写字符串
    """
    return text.upper()


def lower(text: str) -> str:
    """转小写

    Args:
        text: 输入字符串

    Returns:
        小写字符串
    """
    return text.lower()


def swapcase(text: str) -> str:
    """大小写互换

    Args:
        text: 输入字符串

    Returns:
        大小写互换后的字符串
    """
    return text.swapcase()


def reverse(text: str) -> str:
    """反转字符串

    Args:
        text: 输入字符串

    Returns:
        反转后的字符串
    """
    return text[::-1]


def truncate(text: str, length: int, suffix: str = "...") -> str:
    """截断字符串

    Args:
        text: 输入字符串
        length: 最大长度
        suffix: 截断后缀，默认为"..."

    Returns:
        截断后的字符串
    """
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix


def strip(text: str, chars: Optional[str] = None) -> str:
    """去除首尾空白字符

    Args:
        text: 输入字符串
        chars: 要去除的字符，默认为空白字符

    Returns:
        去除首尾字符后的字符串
    """
    return text.strip(chars)


def lstrip(text: str, chars: Optional[str] = None) -> str:
    """去除左侧空白字符

    Args:
        text: 输入字符串
        chars: 要去除的字符，默认为空白字符

    Returns:
        去除左侧字符后的字符串
    """
    return text.lstrip(chars)


def rstrip(text: str, chars: Optional[str] = None) -> str:
    """去除右侧空白字符

    Args:
        text: 输入字符串
        chars: 要去除的字符，默认为空白字符

    Returns:
        去除右侧字符后的字符串
    """
    return text.rstrip(chars)


def camel_to_snake(text: str) -> str:
    """驼峰转下划线

    Args:
        text: 驼峰格式字符串

    Returns:
        下划线格式字符串
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_to_camel(text: str, capitalize_first: bool = False) -> str:
    """下划线转驼峰

    Args:
        text: 下划线格式字符串
        capitalize_first: 是否首字母大写，默认为False

    Returns:
        驼峰格式字符串
    """
    components = text.split('_')
    if capitalize_first:
        return ''.join(x.title() for x in components)
    return components[0] + ''.join(x.title() for x in components[1:])


def mask(text: str, start: int = 0, end: int = 0, mask_char: str = "*") -> str:
    """字符串脱敏

    Args:
        text: 输入字符串
        start: 开始位置
        end: 结束位置（从末尾计算）
        mask_char: 脱敏字符，默认为"*"

    Returns:
        脱敏后的字符串

    Example:
        mask("13812345678", 3, 4) -> "138****5678"
    """
    if start < 0 or end < 0:
        raise ValueError("start和end必须为非负数")
    if start + end > len(text):
        return mask_char * len(text)

    masked_length = len(text) - start - end
    return text[:start] + mask_char * masked_length + text[len(text) - end:]


def format_size(size_bytes: int) -> str:
    """格式化文件大小

    Args:
        size_bytes: 字节数

    Returns:
        格式化后的文件大小字符串
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if abs(size_bytes) < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


def format_number(number: float, decimal_places: int = 2) -> str:
    """格式化数字（千分位）

    Args:
        number: 数字
        decimal_places: 小数位数，默认为2

    Returns:
        格式化后的数字字符串
    """
    return f"{number:,.{decimal_places}f}"


def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """格式化日期时间

    Args:
        dt: datetime对象
        fmt: 格式字符串，默认为"%Y-%m-%d %H:%M:%S"

    Returns:
        格式化后的日期时间字符串
    """
    return dt.strftime(fmt)
