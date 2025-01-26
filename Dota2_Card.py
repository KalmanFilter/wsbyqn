
import streamlit as st

card, buff, version = st.tabs([':credit_card: 卡片说明',':fire: 周BUFF/DEBUFF', ':back: 版本变化'])

with card:
    st.subheader('现行卡片')
    
    with st.expander(':rewind: [1,17] _ 沟壑卡 '):
        st.markdown(' - roll后使用，可选择≥或≤该结果者重roll。')
    
    with st.expander(':zap: [18,34] _ 雷击卡 '):
        st.markdown('  - 使用后roll一次，除自己外，最靠近结果者锁定登场(小于roll结果)。')
        
    with st.expander(':cookie: [35,42] _ 饼干卡 '):
        st.markdown(' - 使用后roll 4。')
        st.markdown(' - 若结果为1、2、3，则指定人点数+30；')
        st.markdown(' - 若结果为4，则-30。')
        
    with st.expander(':bomb: [43,50] _ 自爆卡 '):
        st.markdown(' - roll后使用，可选择≥或≤该结果者重roll。')
        st.markdown(' - 使用人选择1~10中3个自然数集合，被指定人roll 10。')
        st.markdown(' - 若roll结果在集合中，则被指定人替换上场，并锁定位置；否，则使用者-40，并禁用卡片。')
        st.markdown(' - 自爆卡不能在roll卡的最后一轮次使用。')
        
    with st.expander(':recycle: [51,75] _ 刷新卡 '):
        st.markdown(' - 使用后roll，刷新自己roll的结果。')
        
    with st.expander(':cyclone: [76,85] _ 混沌卡 '):
        st.markdown(' - 自己指定35的区间后，roll。')
        st.markdown(' - 若结果在该区间内，则指定任意2人重roll。')
        
    with st.expander(':u6307: [86,90] _ 梦境卡 '):
        st.markdown(' - 使用后当前无需登场者，按从大到小选择登场者交换点数。')
        
    with st.expander(':currency_exchange: [91,99] _ 相位卡 '):
        st.markdown(' - roll点后，可将场上任意1人结果变更为该结果。')
        
    with st.expander(':axe: [100, 100] _ 斩杀卡 '):
        st.markdown(' - 使用后roll 4。')
        st.markdown(' - 指定无需登场者roll，若结果<50，则替换卡片使用者。否，则roll点原结果-roll点结果。')
        

    st.subheader('停用卡片')
    with st.expander(':woman-heart-woman: [96,99] _ 缚魂卡 '):
        st.markdown(' - 指定1个目标，该目标自行选择绑定一个队友。')
        st.markdown(' - 两人分别roll 10，若两人结果相差<5，则两人绑定上场。')

    
    

with buff:
    
    st.subheader('周BUFF')
    st.write('周BUFF，面向上周积分第一、第二。第一，roll 6；第二，roll 3.')
  
    p = '''
    1. 「洗牌」，本周内使用，可将自己的某一种存量卡片兑换为积分。
    2. 「护盾」，可指定一种卡片，本周内“林肯”该卡。
    3. 「精准」，本周可使用两次，使用后可指定自己roll点结果。
    4. 「奥术」，本周内不受“一轮4张卡”的限制。
    5. 「支配」，本周可使用两次，选择四属性的各一名英雄，由被指定玩家本周内上场使用。
    6. 「双倍」，本周内使用的所有卡片，可自定义选择是否使用第二次。
    '''
    st.markdown(p)
    
    st.subheader('周DEBUFF')
    st.write('周DEBUFF，面向上周积分最低者，roll 6.')
    p = '''
    1. 「沉默」，本周内，该玩家持有最高数量卡片被禁用(同数量皆)。
    2. 「束缚」，上周该玩家总积分最低英雄在本周被禁用。
    3. 「支配」，上周最高分可指定该玩家一次，在四属性英雄中各选一名，由被指定玩家选择出场。
    4. 「赎罪」，本周参与的前两场需roll点出场比赛，锁定一个出场名额。
    5. 「虚弱」，本周内该玩家的上场roll点，需进行两次，并取较小值。
    6. 「减疗」，本周积分获取量减半。
    '''
    st.markdown(p)
            
      
with version:
    
    st.divider()
    st.subheader('1.0.1')
    st.text('2024/11/11')
    p = '''
    - 暂停使用缚魂卡
    - 相位卡区间由[91,95]，调整至[91,99]
    '''
    st.markdown(p)
    
    st.divider()
    st.subheader('1.0.0')
    st.text('2024/11/4')
    p = '''
    - 交接前任会长制定规则、存量道具，并沿用。
    '''
    st.markdown(p)

