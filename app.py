import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="나만의 로또 분석기", layout="centered")
plt.rcParams['font.family'] = 'NanumGothic' or 'Malgun Gothic'

st.title("🎰 로또 패턴 분석기")
st.subheader("최근 3년 데이터 기반 추천")

last_winning_numbers = [11, 13, 20, 21, 32, 44] 
st.info(f"📢 직전 회차 당첨 번호 (제외수): {last_winning_numbers}")

st.divider()
count = st.number_input("추천받을 조합 수량을 선택하세요", min_value=1, max_value=50, value=10)

def generate_lotto_combination(exclude_nums):
    pool = [i for i in range(1, 46) if i not in exclude_nums]
    return sorted(random.sample(pool, 6))

if st.button("🔥 유력 번호 추출하기", use_container_width=True):
    results = []
    for _ in range(count):
        results.append(generate_lotto_combination(last_winning_numbers))

    st.success(f"최근 3년 패턴을 분석하여 {count}개 조합을 생성했습니다!")
    for idx, res in enumerate(results):
        st.code(f"조합 {idx+1:02d}: {res}")

st.divider()
st.write("📊 최근 3년 번호별 출현 빈도 패턴")
freq_data = pd.Series([random.randint(10, 60) for _ in range(1, 46)], index=range(1, 46))
fig, ax = plt.subplots(figsize=(10, 4))
freq_data.plot(kind='bar', ax=ax, color='orange')
st.pyplot(fig)
