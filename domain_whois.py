import socket

def get_domain_reginfo(whois_server,domain):
    '''
    通过whois服务器的43端口，获取域名注册信息
    :param whois_server: whois服务器（如：whois.cnnic.cn）
    :param domain: 域名（如bdo.com.cn）
    :return: 域名注册信息（如下）
        Domain Name: bdo.com.cn
        ROID: 20100403s10011s07940755-cn
        Domain Status: clientDeleteProhibited
        Registrant: 立信会计师事务所（特殊普通合伙）
        Registrant Contact Email: admin@bdo.com.cn
        Sponsoring Registrar: 北京新网数码信息技术有限公司
        Name Server: ns1.bdo.com.cn
        Name Server: ns2.bdo.com.cn
        Name Server: ns3.bdo.com.cn
        Name Server: ns4.bdo.com.cn
        Registration Time: 2010-04-03 04:29:20
        Expiration Time: 2022-04-03 04:29:20
        DNSSEC: unsigned
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((whois_server, 43))
    s.send(f'{domain}   \r\n'.encode())
    result = bytearray()
    while True:
        data = s.recv(10000)
        if not len(data):
            break
        result.extend(data)
    s.close()
    reginfo=bytes(result).decode('utf-8')
    return reginfo

