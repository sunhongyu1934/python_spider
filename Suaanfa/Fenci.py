import jieba

def test():
    #seg_list = jieba.cut("北京因果树网络科技有限公司", cut_all=True)
    #print("Full Mode: " + "/ ".join(seg_list))  # 全模式

    #seg_list = jieba.cut("北京因果树网络科技有限公司", cut_all=False)
    #print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
    address=['北京','上海','天津','重庆','新疆','乌鲁木齐','克拉玛依','吐鲁番','哈密','西藏','拉萨','宁夏','银川','石嘴山','吴忠','固原','中卫','内蒙古','呼和浩特','包头','乌海','赤峰',
             '通辽','鄂尔多斯','呼伦贝尔','巴彦淖尔','乌兰察布','广西','南宁','柳州','桂林','梧州','北海','崇左','来宾','贺州','玉林','百色','河池','钦州','防城港','贵港']


    seg_list = jieba.cut("因果树巴彦淖尔市网络科技有限公司")  # 默认是精确模式
    print(", ".join(seg_list))

    #seg_list = jieba.cut_for_search("北京因果树网络科技有限公司")  # 搜索引擎模式
    #print(", ".join(seg_list))

if __name__=='__main__':
    test()