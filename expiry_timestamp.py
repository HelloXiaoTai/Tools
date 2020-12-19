import datetime

from common_util.date_time_util import date_str_to_timestamp

def get_expiry_timestamp(expiry_date):
    '''将过期时间转换为时间戳,注：expiry_date不能为None'''
    if 'T' in expiry_date and 'Z' in expiry_date:
        #将如下时间格式（长度为20、22、24）修改为“2016-11-03 07:59:59”
            #2016-11-02T18:34:56.941Z,2016-10-29T06:34:08Z,2018-11-02T23:59:59.0Z
        utc_format = "%Y-%m-%dT%H:%M:%S.%fZ"
        try:
            utc_time = datetime.datetime.strptime(expiry_date, utc_format)
        except ValueError:
            utc_format = '%Y-%m-%dT%H:%M:%SZ'
            utc_time = datetime.datetime.strptime(expiry_date, utc_format)
        local_date = utc_time + datetime.timedelta(hours=8)  # 将UTC装换成北京时间时，需要加上8小时
        date_str_standard = str(local_date).split('.')[0]  # 去掉秒后面的小数点
        expiry_timestamp=date_str_to_timestamp(date_str_standard,'%Y-%m-%d %H:%M:%S')
    elif 'UTC' in expiry_date:
        temp_list=list()
        #02-Nov-2016 18:44:16 UTC
        temp_list.append(date_str_to_timestamp(expiry_date, '%d-%b-%Y %H:%M:%S UTC'))
        #2017-06-05 00:00:00 UTC
        temp_list.append(date_str_to_timestamp(expiry_date, '%Y-%m-%d %H:%M:%S UTC'))
        # 02-Dec-2013 13:44:33 UTC
        temp_list.append(date_str_to_timestamp(expiry_date, '%d-%b-%Y %H:%M:%S UTC'))
        for expiry_timestamp in temp_list:
            if expiry_timestamp is not None:
                return expiry_timestamp
        expiry_timestamp=None
    elif 'GMT' in expiry_date:
        #Tue Nov 01 23:59:59 GMT 2016
        expiry_timestamp=date_str_to_timestamp(expiry_date,'%a %b %d %H:%M:%S GMT %Y')
    else:
        temp_list=list()
        # 02-nov-2016
        temp_list.append(date_str_to_timestamp(expiry_date, '%d-%b-%Y'))
        # 1-Jan-16
        temp_list.append(date_str_to_timestamp(expiry_date, '%d-%b-%y'))
        #2016-11-29
        temp_list.append(date_str_to_timestamp(expiry_date, '%Y-%m-%d'))
        #21/02/2017
        temp_list.append(date_str_to_timestamp(expiry_date,'%d/%m/%Y'))
        #2014-03-22T00:00:00-0400
        #2014-03-19T00:00:00+08:00

        for expiry_timestamp in temp_list:
            if expiry_timestamp is not None:
                return expiry_timestamp

        expiry_timestamp=None

    return expiry_timestamp