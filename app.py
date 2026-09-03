import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 기본 설정 (와이드 레이아웃, 사이드바 기본 숨김)
st.set_page_config(
    page_title="작업환경측정 계획서",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Streamlit 특유의 상하좌우 기본 여백 및 UI를 완전히 제거하는 강력한 CSS
st.markdown("""
    <style>
        /* 기본 여백 및 최대 너비 제한 완벽 제거 */
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            margin: 0rem !important;
            max-width: 100% !important;
        }
        
        /* 상단 헤더, 하단 워터마크, 툴바 등 Streamlit 기본 UI 숨김 */
        header {visibility: hidden !important; display: none !important;}
        footer {visibility: hidden !important; display: none !important;}
        div[data-testid="stToolbar"] {display: none !important;}
        
        /* iframe(HTML 화면)을 브라우저 화면 전체(100vh)에 꽉 차도록 강제 설정 */
        iframe {
            height: 100vh !important; 
            width: 100vw !important;
            border: none !important;
            margin: 0 !important;
            padding: 0 !important;
            display: block !important;
        }
        
        /* 배경색을 로그인 화면과 이질감 없도록 일치시킴 */
        .stApp {
            background-color: #F8FAFC !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. index.html 파일을 읽어와서 화면에 출력
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # HTML 렌더링 (CSS에서 100vh로 덮어씌우지만, 기본 속성으로 height 설정)
    components.html(html_content, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("index.html 파일을 찾을 수 없습니다. 동일한 폴더에 파일이 있는지 확인해 주세요.")
