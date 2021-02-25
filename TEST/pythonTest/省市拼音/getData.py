import pypinyin
import json


def get_pinyin(name):
    pinYin="".join(pypinyin.lazy_pinyin(name['name']))
    name=name['name']
    if pinYin.find('sheng')>0:
        pinYin=pinYin[0:len(pinYin)-5]
        name=name[0:len(name)-1]
    if pinYin.find('shi')>0:
        pinYin=pinYin[0:len(pinYin)-3]
        name=name[0:len(name)-1]
    return { name:pinYin}

with open('全国地区名.txt','r') as file,\
    open('out.txt','w',encoding='utf-8') as out:
    citys=json.load(file)
    citys_pinyin=map(get_pinyin, citys)
    output=list(citys_pinyin)
    #print(list(citys))
    print(output)
    json.dump(output,out,ensure_ascii=False)
    #print(list(b))
