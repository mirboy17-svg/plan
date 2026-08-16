import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit 페이지 설정 (전체 화면 넓게 사용)
st.set_page_config(
    page_title="작업환경측정 계획서",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Streamlit 기본 여백(위, 좌, 우, 아래) 및 상단 빈 헤더 영역 완벽 제거
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        header {visibility: hidden !important;}
        #MainMenu {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        iframe { width: 100% !important; border: none !important; }
    </style>
""", unsafe_allow_html=True)

# 2. index.html 파일을 읽어오기
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_data = f.read()
        
    # 3. 읽어온 HTML을 Streamlit 화면에 렌더링 (scrolling=False 로 변경하여 이중 스크롤 방지, 높이 자동 맞춤)
    components.html(html_data, height=1200, scrolling=False)

except FileNotFoundError:
    st.error("index.html 파일을 찾을 수 없습니다. app.py와 같은 폴더에 있는지 확인해주세요.")
