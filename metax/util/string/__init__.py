"""字符串处理模块"""

from metax.util.string.format import (
    capitalize, title, upper, lower, swapcase, reverse,
    truncate, strip, lstrip, rstrip,
    camel_to_snake, snake_to_camel, mask,
    format_size, format_number, format_datetime
)
from metax.util.string.validate import (
    is_empty, is_numeric, is_integer, is_alpha, is_alphanumeric,
    is_email, is_phone_cn, is_id_card_cn, is_url, is_ip,
    is_hex_color, is_date, is_chinese, contains_chinese,
    length_between, matches
)

__all__ = [
    # 格式化
    'capitalize', 'title', 'upper', 'lower', 'swapcase', 'reverse',
    'truncate', 'strip', 'lstrip', 'rstrip',
    'camel_to_snake', 'snake_to_camel', 'mask',
    'format_size', 'format_number', 'format_datetime',
    # 验证
    'is_empty', 'is_numeric', 'is_integer', 'is_alpha', 'is_alphanumeric',
    'is_email', 'is_phone_cn', 'is_id_card_cn', 'is_url', 'is_ip',
    'is_hex_color', 'is_date', 'is_chinese', 'contains_chinese',
    'length_between', 'matches'
]