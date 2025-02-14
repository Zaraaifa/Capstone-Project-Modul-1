#REPLACE
nama = "zaraa"
replace = nama.replace('r', 'z').replace('a', 'i') #replace 2 huruf berbeda
print(replace)

#MENGHAPUS SPASI
nama2 = "abdillah zaraaifa" 
replace2 = nama2.replace(' ', '') #petik spasi dan petik kosong
print(replace2)

#########################################3

buah = 'jeruk'
if not buah == 'anggur': #harus == agar berbeda dari variabel
    print('buah ini bukan anggur')
else:
    print('coba buah lain')

########################################

umur = input("Masukkan tanggal lahir dengan format dd-mm-yyy = ")
tahun = int(umur.split(sep='-')[2])
batas = 2024 - tahun 
if batas >= 17:
    print('Anda telah cukup umur')
else:
    print('Anda belum cukup umur')
print('Terima Kasih!')