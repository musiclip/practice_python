import streamlit as st

def app():
    st.write('''
# st.dataframe()
데이터 프레임 테이블 보기

- 기본형태

st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, column_order=None, column_config=None)


# st.pyplot()
차트 그리기

- 기본형태

st.pyplot(fig=None, clear_figure=None, use_container_width=True, **kwargs)

# st.button()
st.button()은 클릭하기 전에는 False를, 버튼을 클릭하면 True를 찍어낸다.
disable을 사용하여 체크박스에 체크를 했을 경우 버튼을 누를 수 있도록 하는 방법도 있다.

- 기본형태

st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)

# st.text_input
변수명(텍스트)를 입력하여 결과값을 받는 코드

- 기본형태

st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")


# st.title/header/write
타이틀과 헤더, 글을 작성할 수 있다.

- 기본형태
  
st.title(body, anchor=None, *, help=None)
st.header(body, anchor=None, *, help=None)
st.write(*args, unsafe_allow_html=False, **kwargs)
             '''
             )
    