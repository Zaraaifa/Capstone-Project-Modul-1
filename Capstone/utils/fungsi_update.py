from .fungsi_cek import cek_kemiskinan
from .fungsi_add import generate_rand_uniq_number, input_data
from .fungsi_confirm import konfirmasi
from tabulate import tabulate

data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

def update_data(database):
    while True:
        nama = input_data('Nama Kepala Keluarga', 'isalpha', 'huruf', data_kelurahan)
        matched_data = [data for data in database if data['Nama'] == nama]
        
        if not matched_data:
            print("\n ❌Nama tidak ditemukan. Masukkan kembali\n")
            continue
        
        print("✅ Data ditemukan ")
        print(tabulate(matched_data, headers="keys", tablefmt="fancy_grid", stralign="center"))
        
        id_pilihan = input("Masukkan ID data yang ingin diubah: ").upper().strip()
        while True: 
            if not id_pilihan.isalnum():
                print("\n🚨 Data yang dimasukkan harus sesuai. Masukkan lagi.")
            else: 
                break
            
        for data in matched_data:
            if data['ID'] == id_pilihan:
                print("Silakan pilih data yang ingin diubah:")
                print("1. Update Nama Kepala Keluarga")
                print("2. Update Pendapatan Total Rumah Tangga Bulanan")
                print("3. Update Jumlah Anggota Keluarga")
                print("4. Update Kelurahan")

                pilihan = input_data("Opsi Perubahan (1-4)", "isdigit", "angka", data_kelurahan)
                
                if pilihan == 1:
                    data['Nama'] = input_data("Nama Kepala Keluarga Baru", "isalpha", "huruf", data_kelurahan)
                    data['ID'] = generate_rand_uniq_number(data['Nama'], database)
                    print(f"Nama berhasil diperbarui menjadi {data['Nama']} dengan ID baru: {data['ID']}")
                
                elif pilihan == 2:
                    data['Pendapatan'] = input_data("Total Pendapatan Rumah Tangga Bulanan", "isdigit", "angka", data_kelurahan)
                
                elif pilihan == 3:
                    data['Anggota_Keluarga'] = input_data("Jumlah Anggota Keluarga", "isdigit", "angka", data_kelurahan)
                    if data['Anggota_Keluarga'] > 0:
                        data['Pendapatan_Perkapita'] = data['Pendapatan'] // data['Anggota_Keluarga']
                    else:
                        print("⚠️ Masukkan angka anggota keluarga yang sesuai")
                
                elif pilihan == 4:
                    data['Kelurahan'] = input_data("Kelurahan", "isalpha", "huruf", data_kelurahan)
                
                else:
                    print("⛔ Pilihan tidak valid. Masukkan angka 1-4.")
                    continue
                
                data['Status'] = cek_kemiskinan(data['Pendapatan'], data['Anggota_Keluarga'])
                print(f"Data {nama} dengan ID {id_pilihan} berhasil diperbarui!\n")
                print(tabulate(database, headers='keys', tablefmt='fancy_grid', stralign='center'))
                return
        
        if not konfirmasi("Apakah ingin mengubah data lagi? (y/n) "):
            break
