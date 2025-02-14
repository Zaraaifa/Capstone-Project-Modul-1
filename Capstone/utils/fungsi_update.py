from .fungsi_cek import cek_kemiskinan
from .fungsi_add import generate_rand_uniq_number
from tabulate import tabulate

data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

def update_data(database):
    while True:
        nama = input("Masukkan nama yang data nya ingin diperbarui: ").capitalize()
        matched_data = [data for data in database if data['Nama'] == nama]
        if not matched_data:
            print("\n ❌Nama tidak ditemukan. Masukkan kembali\n")
            continue
        
        print("Data ditemukan ✅")
        print(tabulate(matched_data, headers="keys", tablefmt="fancy_grid", stralign="center"))
        
        id_pilihan = input("Masukkan ID data yang ingin diubah: ").upper().strip()
            
        for data in matched_data:
            if data['ID'] == id_pilihan:
                print("Silakan pilih data yang ingin diubah:")
                print("1. Update Nama Kepala Keluarga")
                print("2. Update Pendapatan Total Rumah Tangga Bulanan")
                print("3. Update Jumlah Anggota Keluarga")
                print("4. Update Kelurahan")

                try:
                    pilihan = int(input("Pilih opsi yang ingin diubah (1/2/3/4): "))

                    if pilihan == 1:
                        while True:
                            nama_baru = input("Masukkan nama kepala keluarga baru: ").capitalize().strip()
                            if nama_baru.isalpha():
                                data['Nama'] = nama_baru
                                data['ID'] = generate_rand_uniq_number(data['Nama'], database)
                                print(f"Nama berhasil diperbarui menjadi {nama_baru} dengan ID baru: {data['ID']}")
                                break
                            else:
                                print('⛔ Input tidak berupa huruf. Masukkan lagi')
                    if pilihan == 2:
                        pendapatan_baru = input("Masukkan total pendapatan rumah tangga bulanan baru: ")
                        if pendapatan_baru.isdigit():
                            data['Pendapatan'] = int(pendapatan_baru) 
                            pendapatan_perkapita = int(data['Pendapatan']//data['Anggota_Keluarga'])
                            data['Pendapatan_Perkapita'] = pendapatan_perkapita 
                        else:
                            print('⛔Input tidak berupa angka. Masukkan lagi')
        
                    elif pilihan == 3:
                        data_keluarga_baru = input("Masukkan data anggota keluarga baru: ")
                        if (data_keluarga_baru).isdigit():
                            data['Anggota_Keluarga'] = int(data_keluarga_baru)
                            if data['Anggota_Keluarga'] > 0:
                                pendapatan_perkapita = int(data['Pendapatan']//data['Anggota_Keluarga'])
                                data['Pendapatan_Perkapita'] = pendapatan_perkapita 
                            else:
                                print("⚠️Masukkan angka pendapatan yang sesuai")
                        else:
                            print('⛔Input tidak berupa angka. Masukkan lagi')
                            continue

                    elif pilihan == 4:
                        kelurahan_baru = input("Masukkan nama kelurahan baru: ").capitalize()
                        if kelurahan_baru in data_kelurahan and kelurahan_baru.isalpha():
                            data['Kelurahan'] = kelurahan_baru
                            break
                        else:
                            print('Input tidak berupa huruf. Masukkan lagi')

                    else:
                        print("Pilihan tidak valid.")

                    data['Status'] = cek_kemiskinan(data['Pendapatan'], data['Anggota_Keluarga'])  # Update status kemiskinan
                    print(f"Data {nama} dengan ID {id_pilihan} berhasil diperbarui!\n")
                    print(tabulate(database, headers='keys', tablefmt='fancy_grid', stralign='center'))
                    return
                
                except ValueError:
                    print("ID harus sesuai! masukkan lagi\n")
                    continue

        konfirmasi = input(f"Apakah ingin mengubah data lagi? (y/n): ").lower()
        if konfirmasi != 'y':
            break