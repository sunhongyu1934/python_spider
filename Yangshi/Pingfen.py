__author__ = 'Administrator'


from functools import reduce


def Wen(list):
    maiche={'danwangji' : '1/2','hetong':'0','laoshaojieyi':'1','huitouke':'1','liwu':'0','dingqikehu':'1','kedingzhi':'1','dadianhua':'0','yingchou':'1/2','nengdong':'0','shengzhi':'0','nvbinan':'1','suishen':'1'}
    sheyipin={'danwangji' : '1','hetong':'1','laoshaojieyi':'1/2','huitouke':'0','liwu':'0','dingqikehu':'0','kedingzhi':'1/2','dadianhua':'1','yingchou':'1','nengdong':'1','shengzhi':'0','nvbinan':'1','suishen':'0'}
    shengxian={'danwangji' : '1','hetong':'1','laoshaojieyi':'0','huitouke':'0','liwu':'0','dingqikehu':'1','kedingzhi':'1','dadianhua':'1','yingchou':'1','nengdong':'1','shengzhi':'0','nvbinan':'0','suishen':'0'}
    huazhuangpin={'danwangji' : '1','hetong':'1','laoshaojieyi':'1','huitouke':'0','liwu':'0','dingqikehu':'1','kedingzhi':'1','dadianhua':'1','yingchou':'1','nengdong':'1','shengzhi':'1','nvbinan':'0','suishen':'0'}
    lvyou={'danwangji' : '0/2','hetong':'0','laoshaojieyi':'0','huitouke':'0','liwu':'0','dingqikehu':'0/2','kedingzhi':'0','dadianhua':'1','yingchou':'1','nengdong':'1','shengzhi':'1','nvbinan':'0/2','suishen':'1'}
    fangzi={'danwangji' : '0/2','hetong':'0','laoshaojieyi':'0','huitouke':'1','liwu':'0','dingqikehu':'0/2','kedingzhi':'1','dadianhua':'0','yingchou':'1/2','nengdong':'1','shengzhi':'0','nvbinan':'1','suishen':'1'}
    peixun={'danwangji' : '0','hetong':'0','laoshaojieyi':'0/2','huitouke':'1','liwu':'0','dingqikehu':'0','kedingzhi':'0','dadianhua':'0','yingchou':'1','nengdong':'1','shengzhi':'1','nvbinan':'2','suishen':'1'}
    baoxian={'danwangji' : '1','hetong':'0','laoshaojieyi':'0','huitouke':'1/2','liwu':'0','dingqikehu':'0','kedingzhi':'1/2','dadianhua':'0','yingchou':'1/2','nengdong':'1','shengzhi':'1','nvbinan':'2','suishen':'1'}
    mairuanjian={'danwangji' : '1','hetong':'0','laoshaojieyi':'1/2','huitouke':'1','liwu':'1','dingqikehu':'0','kedingzhi':'0','dadianhua':'0','yingchou':'0','nengdong':'1','shengzhi':'0','nvbinan':'1','suishen':'0'}
    mudi={'danwangji' : '1','hetong':'0','laoshaojieyi':'1','huitouke':'1','liwu':'1','dingqikehu':'1','kedingzhi':'1/2','dadianhua':'1','yingchou':'1','nengdong':'1','shengzhi':'0','nvbinan':'2','suishen':'1'}
    hunjie={'danwangji' : '1','hetong':'0/2','laoshaojieyi':'1','huitouke':'1','liwu':'1','dingqikehu':'0','kedingzhi':'0','dadianhua':'1','yingchou':'1','nengdong':'1','shengzhi':'1','nvbinan':'2','suishen':'1'}
    xiuxian={'danwangji' : '1','hetong':'0','laoshaojieyi':'0','huitouke':'0','liwu':'0','dingqikehu':'0','kedingzhi':'1','dadianhua':'0','yingchou':'1','nengdong':'1','shengzhi':'1','nvbinan':'0/2','suishen':'1'}
    yiliao={'danwangji' : '1','hetong':'0','laoshaojieyi':'1/2','huitouke':'0/2','liwu':'1','dingqikehu':'0','kedingzhi':'1','dadianhua':'1','yingchou':'0','nengdong':'0','shengzhi':'1','nvbinan':'2','suishen':'1/2'}
    chongwu={'danwangji' : '1','hetong':'1','laoshaojieyi':'0','huitouke':'0','liwu':'0','dingqikehu':'1','kedingzhi':'1','dadianhua':'1','yingchou':'1','nengdong':'1','shengzhi':'1','nvbinan':'1','suishen':'1'}
    meirong={'danwangji' : '1','hetong':'1/2','laoshaojieyi':'1','huitouke':'0/2','liwu':'0','dingqikehu':'0','kedingzhi':'0/2','dadianhua':'1/2','yingchou':'1','nengdong':'1','shengzhi':'1','nvbinan':'0','suishen':'1'}
    muying={'danwangji' : '1','hetong':'1','laoshaojieyi':'1','huitouke':'0','liwu':'0','dingqikehu':'0','kedingzhi':'1','dadianhua':'1','yingchou':'1','nengdong':'1','shengzhi':'1','nvbinan':'0/2','suishen':'1'}
    jiadian={'danwangji' : '1','hetong':'1','laoshaojieyi':'0','huitouke':'0','liwu':'0','dingqikehu':'1','kedingzhi':'1','dadianhua':'1','yingchou':'1','nengdong':'1/2','shengzhi':'1','nvbinan':'2','suishen':'1'}
    sanc={'danwangji' : '1/2','hetong':'1','laoshaojieyi':'0','huitouke':'0','liwu':'0','dingqikehu':'1','kedingzhi':'1','dadianhua':'1','yingchou':'1','nengdong':'1','shengzhi':'1','nvbinan':'1','suishen':'0'}
    fuzhuang={'danwangji' : '1','hetong':'1','laoshaojieyi':'0','huitouke':'0','liwu':'0','dingqikehu':'0/2','kedingzhi':'0','dadianhua':'1','yingchou':'1','nengdong':'1','shengzhi':'1','nvbinan':'0/2','suishen':'0'}
    jiancai={'danwangji' : '0/2','hetong':'0','laoshaojieyi':'1/2','huitouke':'0','liwu':'1','dingqikehu':'1','kedingzhi':'1','dadianhua':'1','yingchou':'0/2','nengdong':'1','shengzhi':'1','nvbinan':'1','suishen':'1'}

    list2=[{'maiche':maiche},{'sheyipin':sheyipin},{'shengxian':shengxian},{'huazhuangpin':huazhuangpin},{'lvyou':lvyou},{'fangzi':fangzi},{'peixun':peixun},{'baoxian':baoxian},{'mairuanjian':mairuanjian},{'mudi':mudi},{'hunjie':hunjie},{'xiuxian':xiuxian},{'yiliao':yiliao},{'chongwu':chongwu},{'meirong':meirong},{'muying':muying},{'jiadian':jiadian},{'sanc':sanc},{'fuzhuang':fuzhuang},{'jiancai':jiancai}]





    fens=[]
    for p in list2:
        fen = 0
        for (a,b) in p.items():
            for (c,d) in b.items():
                for (la, lb) in list.items():
                    if la==c:
                        ds=d.split('/')
                        for dd in ds:
                            if lb==dd:
                                fen=fen+10
                                break
            fens.append({a:fen})


    print (reduce(Bijiao,fens))




def Bijiao(x,y):
    if list(x.values())[0] >= list(y.values())[0]:
        return x
    else:
        return y





if __name__=='__main__':
    file=open("C:\\Users\\Administrator\\Desktop\\wenti.txt")
    lines=file.readlines()
    list2={}
    for line in lines:
        daan=str(line,).replace('\n','')
        list2[daan.split(',')[0]]=daan.split(',')[1]

    Wen(list2)