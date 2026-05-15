"""MetaX - Python工具库

提供数学运算、字符串处理、日期时间、文件操作等常用功能
"""

from metax.base.math.basic import add, subtract, multiply, divide
from metax.base.math.advanced import (
    power, sqrt, cbrt, sin, cos, tan,
    log, log10, log2, abs, round, floor, ceil,
    factorial, gcd, lcm
)
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
from metax.util.datetime import (
    now, today, timestamp, timestamp_ms, from_timestamp,
    parse, format, add_days, add_hours, add_minutes,
    diff_days, diff_seconds, is_weekend, is_weekday,
    get_age, get_quarter, get_week_of_year, get_day_of_year
)
from metax.util.file import (
    read_text, write_text, read_lines, write_lines,
    read_json, write_json, exists, is_file, is_dir,
    get_size, get_extension, get_filename, get_basename,
    get_parent, join_path, create_dir,
    delete_file, delete_dir, copy_file, copy_dir,
    move, rename, list_files, list_dirs,
    get_md5, get_sha256
)

__version__ = "0.1.4"
__author__ = "ACANX"

__all__ = [
    # 问候
    'hello',
    # 基础数学运算
    'add', 'subtract', 'multiply', 'divide',
    # 高级数学运算
    'power', 'sqrt', 'cbrt', 'sin', 'cos', 'tan',
    'log', 'log10', 'log2', 'abs', 'round', 'floor', 'ceil',
    'factorial', 'gcd', 'lcm',
    # 字符串格式化
    'capitalize', 'title', 'upper', 'lower', 'swapcase', 'reverse',
    'truncate', 'strip', 'lstrip', 'rstrip',
    'camel_to_snake', 'snake_to_camel', 'mask',
    'format_size', 'format_number', 'format_datetime',
    # 字符串验证
    'is_empty', 'is_numeric', 'is_integer', 'is_alpha', 'is_alphanumeric',
    'is_email', 'is_phone_cn', 'is_id_card_cn', 'is_url', 'is_ip',
    'is_hex_color', 'is_date', 'is_chinese', 'contains_chinese',
    'length_between', 'matches',
    # 日期时间
    'now', 'today', 'timestamp', 'timestamp_ms', 'from_timestamp',
    'parse', 'format', 'add_days', 'add_hours', 'add_minutes',
    'diff_days', 'diff_seconds', 'is_weekend', 'is_weekday',
    'get_age', 'get_quarter', 'get_week_of_year', 'get_day_of_year',
    # 文件操作
    'read_text', 'write_text', 'read_lines', 'write_lines',
    'read_json', 'write_json', 'exists', 'is_file', 'is_dir',
    'get_size', 'get_extension', 'get_filename', 'get_basename',
    'get_parent', 'join_path', 'create_dir',
    'delete_file', 'delete_dir', 'copy_file', 'copy_dir',
    'move', 'rename', 'list_files', 'list_dirs',
    'get_md5', 'get_sha256'
]


def hello(name: str = "世界") -> str:
    """返回一个问候语

    Args:
        name: 要问候的名字，默认为"世界"

    Returns:
        问候语字符串
    """
    return f"你好, {name}!"