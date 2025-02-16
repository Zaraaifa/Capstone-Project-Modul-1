from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print

console = Console() # membuat objek console

database = [
    {'ID': 'RA07', 'Nama': 'Ramina', 'Kelurahan': 'Hargorejo', 'Pendapatan': 5000000, 'Anggota_Keluarga': 2, 'Pendapatan_Perkapita': 2500000, 'Status': 'Tidak Miskin'},
    {'ID': 'TO12', 'Nama': 'Toni Sutono', 'Kelurahan': 'Hargorejo', 'Pendapatan': 6000000, 'Anggota_Keluarga': 4, 'Pendapatan_Perkapita': 500000, 'Status': 'Tidak Miskin'},
    {'ID': 'HE72', 'Nama': 'Heru Maryadi', 'Kelurahan': 'Hargowilis', 'Pendapatan': 4000000, 'Anggota_Keluarga': 4, 'Pendapatan_Perkapita': 1000000, 'Status': 'Tidak Miskin'},
    {'ID': 'YA56', 'Nama': 'Yanto', 'Kelurahan': 'Sendangsari', 'Pendapatan': 700000, 'Anggota_Keluarga': 2, 'Pendapatan_Perkapita': 350000, 'Status': 'Miskin' },
    {'ID': 'JO23', 'Nama': 'Jono Harjo', 'Kelurahan': 'Sendangsari', 'Pendapatan': 800000, 'Anggota_Keluarga': 2, 'Pendapatan_Perkapita': 400000, 'Status': 'Miskin' },
    {'ID': 'BU44', 'Nama': 'Budi', 'Kelurahan': 'Hargorejo', 'Pendapatan' : 1500000, 'Anggota_Keluarga' : 2, 'Pendapatan_Perkapita' : 750000, 'Status' : 'Tidak Miskin'},
    {'ID': 'AN05', 'Nama': 'Andi Putra', 'Kelurahan': 'Hargowilis', 'Pendapatan' : 2000000, 'Anggota_Keluarga' : 2, 'Pendapatan_Perkapita' : 1000000, 'Status' : 'Tidak Miskin'},
    {'ID': 'KI06', 'Nama': 'Kirman', 'Kelurahan': 'Sendangsari', 'Pendapatan' : 3000000, 'Anggota_Keluarga' : 3, 'Pendapatan_Perkapita' : 1000000, 'Status' : 'Tidak Miskin'},
    {'ID': 'KA19', 'Nama': 'Karno', 'Kelurahan': 'Hargowilis', 'Pendapatan' : 800000, 'Anggota_Keluarga' : 3, 'Pendapatan_Perkapita' : 266666, 'Status' : 'Miskin'},    
    {'ID': 'BU17', 'Nama': 'Budi Sumanto', 'Kelurahan': 'Sendangsari', 'Pendapatan':2300000, 'Anggota_Keluarga': 5, 'Pendapatan_Perkapita': 460000, 'Status': 'Tidak Miskin'}
]

data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

from utils import fungsi_add as fa, fungsi_update as fu, fungsi_delete as fd, fungsi_show as fs, fungsi_restore as fr, fungsi_cek as fc, fungsi_dash as fo
from tabulate import tabulate

def menu():
    """
    Fungsi untuk menampilkan menu utama program. Fungsi ini akan terus berjalan
    hingga pengguna memilih opsi 8 (Keluar).

    Menu yang tersedia adalah:
        1. Tambah Data
        2. Update Data
        3. Hapus Data
        4. Tampilkan Data
        5. Kembalikan Data yang Terhapus
        6. Cek Status Kemiskinan
        7. Tampilkan Dashboard
        8. Keluar

    Jika pengguna memilih opsi yang tidak valid, maka program akan menampilkan
    pesan kesalahan dan meminta input kembali.

    :return: None
    """
    while True:
        header = "[bold green]Selamat Datang di Program Data Kemiskinan Kabupaten Kulon Progo![/bold green]" # tampilan header
        console.print(Panel(header, style="underline", expand=False)) 
        table = Table(show_header=True, header_style="bold blue", style="dim", show_lines=True)
        table.add_column("No", justify="center", style="bold cyan")
        table.add_column("Menu", style="bold")

        menu_items = [
            ("1", "Tambah Data"),
            ("2", "Update Data"),
            ("3", "Hapus Data"),
            ("4", "Tampilkan Data"),
            ("5", "Kembalikan Data yang Terhapus"),
            ("6", "Cek Status Kemiskinan"),
            ("7", "Tampilkan Dashboard"),
            ("8", "Keluar")
        ]

        for item in menu_items:
            table.add_row(item[0], item[1])
        
        console.print(table)

        try:
            pilihan = int(input("Pilih opsi (1-8): "))
            
            if pilihan == 1:
                fa.tambah_data(database)  # menambahkan data
            elif pilihan == 2:
                fu.update_data(database)  # mengupdate data
            elif pilihan == 3:
                fd.hapus_data(database)  # menghapus data
            elif pilihan == 4:  
                fs.tampilkan_data(database)  # menampilkan data
            elif pilihan == 5:  
                fr.restore_data(database)  # mengembalikan data yang terhapus
            elif pilihan == 6:  
                fc.cek_status(database)  # cek status kemiskinan berdasarkan inputan
            elif pilihan == 7:
                fo.show_dashboard(database)  # menampilkan dashboard(report kemiskinan) 
            elif pilihan == 8:
                console.print("\nTerima kasih! Program selesai.")
                break  # keluar dari loop menu()
            else: 
                print("\nPilihan tidak valid. Hanya masukkan 1-8!\n")
        except ValueError:
            print("Input harus berupa angka. Masukkan kembali.\n") 

menu() # untuk menjalankan program utama