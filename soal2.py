def main():
    total_cost = 0
    products = []

    while True:
        # Input untuk nama barang
        product_name = input("Masukkan Nama Barang (atau ketik 'selesai' untuk menyelesaikan): ")
        if product_name.lower() == 'selesai':
            break

        # Input untuk harga barang
        while True:
            try:
                product_price = float(input("Masukkan Harga Barang: "))
                if product_price < 0:
                    print("Harga Barang tidak boleh negatif. Silakan masukkan lagi.")
                    continue
                break
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")

        # Input untuk jumlah barang
        while True:
            try:
                product_quantity = int(input("Masukkan Jumlah Barang: "))
                if product_quantity < 0:
                    print("Jumlah Barang tidak boleh negatif. Silakan masukkan lagi.")
                    continue
                break
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")

        # Hitung total harga untuk barang ini dan tambahkan ke total keseluruhan
        total_item_cost = product_price * product_quantity
        total_cost += total_item_cost
        products.append((product_name, product_price, product_quantity, total_item_cost))

    # Tampilkan informasi semua barang yang dimasukkan
    print("\nInformasi Barang yang Dimasukkan:")
    for idx, product in enumerate(products):
        print(f"{idx + 1}. Nama Barang: {product[0]}, Harga: {product[1]}, Jumlah: {product[2]}, Total: {product[3]}")
    
    # Tampilkan total harga dari semua barang
    print(f"\nTotal Harga Semua Barang: {total_cost}")

if __name__ == "__main__":
    main()