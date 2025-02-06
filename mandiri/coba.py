#SOAL NOMOR 1
dict_menu = {'burger': 50000, 'pizza' : 100000, 'pasta' : 75000}
burger = 50000
pasta = 75000
pizza = 100000

nama = input("Masukkan nama pelanggan : ")
kategori = input("Apakah Anda member restoran? (Ya/Tidak) : ")
print("""Menu yang tersedia hari ini = 
      1. Burger = Rp 50.000
      2. Pasta  = Rp 75.000
      3. Pizza  = Rp 100.000""")
menu = input("Pilih menu yang akan dibeli : ")
harga = int(input("Masukkan total harga makanan yang Anda pilih (tanpa .): "))

dict_pelanggan = {'Nama': nama, 'Kategori' : kategori, 'Menu' : menu}
print(dict_pelanggan)

if kategori == "Ya" or "ya" or "YA":
    if harga >= 150000:
        diskon1 = harga - (harga*(20/100))
        print(f"""
          Total harga makanan = Rp{harga}
          Diskon = 20%
          Total harga setelah diskon = Rp{diskon1}""")
    elif harga < 150000:
        diskon2 = harga - (harga*(10/100))
        print(f"""
          Total harga makanan = Rp{harga}
          Diskon = 20%
          Total harga setelah diskon = Rp{diskon2}""")
elif kategori == "Tidak" or "TIDAK" or "tidak":
    print(f"""
          Diskon = -
          Total harga makanan = Rp{harga}""")
else:
    print("Mohon maaf transaksi Anda gagal")
