# Definisi list dua dimensi
data = [
    ['Andi', 'Rudi', 'Matius'],
    ['Medan', 'Jakarta', 'Papua'],
    ['Matematika', 'Fisika', 'Teknik Industri']
]

# Menampilkan data secara keseluruhan
print("Data keseluruhan:")
for sublist in data:
    print(sublist)

# Mengakses elemen spesifik
print("\nMengakses elemen spesifik:")
print(f"Nama pertama: {data[0][0]}")
print(f"Kota kedua: {data[1][1]}")
print(f"Jurusan ketiga: {data[2][2]}")

# Menampilkan data secara lebih terstruktur
print("\nData terstruktur:")
for i in range(len(data[0])):
    print(f"Nama: {data[0][i]}, Kota: {data[1][i]}, Jurusan: {data[2][i]}")