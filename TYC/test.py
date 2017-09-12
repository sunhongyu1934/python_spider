import json

import requests
from lxml import etree


def test():
    heads={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
        "Content-Type":"application/json"
    }
    data={
        "autoLogin":"true",
        "cdpassword":"349617b80072ce2b45926f82f0b2d492",
        "loginway":"PL",
        "mobile":"13717951934"
    }
    r=requests.post("http://www.tianyancha.com/cd/login.json",data=json.dumps(data),headers=heads)
    print(r.headers)




if __name__ == '__main__':
    test()