
import streamlit as st

st.markdown(':red[以下更新自:2月10日起生效：]')
st.markdown(' - 上场Roll点，以数值结果更小者不上场;')
st.markdown(' - 每位玩家每周第一次上线，须将全部积分兑换为卡片(暂仍为每张4分)，不得透支;')
st.markdown(' - 每场最多合计使用3次卡（微光卡不计入该次数）,每种卡片你最多可以使用1次（刷新卡除外）;')
st.markdown(' - 若单周从未参与游戏或roll点，减4分, 直至零分.')

st.markdown(':red[此外：]')
st.markdown(' - 存量积分仍可按现卡种正常兑换卡片;')
st.markdown(' - 2月10日起将被停用的卡片：斩杀卡、混沌卡、梦境卡、相位卡、斩杀卡等;')
st.markdown(' - 2月8日、9日，以上卡片仍可正常使用，2月10日失效清零;')
st.markdown(' - 2月10日后未被停用的卡片可按新效果使用（包括升级的卡片）;')


card, buff, version = st.tabs([':credit_card: 卡片说明',':fire: 周BUFF/DEBUFF', ':back: 版本变化'])

with card:
    st.subheader('现行卡片')
    
    with st.expander(':one: _ :raised_hand_with_fingers_splayed: _推推卡 '):
        st.markdown(' - 请先指定使用对象，再roll3;')
        st.markdown(' - 若对自己使用，则自己点数 - 结果×10;')
        st.markdown(' - 若对他人使用，则对方点数 + 结果×10.')
        
    with st.expander(':two: _ :on: _沟壑卡 '):
        st.markdown('  - 使用后roll一次，可以选择≥或≤结果者重roll.')
        
    with st.expander(':three: _ :no_pedestrians: _静默卡 '):
        st.markdown(' - 使用后roll点，除你自己外，结果±12范围内的玩家本场无法再使用卡片.')
        
    with st.expander(':four: _ :zap: _雷神卡 '):
        st.markdown(' - 使用后roll点，除你自己外，结果±12范围内的玩家本场锁定登场.')
        st.markdown(' - （若范围内多于5人，则按和结果差的绝对值从小到大排列，更小的5人上场）')
        
    with st.expander(':five: _ :u6307: _死指卡 '):
        st.markdown(' - 只能对别人使用;')
        st.markdown(' - 使用后roll三次，若结果形成升序或降序，这时你可指定一人锁定登场.')
    
    with st.expander(':six: _ :cyclone: _刷新卡 '):
        st.markdown(' - 只能对自己使用;')
        st.markdown(' - 使用后roll点，小于原结果则对你刷新生效，否则用卡失败.')
        
    with st.expander(':seven: _ :ice_cube: _冰封卡 '):
        st.markdown(' - 只能对别人使用;')
        st.markdown(' - 使用后roll 5，如果结果为单数，这时你可指定目前场上的一人锁定登场.')
        
    with st.expander(':eight: _ :lab_coat: _微光卡 '):
        st.markdown(' - 只能对别人使用;')
        st.markdown(' - 你可以在其他人声明用卡但尚未roll点前使用此卡，则对方用卡效果对你无效。无法免除推推卡和吹风卡效果.')
    
    with st.expander(':nine: _ :tornado: _吹风卡 '):
        st.markdown(' - 请你先指定使用对象（当然包括你自己）;')
        st.markdown(' - roll两次，如果结果差值<20，本场使用对象免于登场.')
    
    with st.expander(':zero: _ :relaxed: _嘲讽卡 '):
        st.markdown(' - 嘲讽你自己吧，无卡.')
        
    with st.expander(':100: _ :tada: _贤者卡 '):
        st.markdown(' - 恭喜你，被动卡片，至本周结束，你每上一场可额外多积1分。多张贤者卡效果不叠加.')        


    st.subheader('停用卡片')
    
    with st.expander(':bomb: [43,50] _ 自爆卡 '):
        st.markdown(' - roll后使用，可选择≥或≤该结果者重roll。')
        st.markdown(' - 使用人选择1~10中3个自然数集合，被指定人roll 10。')
        st.markdown(' - 若roll结果在集合中，则被指定人替换上场，并锁定位置；否，则使用者-40，并禁用卡片。')
        st.markdown(' - 自爆卡不能在roll卡的最后一轮次使用。')
    
    with st.expander(':cyclone: [76,85] _ 混沌卡 '):
        st.markdown(' - 自己指定35的区间后，roll。')
        st.markdown(' - 若结果在该区间内，则指定任意2人重roll。')
    
    with st.expander(':u6307: [86,90] _ 梦境卡 '):
        st.markdown(' - 使用后当前无需登场者，按从大到小选择登场者交换点数。')
    
    with st.expander(':woman-heart-woman: [96,99] _ 缚魂卡 '):
        st.markdown(' - 指定1个目标，该目标自行选择绑定一个队友。')
        st.markdown(' - 两人分别roll 10，若两人结果相差<5，则两人绑定上场。')
     
    with st.expander(':currency_exchange: [91,99] _ 相位卡 '):
        st.markdown(' - roll点后，可将场上任意1人结果变更为该结果。')
    
    with st.expander(':axe: [100, 100] _ 斩杀卡 '):
        st.markdown(' - 使用后roll 4。')
        st.markdown(' - 指定无需登场者roll，若结果<50，则替换卡片使用者。否，则roll点原结果-roll点结果。')
    


with buff:
    
    st.subheader('周BUFF')
    st.write('周BUFF，面向上周积分第一、第二。第一，roll 4；第二，roll 2.')
  
    p = '''
    1. 「洗牌」，本周内使用，可在兑换卡片后撤销三次兑换，重新换卡。
    2. 「精准」，本周可使用两次，使用后可指定自己roll点结果。
    3. 「奥术」，本周内不受“一轮3张卡”的限制。
    4. 「双倍」，本周内使用的所有卡片，可自定义选择是否使用第二次，使用后第一次仍效果有效。
    '''
    st.markdown(p)
    
    st.subheader('周DEBUFF')
    st.write('周DEBUFF，面向上周积分最低者，roll 2.')
    p = '''
    1. 「赎罪」，本周参与的前两场需roll点出场比赛，锁定一个出场名额。
    2. 「虚弱」，本周内该玩家的上场roll点，需进行两次，并取较大值。
    '''
    st.markdown(p)
            
      
with version:
    
    st.divider()
    st.subheader('1.1.1')
    st.text('2025/2/10')
    p = '''
    - 原6个buff调整为4个，debuff由6个调整为2个；并对应调整roll点数值。
    - 停用原buff：「护盾」，可指定一种卡片，本周内“林肯”该卡。
    - 停用原buff：「支配」，本周可使用两次，选择四属性的各一名英雄，由被指定玩家本周内上场使用。
    - 停用原debuff：「沉默」，本周内，该玩家持有最高数量卡片被禁用(同数量皆)。
    - 停用原debuff：「束缚」，上周该玩家总积分最低英雄在本周被禁用。
    - 停用原debuff：「支配」，上周最高分可指定该玩家一次，在四属性英雄中各选一名，由被指定玩家选择出场。
    - 停用原debuff：「减疗」，本周积分获取量减半。
    '''
    st.markdown(p)
    
    st.divider()
    st.subheader('1.1.0')
    st.text('2025/2/8')
    p = '''
    - 交接前任会长规则;
    - 将卡片数值区间调整为尾数;
    - 暂停使用自爆卡、混沌卡、梦境卡、相位卡、斩杀卡等卡片;
    - 原饼干卡优化为推推卡,原雷击卡优化为雷神卡;
    - 新增静默卡、死指卡、冰封卡、微光卡、吹风卡、嘲讽卡、贤者卡.
    '''
    st.markdown(p)

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

