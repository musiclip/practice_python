import streamlit as st

def desc():
    st.title('Streamlit Test')
    input_user_name = st.text_input(label = '이름을 입력하세요.', value = '')

    if st.button('Confirm'):
#con = st.container()
#con.caption('Result')
#con.write(f'Hello! {str(input_user_name)}')
        st.write(f'Hello! {str(input_user_name)}')