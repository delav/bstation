# coding:utf-8
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
create_time = datetime.datetime.strptime('2009-06-01', "%Y-%m-%d")
dt = pd.read_json('../Bibili/author.json', orient='records', encoding='utf-8')
patt = r'(\d{4}-\d{1,2})'
dt['register_time'] = dt['register_time'].str.extract(patt, expand=True)
dt['register_time'] = pd.to_datetime(dt['register_time'])
dt.ix[dt['register_time'] < create_time, 'register_time'] = create_time

# dp = dt.set_index('date')
# print dt.index
# print dt.shape
dl = dt.groupby(['register_time'], as_index=False)['register_time'].agg({'cnt': 'count'}).sort_values(by='register_time')
# print(dl.info())
# print(dl.describe())
# diff()函数对数据进行某种移动之后与原数据进行比较得出的差异数据
# dl['cnt'] = dl['cnt'].diff()
# shift()函数对数据进行移动操作

dl.insert(2, 'rise', (dl['cnt']-dl['cnt'].shift(1))/dl['cnt'].shift(1))
dl.insert(3, 'nums', (dl['cnt'].cumsum()))
print dl
# print dt['date'].value_counts()
# 较上月增长率
# dl.plot(x=dl['register_time'], y='rise', kind='line', linestyle='-', markerfacecolor='red',
#         marker='o', color='green', figsize=(8, 4), grid=True)
# 增长曲线图
dl.plot(x=dl['register_time'], y='nums', kind='line', linestyle='-', markerfacecolor='red',
        marker='o', color='green', figsize=(8, 4), grid=True)
# 统计条形图
# dl.plot(x=dl['register_time'].apply(lambda x: x.strftime('%Y-%m')), y='cnt', kind='bar',
#         color='green', figsize=(8, 4), grid=True)
plt.xticks(rotation=50)
plt.xlabel("月份", fontproperties=font)
plt.ylabel("数量", fontproperties=font)
plt.title("注册人数增长趋势图", fontproperties=font)
plt.show()
plt.close()
