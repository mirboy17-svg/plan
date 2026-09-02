import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정 (와이드 모드)
st.set_page_config(layout="wide", page_title="작업환경측정 계획서", initial_sidebar_state="collapsed")

# 1. index.html 파일 읽기
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 2. 🚀 핵심! 내부 HTML의 높이를 계산해서 바깥 Streamlit(iframe)으로 쏴주는 자바스크립트 주입
# 이 코드가 HTML 렌더링이 끝난 직후 높이를 재서 iframe 크기를 딱 맞게 맞춰줍니다.
auto_resize_script = """
<script>
    function sendHeight() {
        // 메인 컨텐츠 영역의 높이 계산
        const height = Math.max(
            document.body.scrollHeight, 
            document.documentElement.scrollHeight,
            document.getElementById('mainAppContent') ? document.getElementById('mainAppContent').scrollHeight : 0
        );
        // 부모 창(Streamlit)으로 높이 값 전송
        window.parent.postMessage({
            isStreamlitMessage: true,
            type: "setFrameHeight",
            height: height + 50 // 약간의 여유 공간 추가
        }, "*");
    }
    
    // 화면 크기가 변하거나, 클릭(요약표 생성 등) 이벤트가 있을 때마다 높이 다시 계산
    window.onload = sendHeight;
    window.addEventListener("resize", sendHeight);
    document.addEventListener("click", () => setTimeout(sendHeight, 100));
</script>
"""

# HTML 닫는 태그 직전에 스크립트를 끼워넣음
final_html = html_content.replace('</body>', auto_resize_script + '</body>')

# 3. HTML 렌더링 (scrolling=True 를 줘야 버그가 안생김)
components.html(final_html, height=1200, scrolling=True) 

# 주의: 
# 처음 로딩 시에는 height=1200(임시 높이)으로 열렸다가, 
# 방금 주입한 자바스크립트가 돌아가면서 내용물에 딱 맞는 높이로 Iframe이 자동 조절됩니다!
