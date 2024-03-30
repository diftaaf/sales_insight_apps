import streamlit as st

st.write('Test Streamlit')
st.write('Random text')
st.title('Training hari ini')
st.write('Hello, *world!* :sunglasses:')
angka_pertama = st.number_input('Insert a number')
st.write('The first number is ', angka_pertama)

angka_kedua = st.number_input('insert a number')
st.write('The second number is', angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
st.write(f"Angka pertama {angka_pertama} x Angka kedua {angka_kedua} = {operasi_matematika}")