"""日期时间工具"""

from datetime import datetime, timedelta, date
from typing import Optional, Union


def now(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """获取当前时间

    Args:
        fmt: 格式字符串，默认为"%Y-%m-%d %H:%M:%S"

    Returns:
        格式化后的当前时间字符串
    """
    return datetime.now().strftime(fmt)


def today(fmt: str = "%Y-%m-%d") -> str:
    """获取今天日期

    Args:
        fmt: 格式字符串，默认为"%Y-%m-%d"

    Returns:
        格式化后的今天日期字符串
    """
    return date.today().strftime(fmt)


def timestamp() -> int:
    """获取当前时间戳（秒）

    Returns:
        当前时间戳
    """
    return int(datetime.now().timestamp())


def timestamp_ms() -> int:
    """获取当前时间戳（毫秒）

    Returns:
        当前时间戳（毫秒）
    """
    return int(datetime.now().timestamp() * 1000)


def from_timestamp(ts: int, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """时间戳转日期时间字符串

    Args:
        ts: 时间戳（秒）
        fmt: 格式字符串，默认为"%Y-%m-%d %H:%M:%S"

    Returns:
        格式化后的日期时间字符串
    """
    return datetime.fromtimestamp(ts).strftime(fmt)


def parse(text: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """解析日期时间字符串

    Args:
        text: 日期时间字符串
        fmt: 格式字符串，默认为"%Y-%m-%d %H:%M:%S"

    Returns:
        datetime对象

    Raises:
        ValueError: 解析失败时抛出
    """
    return datetime.strptime(text, fmt)


def format(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """格式化datetime对象

    Args:
        dt: datetime对象
        fmt: 格式字符串，默认为"%Y-%m-%d %H:%M:%S"

    Returns:
        格式化后的字符串
    """
    return dt.strftime(fmt)


def add_days(dt: Union[datetime, date], days: int) -> Union[datetime, date]:
    """增加天数

    Args:
        dt: datetime或date对象
        days: 天数（可为负数）

    Returns:
        增加天数后的datetime或date对象
    """
    return dt + timedelta(days=days)


def add_hours(dt: datetime, hours: int) -> datetime:
    """增加小时

    Args:
        dt: datetime对象
        hours: 小时数（可为负数）

    Returns:
        增加小时后的datetime对象
    """
    return dt + timedelta(hours=hours)


def add_minutes(dt: datetime, minutes: int) -> datetime:
    """增加分钟

    Args:
        dt: datetime对象
        minutes: 分钟数（可为负数）

    Returns:
        增加分钟后的datetime对象
    """
    return dt + timedelta(minutes=minutes)


def diff_days(start: Union[datetime, date], end: Union[datetime, date]) -> int:
    """计算两个日期之间的天数差

    Args:
        start: 开始日期
        end: 结束日期

    Returns:
        天数差
    """
    return (end - start).days


def diff_seconds(start: datetime, end: datetime) -> int:
    """计算两个时间之间的秒数差

    Args:
        start: 开始时间
        end: 结束时间

    Returns:
        秒数差
    """
    return int((end - start).total_seconds())


def is_weekend(dt: Union[datetime, date]) -> bool:
    """判断是否为周末

    Args:
        dt: datetime或date对象

    Returns:
        是否为周末
    """
    return dt.weekday() >= 5


def is_weekday(dt: Union[datetime, date]) -> bool:
    """判断是否为工作日

    Args:
        dt: datetime或date对象

    Returns:
        是否为工作日
    """
    return dt.weekday() < 5


def get_age(birth_date: date) -> int:
    """计算年龄

    Args:
        birth_date: 出生日期

    Returns:
        年龄
    """
    today_date = date.today()
    age = today_date.year - birth_date.year
    if (today_date.month, today_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def get_quarter(dt: Union[datetime, date]) -> int:
    """获取季度

    Args:
        dt: datetime或date对象

    Returns:
        季度（1-4）
    """
    return (dt.month - 1) // 3 + 1


def get_week_of_year(dt: Union[datetime, date]) -> int:
    """获取年中第几周

    Args:
        dt: datetime或date对象

    Returns:
        年中第几周
    """
    return dt.isocalendar()[1]


def get_day_of_year(dt: Union[datetime, date]) -> int:
    """获取年中第几天

    Args:
        dt: datetime或date对象

    Returns:
        年中第几天
    """
    return dt.timetuple().tm_yday
