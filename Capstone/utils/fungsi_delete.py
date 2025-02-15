from tabulate import tabulate 
from .fungsi_confirm import konfirmasi

def hapus_data(database):
    while True:
        print(tabulate(database, headers='keys', tablefmt='fancy_grid', stralign='center'))
        nama = input("Masukkan nama yang ingin dihapus: ").capitalize()
        matched_data = [data for data in database if nama in data['Nama']]

        if not matched_data:
            print("\n\u26A0 Nama tidak ditemukan. Masukkan lagi\n")
            continue

        print("\nData yang ditemukan:")
        print(tabulate(matched_data, headers="keys", tablefmt="fancy_grid", stralign="center"))

        id_pilihan = input("Masukkan ID data yang ingin dihapus: ").upper()
        data_ditemukan = False
        for data in matched_data:
            if data['ID'].upper() == id_pilihan:
                if konfirmasi(f"\nApakah yakin ingin menghapus data dengan ID {id_pilihan}? (y/n): "):
                    from .fungsi_restore import recycle_bin
                    recycle_bin.append(data)  # Pindahkan ke recycle bin
                    database.remove(data)  # Hapus dari database utama
                    print(f"Data dengan ID {id_pilihan} berhasil dihapus dan masuk ke Recycle Bin!🗑️\n\n")
                    data_ditemukan = True
                    break
                else:
                    print("Data batal dihapus.\n")

        if not data_ditemukan: 
                print("\n\u274C ID tidak ditemukan dalam daftar. Masukkan lagi\n")

        
        if not konfirmasi("Apakah ingin menghapus data lagi? (y/n): "):
            return