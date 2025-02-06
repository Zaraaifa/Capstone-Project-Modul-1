##MEMBUAT DAFTAR BELANJA

daftar_belanja = []

def tambah_item():
    item = input("Masukkan nama item yang ingin ditambahkan: ")
    harga = float(input("Masukkan harga barang = "))
    daftar_belanja.append({'item': item, 'harga': harga})
    print(f"{item} telah ditambahkan ke daftar belanja dengan harga {harga}")

def hapus_item(): 
    item_hapus = input("Masukkan nama item yang ingin dihapus: ")
    harga_hapus = float(input("Masukkan harga barang yang ingin dihapus: "))
    for item in daftar_belanja:
        if item['item'] == item_hapus and item['harga'] == harga_hapus:
            daftar_belanja.remove(item)
            print(f"{item_hapus} seharga Rp{harga_hapus} telah dihapus dari daftar belanja")
            return
    print(f"{item_hapus} seharga Rp{harga_hapus} telah dihapus dari daftar belanja")

def tampilkan_daftar():
    if len(daftar_belanja) == 0:
        print("Daftar belanja masih kosong")
    else:
        print("Daftar belanja:")
        total_pengeluaran = 0
        for item in daftar_belanja:
            print(f"- {item['item']} : Rp {item['harga']}")
            total_pengeluaran += item['harga']
        print(f"Jumlah total item: {len(daftar_belanja)} dengan Total Pengeluaran : Rp {total_pengeluaran}")

def menu():
    while True:
        print("\nMenu Daftar Belanja:")
        print("1. Tambah item")
        print("2. Hapus item")
        print("3. Tampilkan daftar belanja")
        print("4. Keluar")
        pilih = input("Pilih menu (1-4) = ")
        if pilih == '1':
            tambah_item()
        elif pilih == '2':
            hapus_item()
        elif pilih == '3':
            tampilkan_daftar()
        elif pilih == '4':
            print("Terima kasih telah menggunakan menu daftar belanja")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

menu()