from tabulate import tabulate
from .fungsi_confirm import konfirmasi
from .fungsi_add import input_data
recycle_bin = []

def tampilkan_recycle_bin():
    if not recycle_bin:
        print("\nRecycle Bin kosong.\n")
    else:
        print("\nDATA DALAM RECYCLE BIN\n")
        print(tabulate(recycle_bin, headers='keys', tablefmt='fancy_grid', stralign='center'))

def restore_data(database):
    if not recycle_bin:
        print("\n\U0001F5D1 Recycle Bin kosong. Tidak ada data untuk dikembalikan.\n")
        return

    tampilkan_recycle_bin()
    
    try:
        id_pilihan = input_data("Nama Kepala Keluarga", "isalnum", "angka")
    except ValueError:
        print("\n\u26A0 ID harus sesuai dan tanpa spasi. Masukkan lagi!\n")
        return

    for data in recycle_bin:
        if konfirmasi(f"Apakah yakin ingin mengembalikan data dengan ID {id_pilihan}? (y/n): ") == 'y':
            if data['ID'] == id_pilihan:
                database.append(data)  # Kembalikan ke database utama
                recycle_bin.remove(data)  # Hapus dari recycle bin
                print(f"\n\u267B Data dengan ID {id_pilihan} berhasil dikembalikan!\n")
                return
            else:
                print("ID tidak ditemukan di Recycle Bin.\n")
        elif konfirmasi == 'n':
            print("Data tidak dikembalikan.\n")
        else:
            print("\n\u26A0 Pilihan tidak valid. Masukkan hanya y atau n!\n")



        