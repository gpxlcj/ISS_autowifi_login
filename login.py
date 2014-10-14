#! -*- coding:utf8 -*-

import urllib2
import urllib

def login():
    '''
    登陆wifi
    '''
    temp_url = "http://www.baidu.com"
    pre_request = urllib2.urlopen(temp_url)
    url = pre_request.geturl()
    temp_part_list = url.split('?')
    try:
        else_data = temp_part_list[1]
        url = \
        "http://192.168.95.100:8080/RadiusWeb/portalweb/wlanmodel/do.portallogin"
        username = "2012302660044"
        password = "660044"
        data = \
        'username='+username+'&password='+password+'&'+else_data
        request = urllib2.Request(url)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, data)
        print response.read()
    except:
        print 'have login'

def register():
    '''
    注册账号
    '''
    url = "http://192.168.95.100:8080/RadiusWeb/portal/do.portalregister?wlanuserip=20.0.185.184&wlanacname=CISS-AC&wlanacip=172.31.12.1&NASID=123&apmac=00:1F:64:EE:75:D2&usermac=84:4B:F5:DB:76:EB&ssid=ISS-WEBi"
    else_data  = url.split('?')[1]
    data ='username='+'233'+'&password='+'1'+'&'+else_data
    req = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    ans = opener.open(req, data)
    print ans.read()
    print else_data


if __name__=='__main__':
    login()
#    register()
