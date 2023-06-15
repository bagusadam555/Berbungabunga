from d3 import decisionfinal

import pandas as pd

# Membaca file CSV
df = pd.read_csv('C:/Users/ASUS/Documents/GitHub/Berbungabunga/sub3/ujid3.csv')

# Mengecek baris pertama kolom pertama, [baris , kolom]


for i in range(2):
    
    jarak = df.iloc[i, 0]
    heading = df.iloc[i, 1]
    kecepatan = df.iloc[i, 2]
    decisionfinal(jarak, heading, kecepatan)
