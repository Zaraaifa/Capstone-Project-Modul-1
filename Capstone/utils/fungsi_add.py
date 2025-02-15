data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

from utils.fungsi_confirm import konfirmasi
from tabulate import tabulate

import random
import re

def generate_rand_uniq_number(nama, database):
    exisiting_ids = [data['ID'] for data in database]
    while True:
        random_number = str(random.randint(1,99)).zfill(2)  #random 1-99 ketika hanya 1 digit ditambahkan 0 didepannya
        id_baru = f"{nama[:2].upper()}{random_number}"
        if id_baru not in exisiting_ids:
            return id_baru

def input_data(perintah, function, bentuk, data_kelurahan):
    while True:
        if perintah == 'Kelurahan':
            print('\nData Kelurahan: Hargorejo, Hargowilis, dan Sendangsari')

        text = input(f"\nMasukkan {perintah} hanya berupa {bentuk}. Tekan '0' jika ingin batal: ").strip()
        
        if text == "0":
            print("\n\u21A9 Batal, Kembali ke menu utama ")
            return None
        
        elif perintah in ['Nama Kepala Keluarga','Nama Kepala Keluarga Baru'] and function == 'isalpha':
            if re.fullmatch(r'^[a-zA-Z ]+$', text):
                return text.title()
        elif perintah == 'Kelurahan' and function == 'isalpha' and text.isalpha():
            if text.capitalize() in data_kelurahan:
                return text.capitalize()
            else:
                print(f"\n\u26A0 Input {perintah} tidak ada dalam daftar. Masukkan kembali.")
        elif function == 'isdigit' and text.isdigit():
            return int(text)
        
        print(f"\n\u26A0 Input {perintah} harus berupa {bentuk}. Masukkan kembali.")

def tambah_data(database):
    while True: 
        nama = input_data('Nama Kepala Keluarga', 'isalpha', 'huruf', data_kelurahan)
        if nama is None:
            return

        kelurahan = input_data('Kelurahan', 'isalpha', 'huruf', data_kelurahan)
        if kelurahan is None:
            return

        anggota_keluarga = input_data('Jumlah Anggota Keluarga', 'isdigit', 'angka', data_kelurahan)
        if anggota_keluarga is None:
            return

        pendapatan = input_data('Total Pendapatan Rumah Tangga Bulanan', 'isdigit', 'angka', data_kelurahan)
        if pendapatan is None:
            return

        data = {
            'ID' : generate_rand_uniq_number(nama, database),
            'Nama' : nama,
            'Kelurahan' : kelurahan,
            'Anggota_Keluarga' : anggota_keluarga,
            'Pendapatan' : pendapatan
        }
        
        pendapatan = int(data['Pendapatan'])
        anggota_keluarga = data['Anggota_Keluarga']
        pendapatan_perkapita = int(pendapatan//anggota_keluarga)  #floor division untuk menghindari desimal
        status = 'Miskin' if pendapatan_perkapita < 416870  else 'Tidak Miskin'

        data['Pendapatan_Perkapita'] = pendapatan_perkapita
        data['Status'] = status

        database.append(data)
        print(f"\n\u2705 Data untuk nama {data['Nama']} berhasil ditambahkan.\n")
        print("\nDATA STATUS KEMISKINAN KABUPATEN KULONPROGO 2024/2025\n")
        print(tabulate(database, headers='keys', tablefmt='fancy_grid', colalign=("center", "center", "center")))
    
        if not konfirmasi("Apakah ingin menambahkan data lagi? (y/n) "):
            return
            
                
