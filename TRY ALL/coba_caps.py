from tabulate import tabulate

database = [
    {'ID': 'RM01', 'Nama': 'Ramina', 'Kelurahan': 'Hargorejo', 'Pendapatan': 5000000, 'Anggota_Keluarga': 2, 'Status': 'Tidak Miskin', 'Pendapatan_Perkapita': 2500000},
    {'ID': 'TO02', 'Nama': 'Toni', 'Kelurahan': 'Hargorejo', 'Pendapatan': 6000000, 'Anggota_Keluarga': 4, 'Status': 'Tidak Miskin', 'Pendapatan_Perkapita': 500000},
    {'ID': 'HE03', 'Nama': 'Heru', 'Kelurahan': 'Hargowilis', 'Pendapatan': 4000000, 'Anggota_Keluarga': 4, 'Status': 'Tidak Miskin', 'Pendapatan_Perkapita': 1000000},
    {'ID': 'YA04', 'Nama': 'Yanto', 'Kelurahan': 'Sendangsari', 'Pendapatan': 700000, 'Anggota_Keluarga': 2, 'Status': 'Miskin',  'Pendapatan_Perkapita': 350000},
    {'ID': 'JO05', 'Nama': 'Jono', 'Kelurahan': 'Sendangsari', 'Pendapatan': 800000, 'Anggota_Keluarga': 2, 'Status': 'Miskin',  'Pendapatan_Perkapita': 400000},
    {'ID': 'BU06', 'Nama': 'Budi', 'Kelurahan': 'Hargorejo', 'Pendapatan' : 1500000, 'Anggota_Keluarga' : 2, 'Status' : 'Tidak Miskin', 'Pendapatan_Perkapita' : 750000},
    {'ID': 'AN07', 'Nama': 'Andi', 'Kelurahan': 'Hargowilis', 'Pendapatan' : 2000000, 'Anggota_Keluarga' : 2, 'Status' : 'Tidak Miskin', 'Pendapatan_Perkapita' : 1000000},
    {'ID': 'KI08', 'Nama': 'Kirman', 'Kelurahan': 'Sendangsari', 'Pendapatan' : 3000000, 'Anggota_Keluarga' : 3, 'Status' : 'Tidak Miskin', 'Pendapatan_Perkapita' : 1000000},
    {'ID': 'KA09', 'Nama': 'Karno', 'Kelurahan': 'Hargowilis', 'Pendapatan' : 800000, 'Anggota_Keluarga' : 3, 'Status' : 'Miskin', 'Pendapatan_Perkapita' : 266666}    
]

data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

def input_data(perintah, function, bentuk, data_kelurahan):
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
            'Kelurahan' : input_data('Kelurahan', 'isalpha', 'huruf', data_kelurahan),
            'Anggota_Keluarga' : input_data('Anggota Keluarga', 'isdigit', 'angka'),
            'Pendapatan' : input_data('Pendapatan_Bulanan', 'isdigit', 'angka')}
        data['ID'] = f"{data['Nama'][0:2].upper()}{len(database)+1}"
        
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

def cek_kemiskinan(pendapatan, anggota_keluarga):
    batas_pendapatan_kulonprogo = 416870  # Batas pendapatan sesuai dengan batas kemiskinan Kab. Kulon Progo
    return 'Miskin' if (pendapatan/anggota_keluarga) < batas_pendapatan_kulonprogo else 'Tidak Miskin'

def cek_status(database):
    while True: 
        nama = input("Masukkan nama untuk cek status kemiskinan: ")
        for data in database:
            if data['Nama'].capitalize() == nama.capitalize():
                status = cek_kemiskinan(data['Pendapatan'], data['Anggota_Keluarga'])
                print(f"Hasil Cek Status kemiskinan {nama}: {data['Status']}\n")
                return
        print("Nama tidak ditemukan. Masukkan nama lain\n")
recycle_bin = []

def hapus_data(database):
    while True:
        nama = input("Masukkan nama yang ingin dihapus: ").capitalize()
        matched_data = [data for data in database if data['Nama'] == nama]

        if not matched_data:
            print("Nama tidak ditemukan.\n")
            return

        print("\nData yang ditemukan:")
        print(tabulate(matched_data, headers="keys", tablefmt="fancy_grid", stralign="center"))

        try:
            id_pilihan = input("Masukkan ID data yang ingin dihapus: ").upper()
        except ValueError:
            print("ID harus berupa angka!\n")
            return
        
        for data in matched_data:
            if data['ID'] == id_pilihan:
                recycle_bin.append(data)  # Pindahkan ke recycle bin
                database.remove(data)  # Hapus dari database utama
                print(f"Data dengan ID {id_pilihan} berhasil dihapus dan masuk ke Recycle Bin!\n")
                return
        
        print("ID tidak ditemukan dalam daftar.\n")

def tampilkan_recycle_bin():
    if not recycle_bin:
        print("\nRecycle Bin kosong.\n")
    else:
        print("\nDATA DALAM RECYCLE BIN\n")
        print(tabulate(recycle_bin, headers='keys', tablefmt='fancy_grid', stralign='center'))

def restore_data(database):
    if not recycle_bin:
        print("\nRecycle Bin kosong. Tidak ada data untuk dikembalikan.\n")
        return

    tampilkan_recycle_bin()
    
    try:
        id_pilihan = input("Masukkan ID data yang ingin dikembalikan: ").strip().upper()
    except ValueError:
        print("ID tidak sesuai. Masukkan lagi\n")

    for data in recycle_bin:
        if data['ID'] == id_pilihan:
            database.append(data)  # Kembalikan ke database utama
            recycle_bin.remove(data)  # Hapus dari recycle bin
            print(f"Data dengan ID {id_pilihan} berhasil dikembalikan!\n")
            tampilkan_data(database)
            return

    print("ID tidak ditemukan di Recycle Bin.\n")
        
def tampilkan_data(database):
    while True:
        print("\nPilih tampilan data:")
        print("1. Tampilkan berdasarkan data kelurahan")
        print("2. Tampilkan berdasarkan data status kemiskinan")
        print("3. Tampilkan seluruh data (tanpa filter)")
        
        pilihan = input("Masukkan pilihan (1/2/3): ")

        # Inisialisasi variabel filter
        kelurahan = None
        status_kemiskinan = None

        if pilihan == "1":
            print("\nPilih kelurahan yang ingin ditampilkan:")
            print("1. Hargorejo")
            print("2. Hargowilis")
            print("3. Sendangsari")
            
            kelurahan_pilihan = input("Masukkan pilihan (1/2/3): ")

            kelurahan_dict = {
                "1": "Hargorejo",
                "2": "Hargowilis",
                "3": "Sendangsari"
            }

            kelurahan = kelurahan_dict.get(kelurahan_pilihan)

            if kelurahan is None:
                print("Pilihan kelurahan tidak valid.")
                continue  # Kembali ke awal loop

        elif pilihan == "2":
            print("\nPilih status kemiskinan yang ingin ditampilkan:")
            print("M. Miskin")
            print("TM. Tidak Miskin")

            status_pilihan = input("Masukkan pilihan (M/TM): ").upper()

            status_dict = {
                "M": "Miskin",
                "TM": "Tidak Miskin"
            }

            status_kemiskinan = status_dict.get(status_pilihan)

            if status_kemiskinan is None:
                print("Pilihan status tidak valid.")
                continue  # Kembali ke awal loop
        elif pilihan == '3':
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
                return 
        else:
            print("Pilihan tidak valid.")
            continue  # Kembali ke awal loop

        # Filter data sesuai pilihan user
        filtered_data = [
            data for data in database
            if (kelurahan is None or data['Kelurahan'] == kelurahan) and 
               (status_kemiskinan is None or data['Status'] == status_kemiskinan)
        ]
        
        if len(filtered_data) == 0:
            print("Tidak ada data yang sesuai dengan filter yang diberikan.\n")
        else:
            jmlh_miskin = sum(1 for data in filtered_data if data['Status'] == 'Miskin')
            jmlh_tidak_miskin = sum(1 for data in filtered_data if data['Status'] == 'Tidak Miskin')

            print("\nDATA STATUS KEMISKINAN KABUPATEN KULONPROGO 2024/2025\n")
            print(tabulate(filtered_data, headers='keys', tablefmt='fancy_grid', stralign='center'))
            print(f"""Persentase Miskin = {(jmlh_miskin/len(filtered_data)*100):.2f}%
Persentase Tidak Miskin = {(jmlh_tidak_miskin/len(filtered_data)*100):.2f}%""")

        # Tanya user apakah ingin mencari data lagi
        ulang = input("\nApakah ingin menampilkan data lagi? (y/n): ").lower()
        if ulang != "y":
            print("\nKembali ke menu utama\n")
            break

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

def menu():
    while True:
        print("""\nSelamat Datang di Program Data Kemiskinan Kabupaten Kulon Progo!
        Menu:
        1. Tambah Data
        2. Update Data
        3. Hapus Data
        4. Tampilkan Data
        5. Kembalikan Data yang Terhapus
        6. Cek Status Kemiskinan
        7. Keluar
        """)

        try:
            pilihan = int(input("Pilih opsi (1/2/3/4/5/6/7): "))
            if pilihan == 1:
                tambah_data(database)
            elif pilihan == 2:
                update_data(database)
            elif pilihan == 3:
                hapus_data(database)
            elif pilihan == 4:
                tampilkan_data(database)
            elif pilihan == 5:
                restore_data(database)
            elif pilihan == 6:
                cek_status(database)
            elif pilihan == 7:
                print("Terima kasih! Program selesai.")
                break
            else:
                print("Pilihan tidak valid.\n")
        except ValueError:
            print("Input harus berupa angka. Masukkan kembali.\n")
            continue 

menu()        