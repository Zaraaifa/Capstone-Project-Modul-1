from .fungsi_cek import cek_kemiskinan
from .fungsi_add import generate_rand_uniq_number, input_data
from .fungsi_confirm import konfirmasi
from tabulate import tabulate

data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

def update_data(database):
    """
    Fungsi untuk mengupdate data di database berdasarkan ID yang dimasukkan oleh pengguna.

    Fungsi ini akan menampilkan data yang sesuai dengan nama yang dimasukkan oleh pengguna. Jika data ditemukan, maka pengguna akan diminta memasukkan ID data yang ingin diubah.
    Jika ID yang dimasukkan sesuai dengan data yang ditemukan, maka pengguna akan diminta memasukkan
    pilihan perubahan (1-4): Update Nama Kepala Keluarga, Update Pendapatan Total Rumah Tangga Bulanan,
    Update Jumlah Anggota Keluarga, atau Update Kelurahan.

    Jika pilihan perubahan sesuai dengan data yang ditemukan, maka data akan diperbarui dan status kemiskinan akan dihitung ulang berdasarkan data yang diperbarui.
    Jika pilihan tidak valid, maka pengguna akan diminta memasukkan pilihan kembali.

    :param database: List of dictionary yang berisi data kemiskinan
    :return: None
    """
    while True:
        print(tabulate(database, headers='keys', tablefmt='fancy_grid', stralign='center'))  # menampilkan data
        nama_cek = input_data('Nama Kepala Keluarga', 'isalpha', 'huruf', data_kelurahan)  # input nama yang ingin diupdate datanya
        if nama_cek is None:
            return None
        
        matched_data = [data for data in database if nama_cek in data['Nama']]  # cek data didalam database
        
        if not matched_data:
            print("\nNama tidak ditemukan. Masukkan kembali\n")
            continue
        
        print("\nData ditemukan ")
        print(tabulate(matched_data, headers="keys", tablefmt="fancy_grid", stralign="center"))  # menampilkan seluruh data yang ditemukan dari inputan
        
        id_pilihan = input("Masukkan ID data yang ingin diubah: ").upper().strip()  # input ID data yang ingin diupdate
        while True: 
            if not id_pilihan.isalnum():
                print("\nData yang dimasukkan harus sesuai. Masukkan lagi.")
            else: 
                break
            
        for data in matched_data:  # Cek data sesuai ID
            if data['ID'] == id_pilihan:
                print("Silakan pilih data yang ingin diubah:")
                print("1. Update Nama Kepala Keluarga")
                print("2. Update Pendapatan Total Rumah Tangga Bulanan")
                print("3. Update Jumlah Anggota Keluarga")
                print("4. Update Kelurahan")

                pilihan = input_data("Opsi Perubahan (1-4)", "isdigit", "angka", data_kelurahan)  # memanggil fungsi input data 
                
                if pilihan == 1:
                    data['Nama'] = input_data("Nama Kepala Keluarga Baru", "isalpha", "huruf", data_kelurahan)
                    data['ID'] = generate_rand_uniq_number(data['Nama'], database)
                    print(f"Nama kepala keluarga diperbarui menjadi {data['Nama']} dengan ID baru: {data['ID']}")
                
                elif pilihan == 2:
                    data['Pendapatan'] = input_data("Total Pendapatan Rumah Tangga Bulanan", "isdigit", "angka", data_kelurahan)
                
                elif pilihan == 3:
                    data['Anggota_Keluarga'] = input_data("Jumlah Anggota Keluarga", "isdigit", "angka", data_kelurahan)
                    if data['Anggota_Keluarga'] > 0:
                        data['Pendapatan_Perkapita'] = data['Pendapatan'] // data['Anggota_Keluarga']
                    else:
                        print("\nMasukkan angka anggota keluarga yang sesuai")
                
                elif pilihan == 4:
                    data['Kelurahan'] = input_data("Kelurahan", "isalpha", "huruf", data_kelurahan)
                
                else:
                    print("\nPilihan tidak valid. Masukkan angka 1-4.")
                    continue  # memasukkan pilihan kembali
                
                data['Status'] = cek_kemiskinan(data['Pendapatan'], data['Anggota_Keluarga'])  # memanggil fungsi cek kemiskinan 
                print(f"Data {data['Nama']} dengan ID baru {id_pilihan} berhasil diperbarui!\n")
                print(tabulate(database, headers='keys', tablefmt='fancy_grid', stralign='center'))
        
            if not konfirmasi("Apakah ingin mengubah data lagi? (y/n) "):  # memanggil fungsi konfirmasi
                return  # Kembali ke menu utama