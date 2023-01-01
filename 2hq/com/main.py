from pyecharts.globals import ThemeType

from fileReader import jsonfileReader,csvfileReader
from pyecharts.charts import Bar
from pyecharts.options import TitleOpts, LabelOpts, InitOpts
from bean import itemOb
# encapsulate data with beanObject
jsonfileReader = jsonfileReader('E:\programme\Python\practice\Fesaledata.txt')
list1 = jsonfileReader.getItemList()
# encapsulate data with beanObject
csvfileReader = csvfileReader('E:\programme\Python\practice\Januarysaledata.txt')
list2 = csvfileReader.getItemList()

date_list:list[itemOb]=list2+list1

dict1={}
# sum up the money every country in a day
for item in date_list:
    if item.data in dict1:
        dict1[item.data]+=item.money
    else:
        dict1[item.data]=item.money
        # print(item.data)
data_x=list(dict1.keys())
data_y=list(dict1.values())

bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_yaxis('money',data_y,label_opts=LabelOpts(is_show=False))
bar.add_xaxis(data_x)
bar.render('sale.html')




