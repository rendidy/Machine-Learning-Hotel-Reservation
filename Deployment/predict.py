import pandas as pd
import streamlit as st
import numpy as np
import pickle
import json

    

# Load file model

with open('best_model.pkl', 'rb') as file_1:
  best_model = pickle.load(file_1)

#menambah gambar
st.image('header.jpg')

def run():
  #membuat form 
  with st.form(key='form parameters'):

    book = st.text_input('Booking ID', )
    noa = st.number_input('Jumlah Orang Dewasa ', min_value=0, max_value=10, value=1,step=1,help='Jumlah Orang Dewasa')
    noc = st.number_input('Jumlah Anak-Anak', min_value=0, max_value=10, value=0,step=1,help='Jumlah Anak-anak')
    nownn = st.number_input('Jumlah Week End Night', min_value=0, max_value=10, value=1,step=1,help='Reservasi Saat Week End Berapa Hari?')
    nown = st.number_input('Jumlah Week Day Night', min_value=0, max_value=10, value=1,step=1,help='Jumlah Orang Dewasa')
    tomp = st.selectbox('Bundlie Meal yang Dipilih',('Not Selected','Type Meal 1','Type Meal 2','Meal Plan 3'),help='Pilih Tipe Bundling Meal')
    rcps = st.selectbox('Akses Parkir',('Yes','No'),help='Apakah Kamu Memerlukan Akses Parkir')
    rcpsnum = None
    if rcps == 'Yes':
      rcpsnum = 1
    else :
      rcpsnum = 0
        
    rtr = st.selectbox('Tipe Room',('Room_Type 1','Room_Type 2','Room_Type 3','Room_Type 4','Room_Type 5','Room_Type 6','Room_Type 7'),help='Pilih tipe ruangan yang di reservasi')
    lt = st.slider('Rentang Waktu (Hari)',1,700,7,help='Rentang Waktu Reservasi Hingga Tanggal Kedatangan')
    ay = st.selectbox('Tahun',('2017','2018'))
    am = st.selectbox('Bulan',('Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'),help='Reservasi untuk bulan apa?')
    amnum = None
    if am == 'Januari':
      amnum = 1
    if am == 'Februari':
      amnum = 2
    if am == 'Maret':
      amnum = 3
    if am == 'April':
      amnum = 4
    if am == 'Mei':
      amnum = 5
    if am == 'Juni':
      amnum = 6
    if am == 'Juli':
      amnum = 7
    if am == 'Agustus':
      amnum = 8
    if am == 'September':
      amnum = 9
    if am == 'Oktober':
      amnum = 10
    if am == 'November':
      amnum = 11
    else :
      amnum = 12
    
    ad = st.number_input('Tanggal', min_value=1, max_value=31, value=1,step=1,help='Tanggal berapa?')
    mst = st.selectbox('Segmentasi Reservasi',('Online','Offline','Corporate','Complementary','Aviation'),help='Reservasi Melalui apa?')
    rg = st.selectbox('Repeat Guest',('Yes','No'),help='Apakah Pelanggan Pernah Datang Sebelumnya?')
    rgnum = None
    if rg == 'Yes':
      rgnum = 1
    else :
      rgnum = 0

    nopc = st.number_input('Jumlah Pembatalan Sebelumnya', min_value=0, max_value=100, value=0,step=1,help='Pernah Melakukan Pembatalan Berapa Kali?')
    nopbnc = st.number_input('Pernah Reservasi Berapa Kali (Tanpa Pembatalan)', min_value=0, max_value=500, value=0,step=1,help='Jumlah Pemesanan Tanpa Pembatalan')
    appr = st.number_input('Harga Room', min_value=0, max_value=2000, value=50,step=1,help='Harga (USD)')
    nosr = st.number_input('Jumlah Special Request', min_value=0, max_value=10, value=0,step=1,help='Total Tagihan')
    

    Submitted = st.form_submit_button('Predict')

    data_inf = {
        'Booking_ID': book , 
        'no_of_adults': noa , 
        'no_of_children': noc , 
        'no_of_weekend_nights': nownn,
        'no_of_week_nights': nown, 
        'type_of_meal_plan': tomp , 
        'required_car_parking_space': rcpsnum ,
        'room_type_reserved': rtr , 
        'lead_time': lt , 
        'arrival_year': ay , 
        'arrival_month': amnum ,
        'arrival_date': ad , 
        'market_segment_type': mst , 
        'repeated_guest': rgnum ,
        'no_of_previous_cancellations': nopc , 
        'no_of_previous_bookings_not_canceled': nopbnc ,
        'avg_price_per_room': appr , 
        'no_of_special_requests': nosr  
       
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if Submitted:
    # Predict using linear regression
      y_pred_inf = best_model.predict(data_inf)

      if y_pred_inf == 0:
          st.write('## Predict: The reservation will not be canceled')
      elif y_pred_inf == 1:
          st.write('## Predict: The reservation will be canceled')

        
    #menambah gambar
    st.image('hotel.jpg')

if __name__ == '__main__':
    run()













