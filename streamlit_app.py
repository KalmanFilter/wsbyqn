
import streamlit as st

st.set_page_config(
    page_title="边缘青年",
    page_icon=":video_game:",	
    initial_sidebar_state="auto",    
)

pages = {
    "Function":[
        st.Page("news.py", title = 'News',),
        st.Page("chat.py", title = 'Chat'),
        ],

    "DOTA2": [
        st.Page("Dota2_IMP.py", title="IMP", icon=':material/stadia_controller:'),
        st.Page("Dota2_Match.py", title="比赛", icon=':material/joystick:'),
        st.Page("Dota2_Player.py", title="玩家", icon=':material/assignment_ind:'),
        st.Page("Dota2_Card.py", title="卡片",  icon=':material/stack_star:'),
    ],
    "FIFAOL3": [
        st.Page("FIFAOL3_League.py", title="联赛", icon=':material/emoji_events:'),
        st.Page("FIFAOL3_Cup.py", title="杯赛", icon=':material/rewarded_ads:'),
    ],
}
pg = st.navigation(pages)
pg.run()
 