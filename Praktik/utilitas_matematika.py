# Praktik 2 - Utilitas Matematika Modular

# Fungsi luas persegi panjang
def luas_persegi_panjang(p, l):
    return p * l


# Fungsi luas segitiga
def luas_segitiga(a, t):
    return 0.5 * a * t


# Fungsi jumlah 1 sampai n
def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


# Fungsi faktorial
def faktorial(n):
    hasil = 1

    for i in range(2, n + 1):
        hasil *= i

    return hasil


# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n===== UTILITAS MATEMATIKA =====")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("0. Keluar")
    print("===============================")


# Program utama
while True:

    tampilkan_menu()

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        try:
            p = float(input("Masukkan panjang: "))
            l = float(input("Masukkan lebar: "))

            luas = luas_persegi_panjang(p, l)

            print("Luas persegi panjang =", luas)

        except ValueError:
            print("Input harus berupa angka!")

    elif pilihan == "2":
        try:
            a = float(input("Masukkan alas: "))
            t = float(input("Masukkan tinggi: "))

            luas = luas_segitiga(a, t)

            print("Luas segitiga =", luas)

        except ValueError:
            print("Input harus berupa angka!")

    elif pilihan == "3":
        try:
            n = int(input("Masukkan n: "))

            if n >= 0:
                hasil = jumlah_n(n)
                print("Jumlah 1 sampai", n, "=", hasil)
            else:
                print("n harus bilangan bulat nonnegatif!")

        except ValueError:
            print("Input harus berupa bilangan bulat!")

    elif pilihan == "4":
        try:
            n = int(input("Masukkan n: "))

            if n >= 0:
                hasil = faktorial(n)
                print("Faktorial dari", n, "=", hasil)
            else:
                print("n harus bilangan bulat nonnegatif!")

        except ValueError:
            print("Input harus berupa bilangan bulat!")

    elif pilihan == "0":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")
 