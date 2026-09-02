import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 기본 설정 (와이드 레이아웃, 사이드바 기본 숨김)
st.set_page_config(
    page_title="작업환경측정 계획서",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Streamlit 특유의 상하좌우 기본 여백(Padding)을 없애는 CSS 적용
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }
        /* 상단 헤더(주메뉴) 숨기기 */
        header {visibility: hidden;}
        /* 하단 워터마크 숨기기 */
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. index.html 파일을 읽어와서 화면에 출력
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # HTML을 Streamlit 화면에 렌더링 (높이 여유 있게 설정, 스크롤 허용)
    components.html(html_content, height=1500, scrolling=True)

except FileNotFoundError:
    st.error("index.html 파일을 찾을 수 없습니다. 동일한 폴더에 파일이 있는지 확인해 주세요.")
