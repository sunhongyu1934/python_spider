import time
import json
import codecs

class GetproxyPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        fileName = today+'proxy360.json'
        with codecs.open(fileName,'a',encoding='utf-8') as fp:
            line = json.dumps(dict(item),ensure_ascii=False)+'\n'
            fp.write(line)
        return item