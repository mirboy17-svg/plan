import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit 페이지 설정 (전체 화면 넓게 사용)
st.set_page_config(
    page_title="작업환경측정 계획서",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. index.html 파일을 읽어오기
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_data = f.read()
        
    # 3. 읽어온 HTML을 Streamlit 화면에 렌더링
    # height를 충분히 주어 스크롤이 원활하게 되도록 설정합니다.
    components.html(html_data, height=1500, scrolling=True)

except FileNotFoundError:
    st.error("index.html 파일을 찾을 수 없습니다. app.py와 같은 폴더에 있는지 확인해주세요.")
