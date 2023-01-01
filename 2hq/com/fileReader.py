import json

import bean
class fileReader:
    def getItemList(self)->list[bean.itemOb]:
        pass
class csvfileReader(fileReader):
    def __init__(self, filename):
        self.filename = filename

    def getItemList(self) -> list[bean.itemOb]:
        itemList = []
        f = open(self.filename, 'r', encoding='utf-8')
        for line in f.readlines():
            # remove space and '\n'
            line=line.strip()
            # format of dict1: {"date": "2011-02-01", "order_id": "caf99222-53d6-427b-925d-3187fc71a86a", "money": 1805,"province": "江西省"}
            list1: list = line.split(',')
            # print(dict1)
            item = bean.itemOb(list1[0],list1[1],int(list1[2]),list1[3])
            itemList.append(item)
        return itemList
class jsonfileReader(fileReader):
    def __init__(self,filename):
        self.filename=filename
    def getItemList(self) ->list[bean.itemOb]:
        itemList=[]
        f=open(self.filename,'r',encoding='utf-8')
        for line in f.readlines():
            # remove space and '\n'
            line.strip()
            #format of dict1: {"date": "2011-02-01", "order_id": "caf99222-53d6-427b-925d-3187fc71a86a", "money": 1805,"province": "江西省"}
            dict1:dict=json.loads(line)
            # print(dict1)
            item=bean.itemOb(dict1['date'],dict1['order_id'],int(dict1['money']),dict1['province'])
            itemList.append(item)
        return itemList
if __name__ == '__main__':
    jsonfileReader=jsonfileReader('E:\programme\Python\practice\Fesaledata.txt')
    list1=jsonfileReader.getItemList()
    csvfileReader = csvfileReader('E:\programme\Python\practice\Januarysaledata.txt')
    list2 = csvfileReader.getItemList()
