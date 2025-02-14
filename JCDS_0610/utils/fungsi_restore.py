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
        print("\nRecycle Bin kosong. Tidak ada data untuk dikembalikan.\n")
        return

    tampilkan_recycle_bin()
    
    try:
        id_pilihan = int(input("Masukkan ID data yang ingin dikembalikan: "))
    except ValueError:
        print("ID harus berupa angka!\n")
        return

    for data in recycle_bin:
        if data['ID'] == id_pilihan:
            database.append(data)  # Kembalikan ke database utama
            recycle_bin.remove(data)  # Hapus dari recycle bin
            print(f"Data dengan ID {id_pilihan} berhasil dikembalikan!\n")
            tampilkan_data(database)
            return

    print("ID tidak ditemukan di Recycle Bin.\n")

def tampilkan_data(database):
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
        