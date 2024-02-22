# Proyek Analisis Data: E-Commerce Analysis ✨
Saya **Toni Andreas Susanto** mempersembahkan Dashboard Analysis E-Commerce, sebuah alat yang memudahkan menganalisis data perusahaan
E-Commerce dengan visualisasi yang mendalam dan interaktif. Mari menemukan berbagai insight dari perusahaan kami.

## Deskripsi File 
1. `asset` : Berisi foto untuk profil dalam website streamlit.
2. `.ipynb_checkpoints` : history file.
3. `E-Commerce Public Dataset` : Berisi dataset yang digunakan untuk mengerjakan proyek ini.
4. `requirements.txt` : File yang berisi List packages dalam environment projek ini.
5. `streamlit.py` : File code program untuk menjalankan dashboard.
6. `Proyek_Analisis_Data.ipynb` : File untuk melakukan berbagai proses hingga dapat menghasilkan visualisasi data dan insight.
7. `README.md` : Informasi detail dari projek ini.
8. `url.txt` : URL Dashboard dari Proyek ini.

## Latar Belakang 
Analisis ini menggunakan dataset berupa kumpulan data publik dari sebuah e-commerce di Brazil, Olist Store. Dataset ini mencakup informasi dari 100 ribu pesanan yang dilakukan dari tahun 2016 hingga 2018 melalui berbagai platform penjualan di Brazil, berikut sumbernya [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). Data ini memberikan informasi pesanan dari berbagai dimensi: mulai dari status pesanan, harga, pembayaran, kinerja pengiriman, lokasi pelanggan, atribut produk, hingga ulasan yang ditulis oleh pelanggan.

Olist adalah toko departemen terbesar di pasar e-commerce Brazil yang menghubungkan usaha kecil dari seluruh Brazil ke berbagai saluran penjualan dengan satu kontrak. Penjual dapat menjual produk mereka melalui Olist Store dan mengirim langsung ke pelanggan menggunakan mitra logistik Olist. Data ini telah di-anonimkan, sehingga tidak mengandung informasi rahasia dan referensi ke perusahaan serta mitra telah diganti dengan nama-nama rumah besar dari Game of Thrones. Oleh karena itu, saya ingin melakukan analisis


## Pertanyaan Bisnis
1. Bagaimana performa penjualan dan revenue perusahaan dalam beberapa bulan terakhir?
2. Kapan terakhir pelanggan melakukan transaksi (***Recency***)?
3. Seberapa sering seorang pelanggan melakukan pembelian dalam beberapa bulan terakhir (***Frequency***)?
4. Berapa banyak uang yang dihabiskan pelanggan dalam beberapa bulan terakhir (***Monetary***)?
5. Bagaimana Persebaran Revenue antar Wilayah, sebutkan 3 wilayah dengan reveneu tertinggi ?

## Tahapan Proyek
Untuk menjawab berbagai pertanyaan bisnis tersebut maka dalam projek ini melalui berbagai tahapan : 
1. Pertanyaan Bisnis
2. Persiapan Environment dan Import Libraries
3. Data Wrangling
4. Data Cleansing
5. Exploratory Data Analysis (EDA)
6. Visualization & Explanatory Analysis
7. Conclusion
8. Membuat dan Mendeploy program menjadi Dashboard. 

## Setup environment
```
conda create --name bad_python python=3.9
conda activate bad_python
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run streamlit.py
```

## Output
https://e-commerce-python.streamlit.app/
