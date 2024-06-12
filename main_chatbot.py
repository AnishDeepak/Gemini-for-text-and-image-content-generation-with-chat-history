import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model=genai.GenerativeModel('gemini-pro')

model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

def get_response(query):
    response=chat.send_message(query,stream=True)
    return response

st.set_page_config(page_title='chatbot using gemini-pro')
st.header('Chatbot using Gemini-pro')

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]


input=st.text_input('input:',key='input')
submit=st.button('Ask the question')
if submit:
    response=get_response(input)
    st.session_state['chat_history'].append(('you',input))
    st.subheader('The response is')
    for chunck in response:
        st.write(chunck.text)
        st.session_state['chat_history'].append(('Bot',chunck.text))

st.subheader('The chat history is')

for role,text in st.session_state['chat_history']:
    st.write(f'{role}:{text}')
