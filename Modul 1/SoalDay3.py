##SOAL NOMOR 1
list_judul = []
judul1 = input('Masukkan judul buku yang ingin dipinjam = ')
list_judul.append(judul1)

judul2 = input('Masukkan judul buku yang ingin dipinjam = ')
list_judul.append(judul2)

judul3 = input('Masukkan judul buku yang ingin dipinjam = ')
list_judul.append(judul3)

judul4 = input('Masukkan judul buku yang ingin dipinjam = ')
list_judul.append(judul4)


list_judul.sort()
print(list_judul)

buku_balik = input('Apakah ingin mengembalikan buku terakhir? Klik "Enter" untuk konfirmasi')
if buku_balik == '':
    print('Buku berhasil dikembalikan')
else:
    print('Buku belum dikembalikan')
sisa = list_judul.pop()
print(f"Sisa buku yang dipinjam: {list_judul}")

##SOAL NOMOR 2
nilai = []
nilai1 = int(input("Masukkan nilai Anda = "))
nilai.append(nilai1)
nilai2 = int(input("Masukkan nilai Anda = "))
nilai.append(nilai2)
nilai3 = int(input("Masukkan nilai Anda = "))
nilai.append(nilai3)
nilai4 = int(input("Masukkan nilai Anda = "))
nilai.append(nilai4)
nilai.sort()

nilai_max = max(nilai)
nilai_min = min(nilai)
rerata = sum(nilai) / len(nilai)
print(f"Nilai terbesar Anda: {nilai_max} dan Nilai terkecil Anda: {nilai_min} dengan Rata-Rata nilai Anda = {rerata}")

##SOAL NOMOR 3
menu = ['Nasi Goreng', 'Soto Ayam', 'Mie Goreng', 'Ayam Bakar']
print(menu)
pilih = (input('Masukkan menu yang ingin Anda beli = '))
print(f"Makanan {pilih} sudah datang!")

if pilih in menu:
    menu.remove(pilih)
    print(f"Sisa menu yang tersedia = {menu}")
else:
    print('Menu yang Anda pilih tidak tersedia')
