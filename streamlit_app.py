import streamlit as st
import information_ex as ie

st.markdown('''## **UI Information Extraction**''')
st.write('')
st.markdown('''**NAMA: FAKHRUL IBAD**''')
st.markdown('''**NIM: 210411100212**''')
st.write('')

st.markdown('''Extracting Subject, Predicate, and Object from sentence''')
st.write('')

inputan = st.text_input("ENTER SENTENCES (ENGLISH)", "John completed the task")

sub, obj = ie.get_entities(inputan)
pred = ie.get_relation(inputan)

st.write('')
st.write('')
st.write('')

if sub == '':
    st.markdown(f'''##### Subject: :red[-]''')
else:
    st.markdown(f'''##### Subject: :red[{sub}]''')
if pred == '':
    st.markdown(f'''##### Predicate (Verb): :green[-]''')
else:
    st.markdown(f'''##### Predicate (Verb): :green[{pred}]''')
if obj == '':
    st.markdown(f'''##### Object: :orange[-]''')
else:
    st.markdown(f'''##### Object: :orange[{obj}]''')
