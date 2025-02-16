from tabulate import tabulate 
from .fungsi_confirm import konfirmasi
from .fungsi_add import input_data
data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

def hapus_data(database):
    """
    Fungsi untuk menghapus data dari database.

    Fungsi ini akan terus berjalan hingga pengguna memilih opsi untuk keluar.
    Jika pengguna memilih opsi untuk menghapus data, maka data akan dihapus dari database utama dan dipindahkan ke Recycle Bin. Jika pengguna memilih opsi untuk batal menghapus data, maka data tidak akan dihapus.

    :param database: list of dictionaries yang berisi data dari database
    :return: None
    """

    while True:
        print(tabulate(database, headers='keys', tablefmt='fancy_grid', stralign='center'))
        nama = input("Masukkan nama yang ingin dihapus: ").capitalize()
        matched_data = [data for data in database if nama in data['Nama']]

        if not matched_data:
            print("\nNama tidak ditemukan. Masukkan lagi\n")
            continue

        print("\nData yang ditemukan:")
        print(tabulate(matched_data, headers="keys", tablefmt="fancy_grid", stralign="center"))

        id_pilihan = input_data("ID Data yang ingin dihapus", "isalnum", "angka", data_kelurahan) # memanggil fungsi input_data
        if id_pilihan == "0":
            return
        
        data_ditemukan = False
        for data in matched_data:
            if data['ID'].upper() == id_pilihan:
                if konfirmasi(f"\nApakah yakin ingin menghapus data dengan ID {id_pilihan}? (y/n): "):  # memanggil fungsi konfirmasi
                    from .fungsi_restore import recycle_bin     # import recycle bin di lokal
                    recycle_bin.append(data)  # Pindahkan ke recycle bin
                    database.remove(data)  # Hapus dari database utama
                    print(f"Data dengan ID {id_pilihan} berhasil dihapus dan masuk ke Recycle Bin!\n")
                    data_ditemukan = True
                    break
                else:
                    print("Data batal dihapus.\n")

        else:
            print("\nID tidak ditemukan dalam daftar. Masukkan lagi\n")

        
        if not konfirmasi("Apakah ingin menghapus data lagi? (y/n): "):  # memanggil fungsi konfirmasi
            return