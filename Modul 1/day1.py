#SOAL NOMOR 1
nama = input("Masukkan nama Anda = ")
kode_A = nama[-3:]
kode_B = nama[0:2]
print(f"Halo {nama}! Ini adalah kode Anda \'{kode_A+kode_B}\'")

print('-----------------')

#SOAL NOMOR 2
# Buat input yang memiliki prompt "Masukkan bulan lahir anda"
# Hasil input disimpan dalam variabel
#hitung jumlah huruf dari bulan yang dimasukkan
#print "panjang huruf dari bulan lahir anda adalah {jumlah}"
# contoh: inputnya adalah "juni" output nya "panjang huruf dari bulan lahir anda adalah 4"

bulan = input(f"Masukkan bulan lahir Anda =")
jmlh = len(bulan)
print(f"Panjang huruf dari bulan lahir anda adalah '{jmlh}'")

print("-------------")

#SOAL NOMOR 3
#Buat input dengan prompt: "Masukkan nama panjag anda"
#ambil kata kedua dari nama lengkap
#hitung jumlah huruf kata kedua
#print "Panjang huruf kata kedua adalah {panjang kata}"
nama = input("Masukkan nama panjang Anda = ")
kata = nama.split()[1]
nama_kedua = len(kata)
print(f"Panjang huruf kata kedua Anda adalah '{nama_kedua}'")

print("-------------")

#SOAL NOMOR 4
kota = input("Masukkan kota asal Anda = ")
sebelah = input("Masukkan kota asal sebelah Anda = ")
lain = input("Masukkan kota asal lain lagi = ")
kode_kota = kota[0:3].upper()
print(f"Kota asal sebelah Anda adalah '{sebelah}' dengan kode kotanya adalah '{kode_kota}'")

print("-------------")

#SOAL NOMOR 5
nama = input("Masukkan nama Anda = ")
nama_sebelah = input("Masukkan nama sebelah Anda = ")
nama_lain = input("Masukkan nama lain lagi = ")
huruf = input("Masukkan satu huruf = ")
gabungan = nama + nama_sebelah + nama_lain
kode = huruf in gabungan
print(kode)