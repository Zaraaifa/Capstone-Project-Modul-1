data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

from utils.fungsi_show import tampilkan_data
from tabulate import tabulate
from .fungsi_confirm import konfirmasi

import random
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
            print('Data Kelurahan: Hargorejo, Hargowilis, dan Sendangsari')

        text = input(f"Masukkan {perintah} hanya berupa {bentuk}: ").strip()
        
        if perintah in ['Nama Kepala Keluarga','Nama Kepala Keluarga Baru'] and function == 'isalpha':
            if text.replace(" ", "").isalpha():
                return text.title()
            else:
                print(f"Input {perintah} tidak ada dalam daftar. Masukkan kembali ⚠️")
        elif perintah == 'Kelurahan' and function == 'isalpha' and text.isalpha():
            if text.capitalize() in data_kelurahan:
                return text.capitalize()
            else:
                print(f"Input {perintah} tidak ada dalam daftar. Masukkan kembali ⚠️")
                
        elif function == 'isdigit' and text.isdigit():
            return int(text)
        else:
            print(f"Input {perintah} harus berupa {bentuk}. Masukkan kembali⚠️")

def tambah_data(database):
    while True: 
        data = {
            'ID' : '',
            'Nama' : input_data('Nama Kepala Keluarga', 'isalpha', 'huruf', data_kelurahan),
            'Kelurahan' : input_data('Kelurahan', 'isalpha', 'huruf', data_kelurahan),
            'Anggota_Keluarga' : input_data('Jumlah Anggota Keluarga', 'isdigit', 'angka', data_kelurahan),
            'Pendapatan' : input_data('Total Pendapatan Rumah Tangga Bulanan', 'isdigit', 'angka', data_kelurahan)}
        data['ID'] = generate_rand_uniq_number(data['Nama'], database)
        
        pendapatan = int(data['Pendapatan'])
        anggota_keluarga = data['Anggota_Keluarga']
        pendapatan_perkapita = int(pendapatan//anggota_keluarga)  #floor division untuk menghindari desimal
        status = 'Miskin' if pendapatan_perkapita < 416870  else 'Tidak Miskin'

        data['Pendapatan_Perkapita'] = pendapatan_perkapita
        data['Status'] = status

        database.append(data)
        print(f"\nData untuk nama {data['Nama']} berhasil ditambahkan ✅\n")
        print("\nDATA STATUS KEMISKINAN KABUPATEN KULONPROGO 2024/2025\n")
        print(tabulate(database, headers='keys', tablefmt='fancy_grid', stralign='center'))
    
        if not konfirmasi("Apakah ingin menambahkan data lagi? (y/n) "):
            return
            
                
