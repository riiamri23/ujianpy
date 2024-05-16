def main():
    # Input for product name
    product_name = input("Masukkan Nama Barang: ")

    # Input for product price
    while True:
        try:
            product_price = float(input("Masukkan Harga Barang: "))
            if product_price < 0:
                print("Harga Barang tidak boleh negatif. Silakan masukkan lagi.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    # Input for product quantity
    while True:
        try:
            product_quantity = int(input("Masukkan Jumlah Barang: "))
            if product_quantity < 0:
                print("Jumlah Barang tidak boleh negatif. Silakan masukkan lagi.")
                continue
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    # Display the collected information
    print("\nInformasi Barang:")
    print(f"Nama Barang: {product_name}")
    print(f"Harga Barang: {product_price}")
    print(f"Jumlah Barang: {product_quantity}")
    print(f"Total Harga: {product_price * product_quantity}")

if __name__ == "__main__":
    main()