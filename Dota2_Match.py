
import pytz
import json
import time
import datetime
import urllib 
import requests
import numpy as np
import pandas as pd
import streamlit as st

headers = {  
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}  

name = {
    '899457221': '嬛嬛' ,
    '323137248': '我躺下了' ,
    '477959505': '一场游戏一场梦' ,
    '259623855': '梦醒时分' ,
    '480132789': 'RogerLe0n' ,
    '137804277': '他一生要强' ,
    '260236789': '著名野餐组织家' ,
    '899001454': '拷打者' ,
    '1221854081': '__HC__' ,
    '899527848': '僵!' ,
    '915025033': '面包超人' ,
    '1262250160': '克里斯' ,
    '1266892230': '齐景春' ,
    '1011407811': '加速手套' ,
    '1227564282': 'NK带我飞' ,
    '1037094036': '针不戳' ,
    '194522861': '拿你的头...' ,
    '1265081636': '印第安老黑猫' ,
    '1264547137':'国家反诈中心' ,
    }

progress_text = "查询玩家的历史比赛..."
progress_num = 0
my_bar = st.progress(0, text = progress_text)