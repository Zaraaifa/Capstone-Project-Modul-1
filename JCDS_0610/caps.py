##DIPAKAI
from tabulate import tabulate

data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

database = [
    {'Nama': 'Ramina', 'Kelurahan': 'Hargorejo', 'Pendapatan': 5000000, 'Anggota_Keluarga': 2, 'Status': 'Tidak Miskin'},
    {'Nama': 'Toni', 'Kelurahan': 'Hargorejo', 'Pendapatan': 6000000, 'Anggota_Keluarga': 4, 'Status': 'Tidak Miskin'},
    {'Nama': 'Heru', 'Kelurahan': 'Hargowilis', 'Pendapatan': 4000000, 'Anggota_Keluarga': 4, 'Status': 'Tidak Miskin'},
    {'Nama': 'Yanto', 'Kelurahan': 'Sendangsari', 'Pendapatan': 700000, 'Anggota_Keluarga': 2, 'Status': 'Miskin'},
    {'Nama': 'Jono', 'Kelurahan': 'Sendangsari', 'Pendapatan': 800000, 'Anggota_Keluarga': 3, 'Status': 'Miskin'}
]

# Fungsi untuk mengecek status kemiskinan berdasarkan parameter
def cek_kemiskinan(pendapatan, anggota_keluarga):
    batas_pendapatan_kulonprogo = 416870  # Batas pendapatan sesuai dengan batas kemiskinan Kab. Kulon Progo
    return 'Miskin' if (pendapatan/anggota_keluarga) < batas_pendapatan_kulonprogo else 'Tidak Miskin'
    
def input_data(perintah, function, bentuk):
    while True:
        text = input(f"Masukkan {perintah} hanya berupa {bentuk}: ").strip()
        if perintah == 'Kelurahan' and function == 'isalpha' and text.isalpha():
            if text.capitalize() not in data_kelurahan:
                print(f"Input {perintah} tidak ada dalam daftar. Masukkan kembali")
            else:
                return text.capitalize()
        elif perintah != 'Kelurahan' and function == 'isalpha' and text.isalpha():
            return text.capitalize()
        elif function == 'isdigit' and text.isdigit():
            return int(text)
        else:
            print(f"Input {perintah} harus berupa {bentuk}. Masukkan kembali")

def tambah_data(database):
    while True: 
        data = {
            'ID' : '',
            'Nama' : input_data('Nama', 'isalpha', 'huruf'),
            'Kelurahan' : input_data('Kelurahan', 'isalpha', 'huruf'),
            'Anggota_Keluarga' : input_data('Anggota Keluarga', 'isdigit', 'angka'),
            'Pendapatan' : input_data('Pendapatan_Bulanan', 'isdigit', 'angka')}
        data['ID'] = f"{data['Nama'][0:2]}{len(database)+1}"
        
        pendapatan = int(data['Pendapatan'])
        anggota_keluarga = data['Anggota_Keluarga']
        pendapatan_perkapita = int(pendapatan/anggota_keluarga)
        status = 'Miskin' if pendapatan_perkapita < 416870  else 'Tidak Miskin'

        data['Pendapatan_Perkapita'] = pendapatan_perkapita
        data['Status'] = status

        database.append(data)
        print(f"\nData untuk nama {data['Nama']} berhasil ditambahkan\n")
        tampilkan_data(database)
        return data

def update_data(database):
    while True:
        nama = input("Masukkan nama yang data nya ingin diperbarui: ").capitalize()
        for data in database:
            if data['Nama'] == nama:
                print("Data ditemukan.")
                print("1. Update Pendapatan")
                print("2. Update Anggota Keluarga")
                print("3. Update Kelurahan")
                pilihan = int(input("Pilih opsi yang ingin diubah (1/2/3): "))

                if pilihan == 1:
                    pendapatan_baru = input("Masukkan pendapatan baru: ")
                    if pendapatan_baru.isdigit():
                        data['Pendapatan'] = int(pendapatan_baru) 
                    else:
                        print('Input tidak berupa angka. Masukkan lagi')
                elif pilihan == 2:
                    data_keluarga_baru = input("Masukkan data anggota keluarga baru: ")
                    if (data_keluarga_baru).isdigit():
                        data['Anggota_Keluarga'] = int(data_keluarga_baru)
                    else:
                        print('Input tidak berupa angka. Masukkan lagi')
                elif pilihan == 3:
                    kelurahan_baru = input("Masukkan nama kelurahan baru: ").capitalize()
                    if kelurahan_baru in data_kelurahan and kelurahan_baru.isalpha():
                        data['Kelurahan'] = kelurahan_baru
                    else:
                        print('Input tidak berupa huruf. Masukkan lagi')
                else:
                    print("Pilihan tidak valid.")

                data['Status'] = cek_kemiskinan(data['Pendapatan'], data['Anggota_Keluarga'])  # Update status kemiskinan
                print(f"Data {nama} berhasil diperbarui!\n")
                tampilkan_data(database)
                return
        print("Nama tidak ditemukan. Masukkan kembali\n")

# Fungsi untuk menghapus data dari database
def hapus_data(database):
    while True:
        nama = input("Masukkan nama yang ingin dihapus: ")
        for data in database:
            if data['Nama'].capitalize() == nama.capitalize():
                database.remove(data)
                print(f"Data untuk {nama} berhasil dihapus!\n")
                tampilkan_data(database)
                return
        print("Nama tidak ditemukan.\n")

# Fungsi untuk menampilkan data dalam bentuk tabel
def tampilkan_data(database):
    if len(database) == 0:
        print("Tidak ada data yang tersimpan.\n")
        return
    else:
        jmlh_miskin = sum(1 for data in database if data['Status'] == 'Miskin')
        jmlh_tidak_miskin = sum(1 for data in database if data['Status'] == 'Tidak Miskin')
        print("\nDATA STATUS KEMISKINAN KABUPATEN KULONPROGO 2024/2025\n")
        print(tabulate(database, headers='keys', tablefmt='fancy_grid', stralign='center'))
        print(f"""Persentase Miskin = {(jmlh_miskin/len(database)*100):.2f}%
Persentase Tidak Miskin = {(jmlh_tidak_miskin/len(database)*100):.2f}%""")   
    
# Fungsi untuk mengecek status kemiskinan (hanya ditampilkan, tidak disimpan)
def cek_status(database):
    nama = input("Masukkan nama untuk cek status kemiskinan: ")
    for data in database:
        if data['Nama'].capitalize() == nama.capitalize():
            status = cek_kemiskinan(data['Pendapatan'], data['Anggota_Keluarga'])
            print(f"Hasil Cek Status kemiskinan {nama}: {data['Status']}\n")
            return
    print("Nama tidak ditemukan.\n")
    return

# Menu utama program
def menu():
    while True:
        print("""\nSelamat Datang di Program Data Kemiskinan Kabupaten Kulon Progo!
        Menu:
        1. Tambah Data
        2. Update Data
        3. Hapus Data
        4. Tampilkan Data
        5. Cek Status Kemiskinan
        6. Keluar
        """)

        try:
            pilihan = int(input("Pilih opsi (1/2/3/4/5/6): "))
            if pilihan == 1:
                tambah_data(database)
            elif pilihan == 2:
                update_data(database)
            elif pilihan == 3:
                hapus_data(database)
            elif pilihan == 4:
                tampilkan_data(database)
            elif pilihan == 5:
                cek_status(database)
            elif pilihan == 6:
                print("Terima kasih! Program selesai.")
                break
            else:
                print("Pilihan tidak valid.\n")
        except ValueError:
            print("Input harus berupa angka. Masukkan kembali.\n")
            continue 
        
# Menjalankan program
menu()