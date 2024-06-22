import streamlit as st

from transformers import pipeline

st.title('Natural Language Processing')

st.image('https://images.pexels.com/photos/18069696/pexels-photo-18069696.png')

st.header('About')

st.write('This application allows you to use two NLP models:')
st.write('1. English text sentiment analysis')
st.write('2. English to German translation')

st.header('Instruction')

st.write('1. Choose model')
st.write('2. Enter some text and confirm with Ctrl+Enter')
st.write('3. Wait for result')

option = st.selectbox(
    'Choose model',
    [
        'English text sentiment analysis',
        'English to German translation',
    ],
)

text = st.text_area(label='Enter text')

if text:
    model = None

    if option == 'English text sentiment analysis':
        model = pipeline("sentiment-analysis")
    elif option == 'English to German translation':
        model = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
    
    with st.spinner(text='Processing...'):
        answer = model(text)
        st.success('Done')
        st.write(answer)

st.subheader('Author')
st.write('Tomasz Radzki s22132')
