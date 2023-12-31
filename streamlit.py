# Import Libraries
import json
import numpy as np
import pandas as pd
import plotly as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plot
from urllib.request import urlopen


# Read dataset
all_dataset = pd.read_pickle("E-Commerce Public Dataset/all_dataset.pkl")

with st.sidebar:
    # Menambahkan logo pribadi
         st.write("Hello 👋")
         st.image("asset/Toni.png")
         st.write("""Saya Toni Andreas Susanto mempersembahkan Dashboard Analysis E-Commerce, sebuah alat yang memudahkan menganalisis
                  data perusahaan E-Commerce dengan visualisasi yang mendalam dan interaktif. Mari menemukan berbagai insight dari perusahaan kami.""")
         st.caption('Copyright © Toni Andreas Susanto 2023')
    
# ---------------------------------------------------- ROW 1 ------------------------------
st.write('# Dashboard Analysis E-Commerce')
st.write("""Analisis ini menggunakan dataset berupa kumpulan data publik dari sebuah e-commerce di Brazil, Olist Store. 
         Dataset ini mencakup informasi dari 100 ribu pesanan yang dilakukan dari tahun 2016 hingga 2018 melalui 
         berbagai platform penjualan di Brazil, https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce. """)

# ---------------------------------------------------- ROW 2 ---------------------------------------------

st.write('### 1: Bagaimana Performa Penjualan dan Revenue Perusahaan dalam Beberapa Bulan Terakhir?')

col3, col4 = st.columns(2) 
# Menyiapkan data
monthly_orders_df = all_dataset.resample(rule='M', on='order_purchase_timestamp').agg({
    "order_id": "nunique",
    "payment_value": "sum"
})
monthly_orders_df.index = monthly_orders_df.index.strftime('%Y-%m')
monthly_orders_df = monthly_orders_df.reset_index()
monthly_orders_df.rename(columns={
    "order_id": "order_count",
    "payment_value": "revenue"
}, inplace=True)

# Ploting Line Chart
line_chart = px.line(data_frame=monthly_orders_df,
        x='order_purchase_timestamp',
        y='order_count',
        markers=True,
        labels={'order_purchase_timestamp': 'Month',
                'order_count': 'Total Order'},
        title="Number of Orders per Month")
col3.plotly_chart(line_chart, use_container_width=True)



line_chart1 = px.line(data_frame=monthly_orders_df,
        x='order_purchase_timestamp',
        y='revenue',
        markers=True,
        labels={'order_purchase_timestamp': 'Month',
                'revenue': 'Total Revenue'},
        title="Total Revenue per Month")
col4.plotly_chart(line_chart1, use_container_width=True)


# ---------------------------------------------------- ROW 3 ---------------------------------------------

# --- Menyiapkan data untuk pertanyaan 2 - 4 ----

rfm_df = all_dataset.groupby(by="customer_id", as_index=False).agg({
    "order_purchase_timestamp": "max", # mengambil tanggal order terakhir
    "order_id": "nunique", # menghitung jumlah order
    "payment_value": "sum" # menghitung jumlah revenue yang dihasilkan
})

rfm_df.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]

# menghitung kapan terakhir pelanggan melakukan transaksi (hari)
rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
recent_date = all_dataset["order_purchase_timestamp"].dt.date.max()
rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)

rfm_df.drop("max_order_timestamp", axis=1, inplace=True)
rfm_df.head()


st.write('### 2: Kapan Terakhir Pelanggan Melakukan Transaksi (***Recency***)?')

# ---------------------- px.bar

plot_recency = px.bar(data_frame=rfm_df.sort_values(by="recency", ascending=True).head(5),
                      x='recency',
                      y='customer_id',
                      labels={'customer_id':'Customer ID',
                              'recency': 'Recency'},
                      title="Best Customer Based on RFM Parameters (customer_id) - Recency")

st.plotly_chart(plot_recency, use_container_width=True)



# ---------------------------------------------------- ROW 4 ---------------------------------------------

st.write('### 3: Seberapa Sering Seorang Pelanggan Melakukan Pembelian dalam Beberapa Bulan Terakhir (***Frequency***)?')

# px.bar
plot_freq = px.bar(data_frame=rfm_df.sort_values(by="frequency", ascending=False).head(5),
                      x='frequency',
                      y='customer_id',
                      labels={'customer_id':'Customer ID',
                              'frequency': 'Frequency'},
                      title="Best Customer Based on RFM Parameters (customer_id) - Frequency")
st.plotly_chart(plot_freq, use_container_width=True)


# ---------------------------------------------------- ROW 5 ---------------------------------------------

st.write('### 4: Berapa Banyak Uang yang Dihabiskan Pelanggan dalam Beberapa Bulan Terakhir (***Monetary***)?')

# px.bar
plot_mone = px.bar(data_frame=rfm_df.sort_values(by="monetary", ascending=False).head(5),
                      x='monetary',
                      y='customer_id',
                      labels={'customer_id':'Customer ID',
                              'monetary': 'Monetary'},
                      title="Best Customer Based on RFM Parameters (customer_id) - Monetary")

st.plotly_chart(plot_mone, use_container_width=True)


# ---------------------------------------------------- ROW 6 ---------------------------------------------

st.write('### 5: Bagaimana Persebaran Revenue antar States ?')

# Persiapan Data
df_map_revenue = all_dataset.groupby('States_Name')['payment_value'].sum()
df_map_revenue = pd.DataFrame(df_map_revenue).reset_index()

response = urlopen('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson')
Brazil = json.load(response) # Javascrip object notation

state_id_map = {}
for feature in Brazil ['features']:
 feature['id'] = feature['properties']['name']
 state_id_map[feature['properties']['sigla']] = feature['id']
 
 
# Plot
plot_map = px.choropleth(
    df_map_revenue, # database
    locations = 'States_Name', #define the limits on the map/geography
    geojson = Brazil, #shape information
    color = "payment_value", #defining the color of the scale through the database
    hover_name = 'States_Name', #the information in the box
    hover_data =["payment_value","States_Name"],
    center={"lat": -6.31957680, "lon": -47.41998438},
     color_continuous_scale="Viridis",
)
plot_map.update_geos(fitbounds = "locations", visible = True)
plot_map.update_layout(margin={"r":1,"t":0,"l":0,"b":0})

st.write("**Distribution Revenue by Every District**")
st.plotly_chart(plot_map)


# ---------------------------------------------------- ROW 8 ------------------------------
st.write("### Conclusion")
            
st.write("""
**Kesimpulan Keseluruhan :**
Sebaiknya perusahaan mesti mengevaluasi lebih lanjut aktivitas bisnis beberapa bulan terakhir, dikarenakan dari berbagai indikator bisnis melalui 
insight 1 hingga 4 terdapat masalah. Insight yang diperoleh terjadi penurunan penjualan & revenue beberapa bulan terakhir maupun penurunan performa RFM. 
Selain itu, dari insight no 5 kita juga dapat memasifkan berbagai strategi pemasaran untuk meningkatkan total revenue berbagai daerah yang kurang berkembang 
dan mempertahankan daerah-daerah yang sudah baik seperti São Paulo dan Minas Gerais.
         """)
