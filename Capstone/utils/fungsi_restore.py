from tabulate import tabulate
recycle_bin = []

def tampilkan_recycle_bin():
    if not recycle_bin:
        print("\nRecycle Bin kosong.\n")
    else:
        print("\nDATA DALAM RECYCLE BIN\n")
        print(tabulate(recycle_bin, headers='keys', tablefmt='fancy_grid', stralign='center'))

def restore_data(database):
    if not recycle_bin:
        print("\n🗑️ Recycle Bin kosong. Tidak ada data untuk dikembalikan.\n")
        return

    tampilkan_recycle_bin()
    
    try:
        id_pilihan = input("Masukkan ID data yang ingin dikembalikan: ").upper().strip()
    except ValueError:
        print("⚠️ID harus sesuai dan tanpa spasi. Masukkan lagi!\n")
        return

    for data in recycle_bin:
        konfirmasi = input(f"Apakah ingin mengembalikan data dengan ID {id_pilihan}? (y/n): ").lower()
        if konfirmasi == 'y':
            if data['ID'] == id_pilihan:
                database.append(data)  # Kembalikan ke database utama
                recycle_bin.remove(data)  # Hapus dari recycle bin
                print(f"Data dengan ID {id_pilihan} berhasil dikembalikan! ♻️\n")
                return
            else:
                print("ID tidak ditemukan di Recycle Bin.\n")
        elif konfirmasi == 'n':
            print("Data tidak dikembalikan.\n")
        else:
            print("⛔ Pilihan tidak valid. Masukkan hanya y atau n!\n")



        