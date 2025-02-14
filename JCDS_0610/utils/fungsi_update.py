from .fungsi_show import tampilkan_data
from .fungsi_cek import cek_kemiskinan
from tabulate import tabulate

data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

def update_data(database):
    while True:
        nama = input("Masukkan nama yang data nya ingin diperbarui: ").capitalize()
        matched_data = [data for data in database if data['Nama'] == nama]
        if not matched_data:
            print("\nNama tidak ditemukan. Masukkan kembali\n")
        for data in database:
            print("Data ditemukan.")
            print(tabulate(matched_data, headers="keys", tablefmt="fancy_grid", stralign="center"))
            try:
                id_pilihan = input("Masukkan ID data yang ingin diubah: ").upper().strip()
                print("Silakan pilih data yang ingin diubah:")
                print("1. Update Pendapatan")
                print("2. Update Anggota Keluarga")
                print("3. Update Kelurahan")
                pilihan = int(input("Pilih opsi yang ingin diubah (1/2/3): "))
                if pilihan == 1:
                    pendapatan_baru = input("Masukkan pendapatan bulanan baru: ")
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
            except ValueError:
                print("ID harus sesuai! masukkan lagi\n")
                return
        print("Nama tidak ditemukan. Masukkan kembali\n")