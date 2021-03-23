import datetime
import time


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

    :param date_str:  例如：2020-12-20 20:50:00
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

def get_timestamp(date_str):
    '''将时间字符串转换为时间戳'''
    if 'T' in date_str and 'Z' in date_str:
        #将如下时间格式（长度为20、22、24）修改为“2016-11-03 07:59:59”
            #2016-11-02T18:34:56.941Z,2016-10-29T06:34:08Z,2018-11-02T23:59:59.0Z
        utc_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        try:
            utc_time = datetime.datetime.strptime(date_str, utc_format)
        except ValueError:
            utc_format = '%Y-%m-%dT%H:%M:%SZ'
            utc_time = datetime.datetime.strptime(date_str, utc_format)
        local_date = utc_time + datetime.timedelta(hours=8)  # 将UTC装换成北京时间时，需要加上8小时
        date_str_standard = str(local_date).split('.')[0]  # 去掉秒后面的小数点
        timestamp=date_str_to_timestamp(date_str_standard,'%Y-%m-%d %H:%M:%S')
    elif 'UTC' in date_str:
        temp_list=list()
        #02-Nov-2016 18:44:16 UTC
        temp_list.append(date_str_to_timestamp(date_str, '%d-%b-%Y %H:%M:%S UTC'))
        #2017-06-05 00:00:00 UTC
        temp_list.append(date_str_to_timestamp(date_str, '%Y-%m-%d %H:%M:%S UTC'))
        # 02-Dec-2013 13:44:33 UTC
        temp_list.append(date_str_to_timestamp(date_str, '%d-%b-%Y %H:%M:%S UTC'))
        for timestamp in temp_list:
            if timestamp is not None:
                return timestamp
        timestamp=None
    elif 'GMT' in date_str:
        #Tue Nov 01 23:59:59 GMT 2016
        timestamp=date_str_to_timestamp(date_str,'%a %b %d %H:%M:%S GMT %Y')
    else:
        temp_list=list()
        # 02-nov-2016
        temp_list.append(date_str_to_timestamp(date_str, '%d-%b-%Y'))
        # 1-Jan-16
        temp_list.append(date_str_to_timestamp(date_str, '%d-%b-%y'))
        #2016-11-29
        temp_list.append(date_str_to_timestamp(date_str, '%Y-%m-%d'))
        #21/02/2017
        temp_list.append(date_str_to_timestamp(date_str,'%d/%m/%Y'))
        #2014-03-22T00:00:00-0400
        #2014-03-19T00:00:00+08:00

        for timestamp in temp_list:
            if timestamp is not None:
                return timestamp

        timestamp=None

    return timestamp