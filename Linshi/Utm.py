from __future__ import print_function, unicode_literals

from urllib.parse import quote

import requests
import time
import re




proxyHost = "proxy.abuyun.com"
proxyPort = "9020"
# 代理隧道验证信息
proxyUser = "H4XGPM790E93518"
proxyPass = "2835A47D56143D6"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}


session = requests.session()
session.cookies.set("tnet", "36.110.41.42")

index_url = "http://www.tianyancha.com/search?key=%E5%B0%8F%E7%B1%B3&checkFrom=searchBox"
tongji_url = "http://dis.tianyancha.com/qq/150041670.json?random=%s" % (int(time.time()) * 1000)
api_url = "http://dis.tianyancha.com/dis/getInfoById/150041670.json?"

tongji_url2="http://www.tianyancha.com/tongji/23402373.json?random=%s"% (int(time.time()) * 1000)
api_url2="http://www.tianyancha.com/v2/company/23402373.json"
na=quote("百度")

tongji_url3=r"http://www.tianyancha.com/tongji/%s.json?random=%s"% (na,int(time.time()) * 1000)
api_url3="http://www.tianyancha.com/v2/search/%s.json?"%na

public_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
        }

api_headers = public_headers.copy()
api_headers.update({
        "Tyc-From": "normal",
        "Accept": "application/json, text/plain, */*",
        "CheckError": "check",
    })


# 访问首页
#index_page = session.request("GET", index_url, headers = public_headers)



#js_page = session.request("GET", "http://static.tianyancha.com/wap/resources/scripts/app-7476398ced.js", headers = public_headers)
sgattrs = sgArr=[
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

# 取得token和fxckStr
tongji_page = session.request("GET", tongji_url2, headers = api_headers,proxies=proxies)
print(tongji_page.content.decode("utf-8"))
js_code = "".join([ chr(int(code)) for code in tongji_page.json()["data"]["v"].split(",") ])
token = re.findall(r"token=(\w+);", js_code)[0]
print("token:", token)

fxck_chars = re.findall(r"\'([\d\,]+)\'", js_code)[0].split(",")
sogou = sgattrs[0] # window.$SoGou$ = window._sgArr[9]

utm = "".join([sogou[int(fxck)] for fxck in fxck_chars])    # if(window.wtf){var fxck = window.wtf().split(",");var fxckStr = "";for(var i=0;i<fxck.length;i++){fxckStr+=window.$SoGou$[fxck[i]];}document.cookie = "_utm="+fxckStr+";path=/;";window.wtf = null;}
print("utm:", utm)

session.cookies.set("token", token)
session.cookies.set("_utm", utm)

#r = session.request("GET", "http://www.tianyancha.com/IcpList/150041670.json",
#        headers = api_headers)
#print(r.content.decode("utf-8"))

api_page = session.request("GET", api_url2, headers = api_headers,proxies=proxies)
print(api_page.content.decode("utf-8"))


