import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 기본 설정 (와이드 레이아웃, 사이드바 숨김)
st.set_page_config(
    page_title="작업환경측정 계획서",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Streamlit 상하좌우 여백(Padding) 완전 제거 및 헤더 숨김
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }
        /* 상단 빈 공간(헤더) 및 하단 워터마크 숨기기 */
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. index.html 파일 읽기 및 화면 출력
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # 💡 Iframe 높이(height)를 1500 이상으로 넉넉하게 주어 표가 잘리지 않도록 방지
    # (로그인 창은 방금 HTML에서 상단 고정했으므로 높이가 커도 문제없습니다!)
    components.html(html_content, height=1500, scrolling=True)

except FileNotFoundError:
    st.error("오류: index.html 파일을 찾을 수 없습니다. app.py와 같은 폴더에 있는지 확인해 주세요.")
```eof

**💡 팁:** 
만약 나중에 사업장 규모가 매우 커서 표가 아래로 엄청나게 길어지는데 바깥쪽 창이 짤린다면, 코드 하단의 `height=1500` 숫자를 `2000`이나 `2500`으로 여유 있게 더 늘려주시기만 하면 됩니다!
