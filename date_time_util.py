# -*- coding: utf-8 -*-
import re
import time


def get_now_timestamp():
    """
    十三位时间戳获取
    :return:
    """
    return int(round(time.time() * 1000))


def get_normal_date_format():
    """
    获取常规时间格式
    :return:
    """
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def get_date_format_day(timestamp):
    """
    获取时间格式化，按照天
    :return:
    """
    return time.strftime('%Y%m%d', time.localtime(timestamp))


def get_date_format_month(timestamp):
    """
    获取时间格式化，按照月
    :return:
    """
    return time.strftime('%Y%m', time.localtime(timestamp))


def get_date_format_day(timestamp):
    """
    获取时间格式化，按照月
    :return:
    """
    return time.strftime('%Y%m%d', time.localtime(timestamp))


def date_str_to_timestamp(date_str=None, date_format=None):
    """
    时间格式字符串转换成时间戳

    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12） 
    %M 分钟数（00=59）
    %S 秒（00-59）

    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身 

    :param date_str:  例如：2018-10-25 20:13:15
    :param date_format:  例如： %Y-%m-%d %H:%M:%S
    :return:
    """
    if date_str is not None and date_format is not None:
        try:
            return int(round(time.mktime(time.strptime(date_str, date_format)) * 1000))
        except ValueError:
            return None
    else:
        return None


week_en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week_simple = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
week_zh = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日', '星期天']
month_zh = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
month_en = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_simple = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
am_pm_zh = ['上午', '下午']
am_pm_en = ['AM', 'PM']


def chinese_format_replace(date_str):
    """
    中文时间格式替换成英文
    :param date_str:
    :return:
    """
    if date_str.find('星期') > -1:
        index = date_str.index('星期')
        week = date_str[index:index+3]
        date_str = date_str.replace(week, week_en[week_zh.index(week)], 1)
    if date_str.find('月') > -1:
        index = date_str.index('月')
        if '十' == date_str[index-2:index-1]:
            month = date_str[index-2:index+1]
        else:
            month = date_str[index-1:index + 1]
        date_str = str(date_str).replace(month, month_en[month_zh.index(month)], 1)
    if date_str.find('上午') > -1:
        date_str = date_str.replace('上午', 'AM', 1)
    if date_str.find('下午') > -1:
        date_str = date_str.replace('下午', 'PM', 1)
    return date_str


if __name__ == '__main__':
    print(date_str_to_timestamp('2018-12-24 17:13:56 (CST)'.strip(), '%Y-%m-%d %H:%M:%S (CST)'))
    print(date_str_to_timestamp('2020-12-9', '%Y-%m-%d'))
    print(date_str_to_timestamp('27-jun-2014', '%d-%b-%Y'))
    print(date_str_to_timestamp('Tue Nov 01 23:59:59 GMT 2016', '%a %b %d %H:%M:%S GMT %Y'))
    print(get_now_timestamp())  #1735637717000
    print(date_str_to_timestamp('02-Dec-2013 13:44:33 UTC', '%d-%b-%Y %H:%M:%S UTC'))
