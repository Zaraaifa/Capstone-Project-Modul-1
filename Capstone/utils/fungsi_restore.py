from tabulate import tabulate
from .fungsi_confirm import konfirmasi
from .fungsi_add import input_data

data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

recycle_bin = [] # inisiasi dict untuk menampung data-data yang dihapus

def tampilkan_recycle_bin():
    """
    Menampilkan data-data yang dihapus yang masih ada dalam recycle bin.
    
    Jika recycle bin kosong, maka akan menampilkan pesan "Recycle Bin kosong."
    Jika tidak, maka akan menampilkan table berisi data-data yang dihapus.
    """
    if not recycle_bin:
        print("\nRecycle Bin kosong.\n")
    else:
        print("\nDATA DALAM RECYCLE BIN\n")
        print(tabulate(recycle_bin, headers='keys', tablefmt='fancy_grid', stralign='center'))

def restore_data(database):
    """
    Mengembalikan data yang dihapus dari Recycle Bin ke database utama.

    Jika Recycle Bin kosong, maka akan menampilkan pesan "Recycle Bin kosong." Jika tidak, maka akan menampilkan table berisi data-data yang dihapus dan meminta input ID data yang ingin dikembalikan.
    Jika ID yang diinput tidak ditemukan di Recycle Bin, maka akan menampilkan pesan "ID tidak ditemukan di Recycle Bin."
    Jika ID yang diinput sesuai dan dikonfirmasi, maka akan mengembalikan data tersebut ke database utama dan menghapus dari Recycle Bin.
    Jika dikonfirmasi tidak, maka tidak akan mengembalikan data apapun.
    """
    if not recycle_bin:
        print("\nRecycle Bin kosong. Tidak ada data untuk dikembalikan.\n")
        input("Tekan enter untuk kembali ke menu utama...")
        return #langsung kembali ke menu utama

    while True: 
        tampilkan_recycle_bin()
                
        try:
            id_pilihan = input_data("ID Data yang ingin di restore", "isalnum", "angka", data_kelurahan)
            if id_pilihan == "0":
                return
        except ValueError:
            print("\nID harus sesuai dan tanpa spasi. Masukkan lagi!\n")
            continue # untuk meminta input ulang jika ID tidak sesuai

        data_ditemukan = None  # menandai apakah ID ditemukan di reciycle Bin

        for data in recycle_bin:
            if data['ID'] == id_pilihan:
                data_ditemukan = data
                break

        if data_ditemukan:
            if konfirmasi(f"\nApakah yakin ingin mengembalikan data dengan ID {id_pilihan}? (y/n): "):
                database.append(data_ditemukan)  # Kembalikan ke database utama
                recycle_bin.remove(data_ditemukan)  # Hapus dari recycle bin
                print(f"\nData dengan ID {id_pilihan} berhasil dikembalikan!\n")
            else:
                print("Data tidak dikembalikan.\n")

        else:
            print("ID tidak ditemukan di Recycle Bin. Masukkan ID yang valid!\n")
            continue
    
        if not konfirmasi(f"\nApakah yakin ingin mengembalikan data lain lagi? (y/n): "):
            print("\nKembali ke menu utama...\n")
            break  #keluar loop dan kembali ke menu utama

    return # memastikan fungsi keluar setelah restore selesai dijalankan