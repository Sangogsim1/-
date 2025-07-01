import streamlit as st
import re

def remove_parentheses(text):
    return re.sub(r"\([^)]*\)", "", text).strip()

st.set_page_config(
    page_title="여여부동산 시세계산기",
    page_icon=":house:",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    body {background-color: #fff3e0;}
    .stApp {background-color: #fff3e0;}
    .main-title {font-size:2.5rem; font-weight:bold; color:#ff9800; text-align:center; margin-bottom:0.5em;}
    .agency {font-family: 'Malgun Gothic', sans-serif; color:#7b5fa1; font-size:1.3rem; text-align:center; margin-bottom:2em;}
    .result-box {background:#fffde7; border-radius:16px; border:2px solid #ffd180; padding:1.5em; margin-top:1.5em; text-align:center;}
    .stButton>button {background:#ffd180; color:#a14d4d; font-weight:bold; border-radius:8px; font-size:1.1rem;}
    .stTextInput>div>input {background:#ffe0b2;}
    .stSelectbox>div>div {background:#ffe0b2;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">시세계산기</div>', unsafe_allow_html=True)
st.markdown('<div class="agency">여여부동산</div>', unsafe_allow_html=True)

base_price = st.number_input("기준가격 (예: 800,000,000)", value=800000000, format="%d")
danji = st.selectbox("단지", [-3, -2, -1, 0, 1, 2, 3], format_func=lambda x: f"{x:+d}")
dong = st.selectbox("동위치", [-3, -2, -1, 0, 1, 2, 3], format_func=lambda x: f"{x:+d}")
direction = st.selectbox("방향", [-3, -2, -1, 0, 1, 2, 3], format_func=lambda x: f"{x:+d}")
floor = st.selectbox("층수", [-3, -2, -1, 0, 1, 2, 3], format_func=lambda x: f"{x:+d}")
state = st.selectbox("실내상태", [-3, -2, -1, 0, 1, 2, 3], format_func=lambda x: f"{x:+d}")
option = st.text_input("옵션구성 (실제 금액을 입력하세요, 예: 2000000 또는 -1000000, 비우면 0)", value="")
extra = st.text_input("추가인정금액 (실제 금액을 입력하세요, 예: 1000000 또는 -500000, 비우면 0)", value="")

weights = {0:0, 1:0.012, 2:0.02, 3:0.035, -1:-0.012, -2:-0.02, -3:-0.035}
total_rate = weights[danji] + weights[dong] + weights[direction] + weights[floor] + weights[state]
try:
    option_val = int(option.replace(',', '')) if option.strip() else 0
except:
    option_val = 0
try:
    extra_val = int(extra.replace(',', '')) if extra.strip() else 0
except:
    extra_val = 0
result = round(base_price * (1 + total_rate)) + option_val + extra_val

if st.button("계산"):
    st.markdown(
        f'<div class="result-box"><span style="font-size:1.3rem;">예상 시세:</span><br><span style="font-size:2rem; color:#2d5c2f; font-weight:bold;">{result:,} 원</span></div>',
        unsafe_allow_html=True
    )

# 등급별 설명표 (괄호 및 괄호 안 내용 제거, 요청대로 표기)
if st.checkbox("등급별 설명 보기"):
    descs = [
        "-3: 매우 불리 -3.5%",
        "-2: 불리 -2%",
        "-1: 조금 불리 -1.2%",
        " 0: 기준 0%",
        "+1: 조금 유리 +1.2%",
        "+2: 유리 +2%",
        "+3: 매우 유리 +3.5%"
    ]
    st.markdown("**등급별 설명**")
    for d in descs:
        st.write(d)

# 옵션/추가인정금액 입력란 안내 강화
option = st.text_input("옵션구성 (실제 금액을 입력하세요, 예: 2000000 또는 -1000000, 비우면 0)", value="")
extra = st.text_input("추가인정금액 (실제 금액을 입력하세요, 예: 1000000 또는 -500000, 비우면 0)", value="") 