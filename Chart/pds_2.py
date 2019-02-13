# coding:utf-8
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
dt = pd.read_json('../Bibili/author.json', orient='records', encoding='utf-8')
bins = [0, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 1500, 2000, 2500, np.inf]
st = pd.DataFrame()
d2 = pd.cut(dt['follower'], bins=bins)
dl = pd.cut(dt['following'], bins=bins)
reg1 = dl.value_counts()
reg2 = d2.value_counts()
st.insert(0, 'follower', reg1)
st.insert(1, 'following', reg2)
print st
st[['follower', 'following']].plot(kind='bar', color='green', figsize=(8, 4), grid=True)
plt.xticks(rotation=50)
plt.xlabel("区间", fontproperties=font)
plt.ylabel("数量", fontproperties=font)
plt.title("粉丝&关注数量区间条形图", fontproperties=font)
plt.show()
plt.close()
