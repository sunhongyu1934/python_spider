
# coding:utf-8


from __future__ import print_function
import json
from multiprocessing.pool import Pool
from urllib.parse import quote
import sys
import pymysql
import requests
import time
import re

from multiprocessing import Manager


# 代理服务器
from multiprocessing import Queue

proxyHost = "proxy.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H4XGPM790E93518D"
proxyPass = "2835A47D56143D62"

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

mysql = pymysql.connect(
    host='10.44.60.141',
    user='spider',
    password='spider',
    port='3308',
    db='spider',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    use_unicode=True
)


def get(key, value):
    try:
        return key[value]
    except Exception as e:
        return ''


class Base_Api(object):
    def __init__(self, type='company', id=None, keys=None):
        self.type = type
        self.id = id
        self.keys = keys

        self.session = requests.session()
        # self.session.cookies.set("tnet", "36.110.41.42")


        self.api_headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
        }
        if self.type == 'company':
            # 公司
            self.tongji_url = "http://www.tianyancha.com/tongji/%s.json?random=%s" % (self.id, int(time.time()) * 1000)
            self.api_url = "http://www.tianyancha.com/v2/company/%s.json" % self.id
            self.api_headers.update({
                "Tyc-From": "normal",
                'Host': 'www.tianyancha.com',
                "Referer": "http://www.tianyancha.com/company/%s" % self.id,
            })
        elif self.type == 'search':
            # 搜索
            self.tongji_url = 'http://www.tianyancha.com/tongji/%s.json?random=%s' % (
            quote(self.keys), int(time.time()) * 1000)
            self.api_url = 'http://www.tianyancha.com/v2/search/%s.json?' % quote(self.keys)
            self.api_headers.update({
                "Tyc-From": "normal",
                'Host': 'www.tianyancha.com',
                "Referer": 'http://www.tianyancha.com/search?key=%s&checkFrom=searchBox' % quote(self.keys),
                # "X-AUTH-TOKEN": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzc4NDg1NTQ1NyIsImlhdCI6MTQ5ODUzNTkyNiwiZXhwIjoxNTE0MDg3OTI2fQ.QNesTsmbVo8yZGChzHelTsvIJEnoryS8TRhZONHtmhOdIaHHuX_RWJxlpqg6OvT4-f43LnhXMJ5DW40rdqIFuA",
            })
        elif self.type == 'relation':
            # 关系图
            self.tongji_url = "http://dis.tianyancha.com/qq/%s.json?random=%s" % (self.id, int(time.time()) * 1000)
            self.api_url = "http://dis.tianyancha.com/dis/getInfoById/%s.json?" % self.id
            self.api_headers.update({
                'Host': 'dis.tianyancha.com',
                'Referer': 'http://dis.tianyancha.com/dis/old'
            })
        self.sgattrs = [
            ["6", "b", "t", "f", "2", "z", "l", "5", "w", "h", "q", "i", "s", "e", "c", "p", "m", "u", "9", "8", "y",
             "k", "j", "r", "x", "n", "-", "0", "3", "4", "d", "1", "a", "o", "7", "v", "g"],
            ["1", "8", "o", "s", "z", "u", "n", "v", "m", "b", "9", "f", "d", "7", "h", "c", "p", "y", "2", "0", "3",
             "j", "-", "i", "l", "k", "t", "q", "4", "6", "r", "a", "w", "5", "e", "x", "g"],
            ["s", "6", "h", "0", "p", "g", "3", "n", "m", "y", "l", "d", "x", "e", "a", "k", "z", "u", "f", "4", "r",
             "b", "-", "7", "o", "c", "i", "8", "v", "2", "1", "9", "q", "w", "t", "j", "5"],
            ["x", "7", "0", "d", "i", "g", "a", "c", "t", "h", "u", "p", "f", "6", "v", "e", "q", "4", "b", "5", "k",
             "w", "9", "s", "-", "j", "l", "y", "3", "o", "n", "z", "m", "2", "1", "r", "8"],
            ["z", "j", "3", "l", "1", "u", "s", "4", "5", "g", "c", "h", "7", "o", "t", "2", "k", "a", "-", "e", "x",
             "y", "b", "n", "8", "i", "6", "q", "p", "0", "d", "r", "v", "m", "w", "f", "9"],
            ["j", "h", "p", "x", "3", "d", "6", "5", "8", "k", "t", "l", "z", "b", "4", "n", "r", "v", "y", "m", "g",
             "a", "0", "1", "c", "9", "-", "2", "7", "q", "e", "w", "u", "s", "f", "o", "i"],
            ["8", "q", "-", "u", "d", "k", "7", "t", "z", "4", "x", "f", "v", "w", "p", "2", "e", "9", "o", "m", "5",
             "g", "1", "j", "i", "n", "6", "3", "r", "l", "b", "h", "y", "c", "a", "s", "0"],
            ["d", "4", "9", "m", "o", "i", "5", "k", "q", "n", "c", "s", "6", "b", "j", "y", "x", "l", "a", "v", "3",
             "t", "u", "h", "-", "r", "z", "2", "0", "7", "g", "p", "8", "f", "1", "w", "e"],
            ["7", "-", "g", "x", "6", "5", "n", "u", "q", "z", "w", "t", "m", "0", "h", "o", "y", "p", "i", "f", "k",
             "s", "9", "l", "r", "1", "2", "v", "4", "e", "8", "c", "b", "a", "d", "j", "3"],
            ["1", "t", "8", "z", "o", "f", "l", "5", "2", "y", "q", "9", "p", "g", "r", "x", "e", "s", "d", "4", "n",
             "b", "u", "a", "m", "c", "h", "j", "3", "v", "i", "0", "-", "w", "7", "k", "6"]]

    def get_api(self):
        while True:
            try:
                # 取得token和fxckStr
                while True:
                    try:
                        tongji_page = self.session.request("GET", self.tongji_url, headers=self.api_headers, proxies=proxies,timeout=3)
                        if tongji_page.content.decode("utf-8") and 'forbidden3' not in tongji_page.content.decode("utf-8"):
                            break
                    except Exception as ee:
                        print('time out reget')
                js_code = "".join([chr(int(str(code))) for code in str(json.loads(tongji_page.content.decode("utf-8"))["data"]["v"]).split(",")])
                token = re.findall(r"token=(\w+);", js_code)[0]
                # print("token:", token)

                fxck_chars = re.findall(r"\'([\d\,]+)\'", js_code)[0].split(",")
                parm = self.keys if self.type == 'search' else str(self.id)
                index = int(str(ord(parm[0]))[1])
                sogou = self.sgattrs[index]
                utm = "".join([sogou[int(fxck)] for fxck in fxck_chars])
                # print("utm:", utm)

                if self.type == 'relation':
                    self.session.cookies.set("rtoken", token)
                    self.session.cookies.set("_rutm", utm)
                else:
                    self.session.cookies.set("token", token)
                    self.session.cookies.set("_utm", utm)
                api_page = self.session.request("GET", self.api_url, headers=self.api_headers, proxies=proxies,timeout=3)
                if api_page.content.decode("utf-8") and 'forbidden3' not in tongji_page.content.decode("utf-8"):
                    break
            except Exception as e:
                print('error    ')
        return str(api_page.content.decode("utf-8"))


def data(q):
    with mysql.cursor() as cursor:
        sql1 = "select `Name` from qichacha_search where Province='GD' and `Name` not in (select quan_cheng from tyc_jichu_gd) limit %s,100000"% str(sys.argv[1]);
        cursor.execute(sql1)
        result = cursor.fetchall()
        for re in result:
            na = get(re, 'Name')
            q.put(na)


def getdetail(q):
    with mysql.cursor() as cursor:
        sql2 = "insert into tyc_jichu_gd(quan_cheng,ceng_yongming,logo,p_hone,e_mail,a_ddress,w_eb,fa_ren,zhuce_ziben,zhuce_shijian,jingying_zhuangtai,gongshang_hao,zuzhijigou_daima,tongyi_xinyong,qiye_leixing,hang_ye,yingye_nianxian,dengji_jiguan,zhuce_dizhi,jingying_fanwei,t_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        a=0;
        while True:
            if not q.empty():
                try:
                    print("begin get")
                    na = q.get(True)
                    api = Base_Api(type='search', keys=str(na))
                    # print(api.get_api(),na)
                    print("begin serach")
                    ser = json.loads(str(api.get_api()))
                    print("serach success")
                    if 'data' in ser:
                        for data in ser['data']:
                            tid = get(data, 'id')
                            api_de = Base_Api(type='company', id=tid)
                            print("begin detail")
                            resu = api_de.get_api()
                            print("detail success")
                            detail = json.loads(resu)
                            if 'data' in detail:
                                jiben = detail['data']
                                quan = get(jiben, 'name')
                                ceng = get(jiben, 'historyNames')
                                logo = get(jiben, 'logo')
                                phone = get(jiben, 'phoneNumber')
                                email = get(jiben, 'email')
                                address = get(jiben, 'regLocation')
                                web = get(jiben, 'websiteList')
                                faren = get(jiben, 'legalPersonName')
                                zhuceziben = get(jiben, 'regCapital')
                                if get(jiben, 'estiblishTime'):
                                    zhuceshijian = time.strftime('%Y-%m-%d',
                                                                 time.localtime(int(get(jiben, 'estiblishTime')) / 1000))
                                else:
                                    zhuceshijian=''
                                jingyingzhuangtai = get(jiben, 'regStatus')
                                gongshang = get(jiben, 'regNumber')
                                zuzhijigou = get(jiben, 'orgNumber')
                                tongyixinyong = get(jiben, 'creditCode')
                                qiyeleixing = get(jiben, 'companyOrgType')
                                hangye = get(jiben, 'industry')
                                if get(jiben, 'fromTime') and get(jiben, 'toTime'):
                                    yingyenianx = time.strftime('%Y-%m-%d', time.localtime(
                                        int(get(jiben, 'fromTime')) / 1000)) +"至"+ time.strftime('%Y-%m-%d', time.localtime(
                                        int(get(jiben, 'toTime')) / 1000))
                                elif get(jiben, 'fromTime')=='' and get(jiben, 'toTime'):
                                    yingyenianx = "不清楚至"+ time.strftime('%Y-%m-%d', time.localtime(
                                        int(get(jiben, 'toTime')) / 1000))
                                elif get(jiben, 'fromTime') and get(jiben, 'toTime')=='':
                                    yingyenianx = time.strftime('%Y-%m-%d', time.localtime(
                                        int(get(jiben, 'fromTime')) / 1000)) + "至不清楚"
                                else:
                                    yingyenianx=''
                                dengji = get(jiben, 'regInstitute')
                                zhucedizhi = get(jiben, 'regLocation')
                                jingyingfanwei = get(jiben, 'businessScope')
                                cursor.execute(sql2, (
                                quan, ceng, logo, phone, email, address, web, faren, zhuceziben, zhuceshijian,
                                jingyingzhuangtai, gongshang, zuzhijigou, tongyixinyong, qiyeleixing, hangye, yingyenianx,
                                dengji, zhucedizhi, jingyingfanwei, tid))
                                mysql.commit()
                                a=a+1
                                print('store data success'+str(a))
                                tabletablePro={'table':'tyc_jichu_gd'}
                                detail=[{'content':quan},{'content':ceng},{'content':logo},{'content':phone},{'content':email},{'content':address},
                                        {'content': web},{'content':faren},{'content':zhuceziben},{'content':zhuceshijian},{'content':jingyingzhuangtai},{'content':gongshang},
                                        {'content': zuzhijigou},{'content':tongyixinyong},{'content':qiyeleixing},{'content':hangye},{'content':yingyenianx},{'content':dengji},
                                        {'content': zhucedizhi},{'content':jingyingfanwei},{'content':str(tid)}]
                                deta={'detail':detail,'tablePro':tabletablePro}
                                js=json.dumps(str(deta),ensure_ascii=False)

                                dataee={
                                    'json':js.replace('"','').replace('\'','"')
                                }
                                jishu=0
                                while True:
                                    try:
                                        r=requests.post('http://59.110.52.96:8080/java_web/servlet/insertServlet',data=dataee,timeout=3)
                                        print(r.text)
                                        if 'insert spider success and insert log success' in r.content.decode(
                                                "utf-8"):
                                            break
                                    except Exception as eee:
                                        print('log error')
                                    jishu=jishu+1
                                    if jishu>=10:
                                        break
                except Exception as e:
                    print('error '+str(e))
                print('-------------------------------------------------------------------------------')
            else:
                break


if __name__ == '__main__':
    q = Queue()
    data(q)
    getdetail(q)
    print("over")
