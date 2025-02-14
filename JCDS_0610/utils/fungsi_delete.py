from tabulate import tabulate 
from fungsi_restore import recycle_bin

def hapus_data(database):
    while True:
        nama = input("Masukkan nama yang ingin dihapus: ").capitalize()
        matched_data = [data for data in database if data['Nama'] == nama]

        if not matched_data:
            print("Nama tidak ditemukan.\n")
            return

        # Tampilkan semua data yang cocok agar user bisa memilih ID mana yang ingin dihapus
        print("\nData yang ditemukan:")
        print(tabulate(matched_data, headers="keys", tablefmt="fancy_grid", stralign="center"))

        try:
            id_pilihan = input("Masukkan ID data yang ingin dihapus: ")
        except ValueError:
            print("\nID harus sesuai. Masukkan lagi!\n")
            return
        
        for data in matched_data:
            if data['ID'] == id_pilihan:
                recycle_bin.append(data)  # Pindahkan ke recycle bin
                database.remove(data)  # Hapus dari database utama
                print(f"Data dengan ID {id_pilihan} berhasil dihapus dan masuk ke Recycle Bin!\n")
                import fungsi_show
                return
        
        print("ID tidak ditemukan dalam daftar.\n")


