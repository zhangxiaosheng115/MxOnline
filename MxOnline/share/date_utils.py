# -*- coding: utf-8 -*-
"""
单独放出来是为了防止和任何包导入冲突
"""

DEFAULT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE_YMD_FORMAT = '%Y%m%d'

DEFAULT_TIME_MINUTE_FORMAT = '%Y-%m-%d %H:%M'


def get_cur_time():
    import datetime
    return datetime.datetime.now()


def get_cur_date():
    import datetime
    return datetime.date.today()


def get_cur_timestamp():
    import time
    return int(time.time())


def to_timestamp(date):
    """
    把日期转换为时间戳
    :param date: date 和 datetime 类型都支持
    :return:
    """
    import time
    return int(time.mktime(date.timetuple()))


def to_date(timestamp):
    """
    时间戳转换为日期
    :param timestamp:
    :return:
    """
    import datetime
    return datetime.date.fromtimestamp(timestamp)


def to_datetime(timestamp):
    """
    时间戳转换为日期
    :param timestamp:
    :return:
    """
    import datetime
    return datetime.datetime.fromtimestamp(timestamp)


def timestamp_to_datetime_str(timestamp, fmt=DEFAULT_TIME_FORMAT):
    """
    时间戳转换为日期字符串
    :param timestamp:
    :param fmt:
    :return:
    """
    import datetime
    date_time = datetime.datetime.fromtimestamp(timestamp)
    return date_time.strftime(fmt)


def left_days(date):
    """
    剩余天数
    :param date:
    :return:
    """
    import datetime
    return (date - datetime.date.today()).days


def to_str_time(date_time, fmt=DEFAULT_TIME_FORMAT):
    """
    日期对象转换为字符串
    :param date_time:
    :param fmt:
    :return:
    """
    return date_time.strftime(fmt)


def from_str_time(date_string, fmt=DEFAULT_TIME_FORMAT):
    """
    字符串转换为日期对象
    :param date_string:
    :param fmt:
    :return:
    """
    import datetime
    return datetime.datetime.strptime(date_string, fmt)


def day_delta(days):
    import datetime
    return datetime.timedelta(days)


def to_str_date(date_time, fmt=DEFAULT_DATE_FORMAT):
    """
    日期对象转换为字符串y-m-d
    :param date_time:
    :param fmt:
    :return:
    """
    return date_time.strftime(fmt)


def from_str_date(date_string, fmt=DEFAULT_DATE_FORMAT):
    """
    字符串转换为日期对象
    :param date_string:
    :param fmt:
    :return:
    """
    import datetime
    return datetime.datetime.strptime(date_string, fmt)


def seconds_to_minutes(seconds):
    """
    秒转换为分钟
    :param seconds:
    :return:
    """
    return seconds / 60


def days_to_seconds(days):
    """
    天数转换为秒
    :param days:
    :return:
    """
    return days * 60 * 60 * 24


def until_midnight_timestamp(days=1):
    """
    现在时间到几天后午夜零点的时间戳
    :return:
    """
    return to_timestamp(get_cur_date() + day_delta(days=days))


def before_midnight_timestamp(days=1):
    """
    距离当前时间前的n天午夜零点的时间戳
    :return:
    """
    return to_timestamp(get_cur_date() - day_delta(days=days))


def date_to_datetime(date):
    """
    date转换成datetime
    :param date:
    :return:
    """
    import datetime
    return datetime.datetime(date.year, date.month, date.day)


def some_minutes_later(d, minutes, fmt=DEFAULT_TIME_FORMAT):
    """
    minutes分钟后, 字符串
    :param d:
    :param minutes:
    :param fmt:
    :return:
    """
    import datetime
    return datetime.datetime.strftime(d + datetime.timedelta(minutes=minutes), fmt)


def str_to_timestamp(date_string, fmt=DEFAULT_TIME_MINUTE_FORMAT):
    """
    字符串转换成时间戳
    :param date_string:
    :param fmt:
    :return:
    """
    import time
    import datetime
    date = datetime.datetime.strptime(date_string, fmt)
    return int(time.mktime(date.timetuple()))


def get_cur_datetime_str(fmt=DEFAULT_TIME_FORMAT):
    """
    获得当前时间的字符串时间
    :return:
    """
    return to_str_date(get_cur_time(), fmt)


def get_today_timestamp():
    import datetime
    import time

    today = datetime.date.today()
    return int(time.mktime(today.timetuple()))
