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
        
        /* iframe의 높이를 화면 전체(100vh)로 꽉 채우도록 설정 */
        iframe { 
            width: 100% !important; 
            height: 100vh !important; /* viewport 높이에 맞춤 */
            border: none !important; 
            display: block; /* 기본 여백 제거 */
        }
    </style>
""", unsafe_allow_html=True)

# 2. index.html 파일을 읽어오기
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_data = f.read()
        
    # 3. 읽어온 HTML을 Streamlit 화면에 렌더링
    # 고정된 height 값(1200)을 제거하고, CSS에서 height: 100vh를 적용받도록 합니다.
    # 추가로 자바스크립트를 통해 부모 창의 크기에 맞게 조정하는 꼼수를 쓸 수 있지만, 
    # Streamlit 컴포넌트 특성상 height 파라미터가 없으면 기본값(150px)이 적용되므로
    # 충분히 큰 값을 주고 CSS로 제한하거나, 자바스크립트 기반 컴포넌트를 사용해야 합니다.
    # 여기서는 좀 더 확실한 방법으로, Streamlit의 컴포넌트 컨테이너 자체를 100vh로 만듭니다.
    components.html(html_data, height=1000, scrolling=False) 
    
    # 참고: height 파라미터는 iframe의 높이를 지정합니다. 
    # CSS에서 height: 100vh !important 를 주었으므로 이 값은 무시되거나 보완적으로 작용합니다.
    # 만약 위 방법으로도 안된다면 아래 자바스크립트 코드를 index.html 내부에 삽입하여 
    # 동적으로 높이를 맞추는 방법이 필요할 수 있습니다.

except FileNotFoundError:
    st.error("index.html 파일을 찾을 수 없습니다. app.py와 같은 폴더에 있는지 확인해주세요.")
