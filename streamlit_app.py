import streamlit as st
import information_ex as ie

st.markdown('''## **UI Information Extraction**''')
st.write('')

st.markdown('''Extracting Subject, Predicate, and Object from sentence''')
st.write('')

inputan = st.text_input("ENTER SENTENCES (ENGLISH)", "John completed the task")

sub, obj = ie.get_entities(inputan)
pred = ie.get_relation(inputan)

st.write('')
st.write('')
st.write('')
st.markdown(f'''##### Subject: :red[{sub}]''')
st.markdown(f'''##### Predicate: :green[{pred}]''')
st.markdown(f'''##### Object: :orange[{obj}]''')