import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


st.set_page_config(
    page_title = 'Hotel Reservation - EDA',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)


def run():
    #membuat title
    st.title('Blissful Bay Hotel')

    #membuat sub header
    st.subheader('Statistic Report Blissful Bay Hotel')

    #menambah gambar
    st.image('https://watermark.lovepik.com/photo/20211120/large/lovepik-the-outdoor-swimming-pool-of-the-luxury-resort-picture_500484656.jpg')
    # menambah deskripsi
    st.write('Page ini dibuat oleh rendidy')
    st.write('# Wellcome to Blissful Bay Hotel')
   

    #membuat garis lurus
    st.markdown('---')

    #magic syntax
    '''
    Hallo Semuanya. Selamat Datang Di Blissful Bay Hotel Statistic Report.
    Dataset yang digunakan adalah Hotel Reservation.
    Dataset ini diperoleh dari web Kaggle
    '''
    #show Dataframe
    df = pd.read_csv('Hotel Reservations.csv')
    st.dataframe(df)



    #membuat barplot
    st.write('#### Pie Chart Booking Status')
    booking_status_counts = df['booking_status'].value_counts()
    # Pilih palet warna dari Seaborn 
    colors = sns.color_palette("plasma")
    fig = plt.figure(figsize=(6,6))
    plt.pie(booking_status_counts, labels=booking_status_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.axis('equal')  # Mengatur aspek lingkaran agar terlihat seperti lingkaran
    st.pyplot(fig)
    st.write("Analisa")
    st.write("- Terlihat bahwa kolom target 'booking status' memiliki data yang tidak balance. Untuk itu perlu dilakukan balancing data agar model machine learning dapat belajar lebih optimal dan mendapatkan hasil prediksi yang semakin akurat.")
    st.write("- Namun, imbalance ini secara umum bisa dikatakan adalah hal yang normal. Karena memang pada umumnya persentase pembatalan reservasi hotel tidaklah banyak dibandingkan dengan yang tidak melakukan pembatalan.")



    #membuat barplot berdasarkan input user
    st.write('#### Bar Plot Categorical Terhadap  Booking Status Berdasarkan Input User')
    pilihan = st.selectbox('Pilih kolom :', ['type_of_meal_plan', 'room_type_reserved', 'market_segment_type'])
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(data=df, x=pilihan, hue='booking_status', palette='plasma')
    plt.legend(title='Booking  Status', labels=['Tidak Dibatalkan ', 'Dibatalkan'])
    plt.xlabel(pilihan)
    plt.ylabel('Count')
    st.pyplot(fig)
    st.write("Analisa: ")
    st.write("Berdasarkan ketiga grafik dari kolom kategorikal di atas:")
    st.write("- Meal Plan 1 merupakan pilihan yang paling banyak diambil oleh pelanggan yang melakukan reservasi hotel. Namun, secara umum, tidak ada perbedaan yang signifikan antara pemilihan meal plan dengan cancel or not cancel reservation karena cancel terjadi di semua tipe meal plan dengan proporsi yang sama/cukup mirip.")
    st.write("- Room Type 1 merupakan room type yang paling banyak direservasi. Namun, bezapun dengan Room Type yang dipilih, proporsi perbandingan Cancel dan no cancel terlihat memiliki pola yang sama.")
    st.write("- Online reservation menjadi market segment type yang paling banyak digunakan oleh pelanggan. Dan proporsi perbandingan Cancel dan no cancel terlihat memiliki pola yang sama.")
    st.write("- Berdasarkan ketiga kolom di atas, tidak ada pilihan dari meal plan, room type, ataupun market segment yang benar-benar dapat dikatakan paling banyak menyebabkan Cancel Reservation. Semua memiliki pola proporsi yang sama tergantung banyaknya pesanan yang dipilih.")



    #membuat hist berdasarkan input user
    st.write('#### Histogram Numerical Terhadap Booking Status Berdasarkan Input User')
    pilihan = st.selectbox('Pilih kolom:', ['no_of_week_nights', 'lead_time', 'avg_price_per_room'])
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(data=df, x=pilihan, hue='booking_status', bins=30, kde=True, palette='plasma')
    plt.legend(title='Booking Status', labels=['Tidak Dibatalkan', 'Dibatalkan'])
    plt.xlabel(pilihan)
    plt.ylabel('Count')
    st.pyplot(fig)
    st.write("Analisa :")
    st.write("Berdasarkan dari tiga grafik kolom numerikal di atas:")
    st.write("- Dengan rata-rata berada disekitar angka 2, dan dilihat secara keseluruhan persebaran data grafik kolom 'no_of_week_nights', jumlah 'not cancel' lebih besar dibandingkan 'cancel' dan secara umum memiliki proporsi yang sama dan merata.")
    st.write("- Jika dilihat dari persebaran data 'lead_time', ketika kira-kira lead time di atas 150 hari, terjadi kecenderungan peningkatan rating 'cancel' / pembatalan reservasi dibanding 'not cancel'. Hal ini menunjukkan bahwa semakin lama jarak waktu pemesanan dengan kedatangan pelanggan, semakin besar kemungkinan terjadinya pembatalan reservasi.")
    st.write("- Dilihat dari persebaran data 'avg_price_per_room', dengan pola rasio yang sama antara 'cancel' yang lebih kecil dibandingkan 'not cancel', tergantung pada rata-rata harganya pesanan yang dipilih pelanggan. Hal ini menunjukkan tidak ada kecenderungan yang signifikan antara besarnya harga rata-rata reservasi dengan potensi pembatalan reservasi.")



    #membuat barplot berdasarkan input user
    st.write('##### Bar Plot Categorical Numeric Terhadap Booking Status Berdasarkan Input User')
    pilihan = st.selectbox('Pilih kolom:', ['no_of_adults','no_of_children', 'no_of_weekend_nights', 'no_of_previous_bookings_not_canceled', 'no_of_previous_cancellations', 'required_car_parking_space', 'arrival_year', 'arrival_month', 'arrival_date', 'repeated_guest', 'no_of_special_requests'])
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(data=df, x=pilihan, hue='booking_status', palette='plasma')
    plt.legend(title='Booking Status', labels=['Tidak Dibatalkan', 'Dibatalkan'])
    plt.xlabel(pilihan)
    plt.ylabel('Count')
    st.pyplot(fig)
    st.write(" Analisa:")
    st.write("Berdasarkan dari 11 grafik kolom kategorikal numerik di atas:")
    st.write("- Jika dilihat dari keseluruhan grafik di atas, hampir semuanya memiliki pola dan proporsi yang sama antara 'Not Cancel' dan 'Cancel'.")
    st.write("- Namun, ada beberapa rasio yang berbeda atau dapat dikatakan sebagai anomali, seperti arrival month di bulan 12, dengan jumlah reservasi yang tinggi, rate cancelnya cukup kecil dibandingkan dengan 'not cancel'. Lalu pada arrival date tanggal 2, dengan jumlah reservasi yang tinggi, rate cancelnya cukup kecil dibandingkan dengan 'not cancel'. Selanjutnya pada kolom special request, saat special request = 0 (tidak ada permintaan khusus), rate cancelnya cukup tinggi hampir mengimbangi 'not cancel'.")
    st.write("- Untuk yang saya katakan sebagai 'ANOMALI' ini, adalah faktor-faktor yang dapat diperhatikan yang dapat mempengaruhi tingkat/rating pembatalan reservasi.")



    st.write('#### Bar Plot Arrival Month per Arrival Year')
    tahun_terpilih = st.selectbox('Pilih Tahun:', ['2017', '2018'])
    # Filter data berdasarkan tahun yang dipilih
    data_tahun_terpilih = df[df['arrival_year'] == int(tahun_terpilih)]
    # Hitung jumlah kemunculan 'arrival_month' untuk setiap tahun
    jumlah_bulan_per_tahun = data_tahun_terpilih['arrival_month'].value_counts().sort_index()
    fig = plt.figure(figsize=(12, 6))
    plt.bar(jumlah_bulan_per_tahun.index, jumlah_bulan_per_tahun.values, color='purple')
    plt.xlabel('Arrival Month')
    plt.ylabel('Count')
    plt.title(f'Bar Plot Arrival Month per Arrival Year ({tahun_terpilih})')
    st.pyplot(fig)
    st.write("Analisa:  ")
    st.write("- Terlihat bahwa dataset ini dimulai dari bulan 7 tahun 2017 hingga bulan 12 tahun 2018.")
    st.write("- Terlihat bahwa baik di tahun 2017 maupun 2018, reservasi paling banyak dilakukan untuk bulan Oktober.")
    st.write("- Jika dilihat dari jumlah pelanggan pada tahun 2017 dan 2018, dapat disimpulkan bahwa hotel ini mungkin baru beroperasi pada bulan Juli 2017. Seiring berjalannya waktu, terjadi peningkatan yang signifikan dalam jumlah pelanggan, menunjukkan peningkatan reputasi hotel tersebut.")


    st.write('#### Bar Plot Room Type Reserved vs Avg Price per Room')
    fig = plt.figure(figsize=(12, 8))
    sns.barplot(data=df, x='room_type_reserved', y='avg_price_per_room', palette='plasma')
    plt.xlabel('Room Type Reserved')
    plt.ylabel('Average Price per Room ')
    plt.title('Bar Plot Room Type Reserved vs Avg Price per Room')
    st.pyplot(fig)
    st.write('Analisa:')
    st.write('- Terlihat dari room type yang dipilih pelanggan, room type 6 adalah yang paling mahal dibandingkan dengan room type lainnya.')
    st.write('- Room type 3 menjadi yang paling murah dibanding room type lainnya.')
    st.write('- Jika dilihat dari informasi grafik sebelumnya, Room type 1 adalah yang paling banyak di reservasi. Ini adalah hal wajar, karena pada umumnya pelanggan memesan room type yang memiliki harga tidak terlalu mahal, dan tidak juga terlalu murah.')
    st.write('- Lalu room type 6 tidaklah banyak yang mereservasinya, tentunya karena harganya yang cukup mahal.')
    st.write('- Lalu room type 3 sangat sedikit yang mereservasinya, hal ini juga wajar karena biasanya room type murah tidak bisa menikmati beberapa fasilitas yang tersedia di hotel.')


    st.write('#### Bar Plot Room Type Reserved vs Avg Price per Room by Meal Plan')
    fig = plt.figure(figsize=(12, 8))
    sns.barplot(data=df, x='room_type_reserved', y='avg_price_per_room', hue='type_of_meal_plan', palette='plasma')
    plt.xlabel('Room Type Reserved')
    plt.ylabel('Average Price per Room')
    plt.title('Bar Plot Room Type Reserved vs Avg Price per Room by Meal Plan')
    st.pyplot(fig)
    st.write('Analisa:')
    st.write('- Terlihat bahwa setiap pelanggan yang mereservasi type room yang berbeda-beda, memilih kecendrungan pilihan type meal yang berbeda-beda pula.')
    st.write('- Terlihat hanya pada room type 1 yang memesan meal plan 3, hal ini mungkin bisa terjadi karena room type 1 merupakan room type yang paling banyak di reservasi dan memiliki bundling tersendiri dengan meal plan 3.')
    st.write('- Begitupun dengan room 3 dan 7, saya berasumsi bahwa hanya tersedia pilihan meal plan 1 untuk kedua room tersebut.')


    st.write('#### Scatter Plot Lead Time vs Avg Price per Room')
    fig = plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x='lead_time', y='avg_price_per_room', hue='arrival_month', palette='plasma')
    plt.xlabel('Lead Time')
    plt.ylabel('Average Price per Room')
    plt.title('Scatter Plot Lead Time vs Avg Price per Room')
    st.pyplot(fig)
    st.write("Analisa:")
    st.write("Jika dilihat dari persebaran data di atas:")
    st.write("- Jarak waktu reservasi dengan kedatangan pelanggan yang besar atau rentang waktu yang lama, pada umumnya terjadi pada reservasi yang dilakukan pada bulan 10 hingga 12, dengan rata-rata harga kamar di sekitar 100 dollar.")
    st.write("- Sedangkan untuk rata-rata harga kamar yang mahal (300 dollar ke atas), lead time-nya biasanya kurang dari 175 hari sebelum kedatangan pelanggan.")


    st.write('## Thankyou ^.^')
    st.write('rendidy')


if __name__== '__main__':
    run()















