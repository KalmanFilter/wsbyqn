
import os
import json
import requests
import numpy as np
import akshare as ak
import streamlit as st
from datetime import datetime
from cnsenti import Sentiment
from borax.calendars import LunarDate



# ========================================================================================
# 快讯
df = ak.stock_info_global_cls()
b3 = st.button('🔄 Refresh ')
if b3:
    df = ak.stock_telegraph_cls()
df = df.iloc[::-1]
df = df.head(200)
df.index = range(0,len(df))
senti = Sentiment()
for i in range(0,len(df)):
    dt = str(df.iloc[i]['发布日期'].month) + '月' + str(df.iloc[i]['发布日期'].day) + '日 ' 
    dt = dt + str(df.iloc[i]['发布时间'].hour) + ':' + str(df.iloc[i]['发布时间'].minute) + ':'+ str(df.iloc[i]['发布时间'].second)
    title = str(df.iloc[i]['标题'])
    if '《新闻联播》' in title:
        title = ':exclamation: ' +title
    h = ['习近平','李强','赵乐际','王沪宁','蔡奇','丁薛祥','李希']
    if any(s in title for s in h):
        title = ':sparkling_heart: ' + title
    h = ['拜登','白宫']
    if any(s in title for s in h):
        title = ':shit: ' + title
    h = ['住房','地产','房贷','购房','城中村','楼盘','房企',
         '住建部','认房不认贷','房股','完整社区','二手房','楼市','商品房','首套房','公积金']
    if any(s in title for s in h):
        title = ':house_buildings: ' + title
    h = ['电影','票房','影院']
    if any(s in title for s in h):
        title = ':film_projector: ' + title
    h = ['飞机','机场','航班']
    if any(s in title for s in h):
        title = ':airplane_arriving: ' +title
    h = ['航空','航天','卫星','火箭']
    if any(s in title for s in h):
        title = ':satellite: ' + title
    h = ['高铁','动车','新干线']
    if any(s in title for s in h):
        title = ':bullettrain_front: ' + title
    h = ['汽车','车企','电动车','油车','特斯拉','Model 3','新车','二手车']
    if any(s in title for s in h):
        title = ':car: ' + title
    h = ['医药','医保']
    if any(s in title for s in h):
        title = ':ambulance: ' +title
    h = ['AI','人工智能','大模型']
    if any(s in title for s in h):
        title = ':computer: ' +title
    h = ['数据要素','数据资源']
    if any(s in title for s in h):
        title = ':information_source: ' +title
    h = ['iPhone','iPad','Mate','Galaxy','手机']
    if any(s in title for s in h):
        title = ':iphone: ' +title
    if '台风' in title:
        title = ':tornado: ' +title
    h = ['降雨','大雨','暴雨']
    if any(s in title for s in h):
        title = ':rain_cloud: ' +title
    h = ['银行','央行','美联储','IMF']
    if any(s in title for s in h):
        title = ':bank: ' +title
    if '美元' in title:
        title = ':dollar: ' +title
    if '人民币' in title:
        title = ':yen: ' +title
    if '欧元' in title:
        title = ':euro: ' +title

    st.subheader(title)
    
    content = df.iloc[i]['内容']
    k = content.find('日电，')
    if k>0:
        k = k+3
    else:
        k = 0
    content = content[k:]
    # 分析情绪
    pos = int(senti.sentiment_calculate(content)['pos'])
    neg = int(senti.sentiment_calculate(content)['neg'])

    st.write(content)

    clock_num = df.iloc[i]['发布时间'].hour % 12
    if clock_num == 0:
        clock_num = 12
    if df.iloc[i]['发布时间'].minute >=30:
        clock_num = clock_num * 100 + 30
    clock_num = ':clock' + str(clock_num) + ':'	
    col1,col2 = st.columns([4,1])
    with col1:
        st.caption(clock_num + dt)
    with col2:
        st.caption(':grin: ：' + str(pos) + ' | ' +':worried: ：' + str(neg))