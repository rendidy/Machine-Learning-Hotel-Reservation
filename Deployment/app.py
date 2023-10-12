import streamlit as st
import eda 
import predict

navigation = st.sidebar.selectbox('Pilih Halaman:',('EDA Blissful Bay Hotel','Predict Cancellation Reservation'))

if navigation == 'EDA Blissful Bay Hotel':
    eda.run()
else:
    predict.run()