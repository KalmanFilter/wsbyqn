
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
    #'915025033': '面包超人' ,
    #'1262250160': '克里斯' ,
    #'1266892230': '齐景春' ,
    #'1011407811': '加速手套' ,
    #'1227564282': 'NK带我飞' ,
    #'1037094036': '针不戳' ,
    #'194522861': '拿你的头...' ,
    #'1265081636': '印第安老黑猫' ,
    #'1264547137':'国家反诈中心' ,
    }

avatar = {
    '899457221': 'https://avatars.steamstatic.com/737a9d5a131a70d6e49e3be560e0c97f85d5679d_full.jpg' ,
    '323137248': 'https://avatars.steamstatic.com/3c3b66d14988bc8ac71e9e1d1f2ea826d5ec04a3_full.jpg' ,
    '477959505': 'https://avatars.steamstatic.com/a21e6bf609dbaf4aa9880af2b6a39ab3b3e5ceda_full.jpg' ,
    '259623855': 'https://avatars.steamstatic.com/d2ecdc3e6fcb50f73790c5ba2f6ad700f2ab6c45_full.jpg' ,
    '480132789': 'https://avatars.steamstatic.com/c83f4196806cd7792dff77146ebfb2462a1e4289_full.jpg' ,
    '137804277': 'https://avatars.steamstatic.com/4550df75b653d1747eda2d2f7aeaf10e35039b5b_full.jpg' ,
    '260236789': 'https://avatars.steamstatic.com/73661533481539d34bfa036b3f84aa15f3f44787_full.jpg' ,
    '899001454': 'https://avatars.steamstatic.com/d8fdaeadbea9ec82deb25b90719a3f598adc94eb_full.jpg' ,
    '1221854081': 'https://avatars.steamstatic.com/b75929e7d101f11c77fb06cd657e3651d8542a22_full.jpg' ,
    '899527848': 'https://avatars.steamstatic.com/bbe5653abb028380d4faabdef0e4836ec9933c47_full.jpg' ,
    #'915025033': '面包超人' ,
    #'1262250160': '克里斯' ,
    #'1266892230': '齐景春' ,
    #'1011407811': '加速手套' ,
    #'1227564282': 'NK带我飞' ,
    #'1037094036': '针不戳' ,
    #'194522861': '拿你的头...' ,
    #'1265081636': '印第安老黑猫' ,
    #'1264547137':'国家反诈中心' ,
    }  

hero_pic = {
1:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/antimage.png',
2:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/axe.png',
3:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bane.png',
4:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bloodseeker.png',
5:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/crystal_maiden.png',
6:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/drow_ranger.png',
7:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/earthshaker.png',
8:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/juggernaut.png',
9:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/mirana.png',
11:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/nevermore.png',
10:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/morphling.png',
12:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/phantom_lancer.png',
13:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/puck.png',
14:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/pudge.png',
15:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/razor.png',
16:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/sand_king.png',
17:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/storm_spirit.png',
18:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/sven.png',
19:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/tiny.png',
20:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/vengefulspirit.png',
21:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/windrunner.png',
22:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/zuus.png',
23:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/kunkka.png',
25:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/lina.png',
31:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/lich.png',
26:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/lion.png',
27:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/shadow_shaman.png',
28:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/slardar.png',
29:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/tidehunter.png',
30:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/witch_doctor.png',
32:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/riki.png',
33:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/enigma.png',
34:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/tinker.png',
35:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/sniper.png',
36:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/necrolyte.png',
37:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/warlock.png',
38:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/beastmaster.png',
39:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/queenofpain.png',
40:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/venomancer.png',
41:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/faceless_void.png',
42:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/skeleton_king.png',
43:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/death_prophet.png',
44:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/phantom_assassin.png',
45:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/pugna.png',
46:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/templar_assassin.png',
47:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/viper.png',
48:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/luna.png',
49:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/dragon_knight.png',
50:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/dazzle.png',
51:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/rattletrap.png',
52:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/leshrac.png',
53:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/furion.png',
54:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/life_stealer.png',
55:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/dark_seer.png',
56:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/clinkz.png',
57:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/omniknight.png',
58:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/enchantress.png',
59:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/huskar.png',
60:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/night_stalker.png',
61:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/broodmother.png',
62:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bounty_hunter.png',
63:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/weaver.png',
64:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/jakiro.png',
65:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/batrider.png',
66:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/chen.png',
67:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/spectre.png',
69:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/doom_bringer.png',
68:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ancient_apparition.png',
70:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ursa.png',
71:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/spirit_breaker.png',
72:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/gyrocopter.png',
73:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/alchemist.png',
74:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/invoker.png',
75:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/silencer.png',
76:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/obsidian_destroyer.png',
77:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/lycan.png',
78:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/brewmaster.png',
79:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/shadow_demon.png',
80:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/lone_druid.png',
81:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/chaos_knight.png',
82:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/meepo.png',
83:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/treant.png',
84:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ogre_magi.png',
85:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/undying.png',
86:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/rubick.png',
87:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/disruptor.png',
88:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/nyx_assassin.png',
89:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/naga_siren.png',
90:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/keeper_of_the_light.png',
91:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/wisp.png',
92:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/visage.png',
93:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/slark.png',
94:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/medusa.png',
95:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/troll_warlord.png',
96:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/centaur.png',
97:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/magnataur.png',
98:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/shredder.png',
99:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/bristleback.png',
100:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/tusk.png',
101:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/skywrath_mage.png',
102:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/abaddon.png',
103:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/elder_titan.png',
104:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/legion_commander.png',
106:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ember_spirit.png',
107:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/earth_spirit.png',
108:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/abyssal_underlord.png',
109:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/terrorblade.png',
110:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/phoenix.png',
105:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/techies.png',
111:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/oracle.png',
112:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/winter_wyvern.png',
113:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/arc_warden.png',
114:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/monkey_king.png',
119:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/dark_willow.png',
120:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/pangolier.png',
121:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/grimstroke.png',
123:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/hoodwink.png',
126:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/void_spirit.png',
128:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/snapfire.png',
129:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/mars.png',
131:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/ringmaster.png',
135:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/dawnbreaker.png',
136:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/marci.png',
137:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/primal_beast.png',
138:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/muerta.png',
145:'https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/kez.png',

    }
     

st.header('周IMP排名')
beijing_tz = pytz.timezone('Asia/Shanghai')
# 选择日期
today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
today = today.astimezone(beijing_tz)
wkday = today.weekday()
# 如果今天不是周一，则显示本周。
if wkday > 0:
    d0 = today - datetime.timedelta(days=wkday)
    d1 = today + datetime.timedelta(days=6-wkday)
    
# 如果今天是周一，则显示上周。
if wkday == 0:
    d0 = today - datetime.timedelta(days=wkday+7)
    d1 = today - datetime.timedelta(days=wkday+1)
    st.write('今天是周一，展示上周游戏结果.')

d0 = d0.timestamp()
d1 = d1.timestamp() + 86400

# 查询条 | 查询玩家近期比赛
progress_text = "准备查询玩家近期比赛..."
progress_num = 0
my_bar = st.progress(0, text = progress_text)

api = 'https://api.opendota.com/api/players/'
    # 收集大家最近的match_id
match_id = []
for ids in name.keys():
    # 查询10个ID，这个循环结束后进度是50%.
    progress_num = progress_num + 5
    progress_text = '查询 「 ' + name[ids] + ' 」 的近期比赛...via OpenDota...'
    my_bar.progress(progress_num, text=progress_text)

    url = api + ids + '/recentMatches'
    response = requests.get(url)
    data = response.json()
    if len(data) > 0: # 玩家隐藏信息则data为空
        for t in data:
            if t['lobby_type'] == 0 and t['start_time']>d0 and t['start_time']<d1 : 
                #这里仅记录了普通匹配(lobbytype为0)，因为现在对黑不玩天梯(lobbytype为7).
                match_id.append(str(t['match_id']))

          
match_id = np.array(match_id)
match_id = set(match_id) #列表去重
match_id = [int(item) for item in match_id] # 列表数值化
match_id = np.array(match_id)
match_id = np.sort(match_id)
match_num = len(match_id)

games = pd.DataFrame(columns=['date','gameid','steamid','heroid','pos','wl','imp'])

if match_num == 0:
    progress_num = 100
    progress_text = '没有比赛记录?!...'
    my_bar.progress(progress_num, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.write('本周未有游戏记录... ')
else:
    progress_cc = int(50/match_num)
    # 爬取STRATZ比赛页面中信息.
    for p in match_id:
        url = "https://stratz.com/matches/"
        url = url + str(p)
        progress_text = '正在了解比赛 [ ' + str(p) + ' ] 的详情... via Stratz...'
        progress_num = progress_num + progress_cc 
        my_bar.progress(progress_num, text=progress_text)
        
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req, timeout = 10)
        html = res.read()
        html = str(html, encoding='utf-8')
        k = 0
        for ids in name.keys():
            v = html.count(ids)
            if v>0:
                k = k+1
            # 判断比赛是否为五黑
        if k ==5:
            # 提取“天辉是否胜利”信息
            w = html.index('didRadiantWin\\":')
            # w 是f(fasle)或t(ture)
            w = html[w+16:w+17]
            # 提取比赛开始时间戳
            z1 = html.index('endDateTime\\')
            z1 = int(html[z1+14:z1+24])
            z2 = html.index('durationSeconds\\')
            z2 = html[z2+18:z2+24]
            z2 = int(z2[:z2.find(',')])
            # starttime = endtime - durationseconds
            z0 = z1 - z2
            z0 = datetime.datetime.fromtimestamp(z0).date()
            for ids in name.keys():
                
                v = '{\\"id\\":' + ids
                v = html.find(v)
                if v > 0:
                    # 截取与这位玩家有关的代码片段
                    y = html[0:v]
                    # 英雄信息
                    hero = '-'
                    r = 'eroId\\":'
                    s = y.rfind(r)
                    t = y[s+8:s+13].find(',')
                    hero = int(y[s+8:s+8+t])
                    # 位置信息
                    r = 'POSITION_'
                    s = y.rfind(r)
                    if s < 0:
                        continue
                    else:
                        pos = y[s:s+10]
                    # IMP信息
                    r = '\\"imp\\":'
                    s = y.rfind(r)
                    imp = pd.NA
                    if s>0:
                        t = y[s+8:s+12].find(',')
                        if t>0:
                            imp = int(y[s+8:s+8+t])
                    # 胜负信息
                    r = '\\"isRadiant\\":'
                    s = y.rfind(r)
                    x = y[s+14:s+15]
                    if x == w:
                        wl = 'W'
                    else:
                        wl = 'L'
                        
                    rec = {'date':z0, 'gameid':p, 'steamid':ids, 'heroid':hero, 'pos':pos, 'wl':wl, 'imp':imp}
                    rec = pd.DataFrame([rec])
                    games = pd.concat([games,rec])

    
    # 结算
    my_bar.progress(100, text='查询结束...')
    time.sleep(.5)
    my_bar.empty()
    
    dg = games
    # 统计玩家名称(steamid 对应的 name)
    dg_name = [name[key] for key in dg['steamid'].unique() ]
    # 玩家的头像
    dg_img = [avatar[key] for key in dg['steamid'].unique()]
    # 统计steamid出现的频次
    dg_cnt = [dg['steamid'].value_counts()[ids] for ids in dg['steamid'].unique()]
    # 统计玩了多少个英雄
    dg_hud = [len(dg[dg['steamid']==ids]['heroid'].unique()) for ids in dg['steamid'].unique()]
    # 统计每个steamid的胜率
    dg_wct = [len( dg[ (dg['steamid']==ids) & (dg['wl']=='W')]) for ids in dg['steamid'].unique()]
    # 胜场与频次列表相除得到胜率
    dg_wr = [x/y for x ,y in zip(dg_wct, dg_cnt)] 
    # 统计每个steamid的IMP总和
    dg_imp = [ dg[dg['steamid']==ids]['imp'].sum() for ids in dg['steamid'].unique()]
    # 合成一个用于显示的Dataframe
    dd = pd.DataFrame( {'Avatar':dg_img,'Name':dg_name, 'Games':dg_cnt, 'IMP':dg_imp, 'WR(%)':dg_wr, 'Heros':dg_hud, }  ) 
    # 降序排列IMP
    dd = dd.sort_values(by='IMP', ascending=False)
    # 胜率保留一位小数
    dd['WR(%)'] = dd['WR(%)'].apply(lambda x: "{:.1%}".format(x))
    


    st.subheader('周统计')
    
    st.dataframe(dd,
             use_container_width = True,
             hide_index = True,
             column_config = {
                 'Avatar': st.column_config.ImageColumn()
                 }
             )
    
    # ----------------------------------------------------------------------

    st.subheader('周明细')
    # 比赛编号降序，最近的比赛优先.
    de = dg.sort_values(by = 'gameid', ascending = False)
    game_id = de['gameid'].unique()
    
    for ids in game_id:
        
        dh = de[de['gameid'] == ids]
        dh_date = dh.iloc[0]['date']
        dh_wl   = dh.iloc[0]['wl']
        st.write( str(dh_date) + '  /   '+ str(ids)   + '  /  ' + str(dh_wl))
        dh = dh[['heroid','steamid','pos','imp']]
        dh = dh.sort_values(by = 'pos', ascending = True)

        replacements = {'steamid':name,'heroid': hero_pic }  
        for col, rules in replacements.items():
            dh[col] = dh[col].replace(rules)

        st.dataframe(dh,
             use_container_width = True,
             hide_index = True,
             column_config = {
                 'heroid': st.column_config.ImageColumn()
                 }
             )
    
