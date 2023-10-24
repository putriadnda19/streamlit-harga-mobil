import pickle 
import streamlit as st 

model = pickle.load(open('estimasihargamobil.sav', 'rb'))

st.title('Estimasi Harga Mobil')

ID = st.number_input('Input ID')
Cylinders = st.number_input('Input Silinder Mobil')
Airbags = st.number_input('Input Airbag Mobil')

predict = ''

if st.button('Estimasi Harga '):
    predict = model.predict(
        [[ID, Cylinders, Airbags]]
    )
    st.write('Estimasi Harga Mobil: ', predict)