database = [
    {'ID': 'RM07', 'Nama': 'Ramina', 'Kelurahan': 'Hargorejo', 'Pendapatan': 5000000, 'Anggota_Keluarga': 2, 'Status': 'Tidak Miskin', 'Pendapatan_Perkapita': 2500000},
    {'ID': 'TO12', 'Nama': 'Toni', 'Kelurahan': 'Hargorejo', 'Pendapatan': 6000000, 'Anggota_Keluarga': 4, 'Status': 'Tidak Miskin', 'Pendapatan_Perkapita': 500000},
    {'ID': 'HE72', 'Nama': 'Heru', 'Kelurahan': 'Hargowilis', 'Pendapatan': 4000000, 'Anggota_Keluarga': 4, 'Status': 'Tidak Miskin', 'Pendapatan_Perkapita': 1000000},
    {'ID': 'YA56', 'Nama': 'Yanto', 'Kelurahan': 'Sendangsari', 'Pendapatan': 700000, 'Anggota_Keluarga': 2, 'Status': 'Miskin',  'Pendapatan_Perkapita': 350000},
    {'ID': 'JO23', 'Nama': 'Jono', 'Kelurahan': 'Sendangsari', 'Pendapatan': 800000, 'Anggota_Keluarga': 2, 'Status': 'Miskin',  'Pendapatan_Perkapita': 400000},
    {'ID': 'BU44', 'Nama': 'Budi', 'Kelurahan': 'Hargorejo', 'Pendapatan' : 1500000, 'Anggota_Keluarga' : 2, 'Status' : 'Tidak Miskin', 'Pendapatan_Perkapita' : 750000},
    {'ID': 'AN05', 'Nama': 'Andi', 'Kelurahan': 'Hargowilis', 'Pendapatan' : 2000000, 'Anggota_Keluarga' : 2, 'Status' : 'Tidak Miskin', 'Pendapatan_Perkapita' : 1000000},
    {'ID': 'KI06', 'Nama': 'Kirman', 'Kelurahan': 'Sendangsari', 'Pendapatan' : 3000000, 'Anggota_Keluarga' : 3, 'Status' : 'Tidak Miskin', 'Pendapatan_Perkapita' : 1000000},
    {'ID': 'KA19', 'Nama': 'Karno', 'Kelurahan': 'Hargowilis', 'Pendapatan' : 800000, 'Anggota_Keluarga' : 3, 'Status' : 'Miskin', 'Pendapatan_Perkapita' : 266666}    
]

data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

from utils import fungsi_add as fa, fungsi_update as fu, fungsi_delete as fd, fungsi_show as fs, fungsi_restore as fr, fungsi_cek as fc, fungsi_dash as fo
from tabulate import tabulate

def menu():
    while True:
        print("""\nSelamat Datang di Program Data Kemiskinan Kabupaten Kulon Progo!
        Menu:
        1. Tambah Data
        2. Update Data
        3. Hapus Data
        4. Tampilkan Data
        5. Kembalikan Data yang Terhapus
        6. Cek Status Kemiskinan
        7. Tampilkan dashboard
        8. Keluar
        """)

        try:
            pilihan = int(input("Pilih opsi (1/2/3/4/5/6/7/8): "))
            if pilihan == 1:
                fa.tambah_data(database)
            elif pilihan == 2:
                fu.update_data(database)
            elif pilihan == 3:
                fd.hapus_data(database)
            elif pilihan == 4:
                fs.tampilkan_data(database)
            elif pilihan == 5:
                fr.restore_data(database)
            elif pilihan == 6:
                fc.cek_status(database)
            elif pilihan == 7:
                fo.show_dashboard(database)
            elif pilihan == 8:
                print("Terima kasih! Program selesai.")
                break
            else:
                print("Pilihan tidak valid.\n")
        except ValueError:
            print("Input harus berupa angka. Masukkan kembali.\n")
            continue 

menu()