
import os
import pytz
import random
import numpy as np
import streamlit as st
from datetime import datetime , timedelta


st.header('随机抽签分组')

st.subheader('参赛队伍')

st.markdown('''
- 打铁的
- 尿不湿
- 应体面
- 巧克力
- 在被打
- HBomb            

''')

x = ['打铁的','尿不湿','应体面','巧克力','在被打','HBomb']


if st.button('生成随机分组'):
    
    y = random.sample(x, len(x))
    st.markdown('')
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader('A组')
        st.write(y[0])
        st.write(y[1])
    with col2:
        st.subheader('B组')
        st.write(y[2])
        st.write(y[3])
    with col3:
        st.subheader('C组')
        st.write(y[4])
        st.write(y[5])
    
    time_now = datetime.now(pytz.utc)
    time_now = time_now.astimezone(pytz.timezone('Asia/Shanghai'))
    st.write(time_now)