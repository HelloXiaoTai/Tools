import random
import IPy

def ip_random(ip_first,ip_last,number):
    '''
    根据网段，随机生成指定个数的ip
    :param ip_first: 网段起始ip(如1.1.1.0)
    :param ip_last: 网段结束ip（1.1.2.0）
    :param number: 个数
    :return: 随机ip列表
    '''
    ip_first_int = IPy.IPint(ip_first).int()
    ip_last_int = IPy.IPint(ip_last).int()
    ip_list = list()
    while True:
        ip_random = random.randint(ip_first_int, ip_last_int)
        if IPy.IP(ip_random) not in ip_list:
            ip_list.append(IPy.IP(ip_random).strNormal())
            if len(ip_list) == number:
                break
    return ip_list

if __name__ == '__main__':
    ips=ip_random('12.1.1.1','12.1.2.1',5)
    print(ips) #['12.1.1.251', '12.1.1.44', '12.1.1.114', '12.1.1.128', '12.1.1.247']