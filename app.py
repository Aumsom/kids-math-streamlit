import pandas as pd
import streamlit as st

st.set_page_config(page_title='Kids Math', page_icon='🧮')
st.title('🧮 Kids Math Practice')

df=pd.read_csv('data/questions.csv')
grade=st.selectbox('Grade',sorted(df.grade.unique()))
theme=st.selectbox('Theme',sorted(df[df.grade==grade].theme.unique()))
rows=df[(df.grade==grade)&(df.theme==theme)].reset_index(drop=True)

if 'i' not in st.session_state:
    st.session_state.i=0
    st.session_state.score=0

row=rows.iloc[st.session_state.i % len(rows)]
st.write(f'Question {st.session_state.i+1}')
st.write(row.question)
ans=st.text_input('Answer')
if st.button('Submit'):
    try:
        if int(ans)==int(row.answer):
            st.success('Correct!')
            st.session_state.score+=1
        else:
            st.error(f'Correct answer: {row.answer}')
    except:
        st.error('Enter a number')
    st.write(f'Score: {st.session_state.score}')
    st.session_state.i+=1
    st.rerun()
