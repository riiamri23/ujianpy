import pandas as pd

# Data yang diberikan
data = {
    'Nama': ['Andi', 'Rudi', 'Matius'],
    'Alamat': ['Medan', 'Jakarta', 'Papua'],
    'Jurusan': ['Matematika', 'Fisika', 'Teknik Industri']
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame
print("DataFrame:")
print(df)

# Menyimpan DataFrame ke file CSV (opsional)
df.to_csv('data_untuk_soal4.csv', index=False)
print("\nDataFrame telah disimpan ke 'data.csv'")