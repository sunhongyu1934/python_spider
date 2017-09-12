#!/usr/bin/env python
# --*-- coding:utf-8
import urllib
import time
import json
import cookielib
sgArr=[
    ["6","b","t","f","2","z","l","5","w","h","q","i","s","e","c","p","m","u","9","8","y","k","j","r","x","n","-","0","3","4","d","1","a","o","7","v","g"],
    ["1","8","o","s","z","u","n","v","m","b","9","f","d","7","h","c","p","y","2","0","3","j","-","i","l","k","t","q","4","6","r","a","w","5","e","x","g"],
    ["x","7","0","d","i","g","a","c","t","h","u","p","f","6","v","e","q","4","b","5","k","w","9","s","-","j","l","y","3","o","n","z","m","2","1","r","8"],
    ["s","6","h","0","p","g","3","n","m","y","l","d","x","e","a","k","z","u","f","4","r","b","-","7","o","c","i","8","v","2","1","9","q","w","t","j","5"],
    ["d","4","9","m","o","i","5","k","q","n","c","s","6","b","j","y","x","l","a","v","3","t","u","h","-","r","z","2","0","7","g","p","8","f","1","w","e"],
    ["z","j","3","l","1","u","s","4","5","g","c","h","7","o","t","2","k","a","-","e","x","y","b","n","8","i","6","q","p","0","d","r","v","m","w","f","9"],
    ["j","h","p","x","3","d","6","5","8","k","t","l","z","b","4","n","r","v","y","m","g","a","0","1","c","9","-","2","7","q","e","w","u","s","f","o","i"],
    ["8","q","-","u","d","k","7","t","z","4","x","f","v","w","p","2","e","9","o","m","5","g","1","j","i","n","6","3","r","l","b","h","y","c","a","s","0"],
    ["7","-","g","x","6","5","n","u","q","z","w","t","m","0","h","o","y","p","i","f","k","s","9","l","r","1","2","v","4","e","8","c","b","a","d","j","3"],
    ["1","t","8","z","o","f","l","5","2","y","q","9","p","g","r","x","e","s","d","4","n","b","u","a","m","c","h","j","3","v","i","0","-","w","7","k","6"]]

tid = '7000445'
time_str = int(time.time() * 1000)

url = 'http://dis.tianyancha.com/qq/' + tid + '.json?random=' + str(time_str)
url_qygx = 'http://dis.tianyancha.com/dis/getInfoById/' + tid + '.json?'
CK = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CK))



opener.addheaders=[('Host','dis.tianyancha.com'),
                   ('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'),
                   ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                   ('Connection','keep-alive')]


r=opener.open("http://www.tianyancha.com/company/29725665")
reqData=opener.open(url)
response = reqData.read()

#message = '{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"name":"29725665","uv":197350,"pv":618608,"v":"33,102,117,110,99,116,105,111,110,40,110,41,123,100,111,99,117,109,101,110,116,46,99,111,111,107,105,101,61,39,114,116,111,107,101,110,61,56,97,51,50,51,49,97,51,53,50,97,98,52,102,49,51,97,100,99,52,98,50,53,48,99,100,98,55,48,54,100,101,59,112,97,116,104,61,47,59,39,59,110,46,119,116,102,61,102,117,110,99,116,105,111,110,40,41,123,114,101,116,117,114,110,39,51,49,44,49,57,44,52,44,49,52,44,51,48,44,49,51,44,55,44,49,56,44,50,56,44,50,55,44,51,44,51,49,44,50,57,44,51,50,44,49,57,44,49,57,44,49,57,44,51,49,44,49,57,44,50,57,44,50,56,44,49,51,44,51,44,50,56,44,49,44,51,52,44,52,44,51,48,44,55,44,51,50,44,49,56,44,55,39,125,125,40,119,105,110,100,111,119,41,59"}}'

message = json.loads(response)

message_cookie = ''
for x in message['data']['v'].split(','):
    message_cookie += chr(int(x))

r_token = message_cookie.split('\'')[1].split(';')[0].split('=')[1]
utm_arr = message_cookie.split('\'')[3].split(',')
index = 0

# if len(str(ord(tid[0]))) > 1:
#     index = str(ord(tid[0]))[1]
# else:
#     index = str(ord(tid[0]))

company2index={
    "1":9,
    "2":0,
    "3":1,
    "4":3,
    "5":2,
    "6":5,
    "7":6,
    "8":7,
    "9":4
}

index=company2index[str(tid[0])]

tidArr = sgArr[int(index)]

r_utm = ''
for x in utm_arr:
    r_utm += tidArr[int(x)]


def make_cookie(name, value):
    return cookielib.Cookie(
        version=0,
        name=name,
        value=value,
        port=None,
        port_specified=False,
        domain="dis.tianyancha.com",
        domain_specified=True,
        domain_initial_dot=False,
        path="/",
        path_specified=True,
        secure=False,
        expires=None,
        discard=False,
        comment=None,
        comment_url=None,
        rest=None
    )

opener.addheaders=[ ('Host','dis.tianyancha.com'),
                   ('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'),
                   ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                   ('Connection','keep-alive'),('Referer','http://dis.tianyancha.com/dis/old')]
CK.set_cookie(make_cookie("_rutm",r_utm))
CK.set_cookie(make_cookie("rtoken",r_token))
reqData_qygx = opener.open(url_qygx)
response_qygx = reqData_qygx.read()
print (response_qygx)


