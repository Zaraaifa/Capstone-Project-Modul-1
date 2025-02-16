data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

from utils.fungsi_confirm import konfirmasi  #import fungsi konfirmasi
from tabulate import tabulate  #import fungsi tabulate 

import random  #import fungsi random
import re  #import fungsi regex

def generate_rand_uniq_number(nama, database):
    """
    Fungsi untuk generate ID unik yang terdiri dari 2 huruf depan nama dan 2 angka random. ID yang dihasilkan pasti unik dan tidak ada duplikasi di database. Fungsi ini digunakan saat menambah data baru ke database.
    
    Parameters:
    - nama (str): nama yang digunakan untuk mengenerate ID
    - database (list): database yang berisi data kemiskinan
    
    Returns:
    str: ID unik yang dihasilkan
    """
    
    exisiting_ids = [data['ID'] for data in database] #mengambil semua ID dari database
    while True:
        random_number = str(random.randint(1,99)).zfill(2)  #random 1-99 ketika hanya 1 digit ditambahkan 0 didepannya
        id_baru = f"{nama[:2].upper()}{random_number}"
        if id_baru not in exisiting_ids:
            return id_baru  #ID yang dibuat berupa 2 huruf dari kata pertama "Nama" dan 2 angka random

def input_data(perintah, function, bentuk, data_kelurahan):
    """
    Fungsi untuk meminta input data berupa huruf atau angka tergantung parameter function yang diberikan. Fungsi ini digunakan untuk meminta input data nama, kelurahan, anggota keluarga, dan pendapatan bulanan.
    
    Parameters:
    - perintah (str): perintah untuk meminta input data
    - function (str): fungsi yang digunakan untuk memvalidasi input data dapat berupa 'isalpha' atau 'isdigit'
    - bentuk (str): bentuk input data yang diharapkan dapat berupa 'huruf' atau 'angka'
    - data_kelurahan (list): daftar kelurahan yang diizinkan untuk memasukkan data
    
    Returns:
    str or int: input data yang dihasilkan
    """

    while True:
        if perintah == 'Kelurahan':
            print('\nData Kelurahan: Hargorejo, Hargowilis, dan Sendangsari')

        text = input(f"\nMasukkan {perintah} hanya berupa {bentuk}. Tekan '0' jika ingin batal: ").strip()  
        if function == 'isalnum' and text.isalnum():
            return text.upper() # validasi ID dan mengembalikan text ke bentuk uppercase
        elif text == "0":
            print("\nBatal, Kembali ke menu utama... ")
            return None  # kembali ke menu utama
        
        elif perintah in ['Nama Kepala Keluarga','Nama Kepala Keluarga Baru'] and function == 'isalpha':
            if re.fullmatch(r'^[a-zA-Z ]+$', text):  #validasi huruf dan spasi pada input Nama
                return text.title()
        elif perintah == 'Kelurahan' and function == 'isalpha' and text.isalpha():
            if text.capitalize() in data_kelurahan:  
                return text.capitalize()  # validasi huruf pada input Kelurahan dan mengembalikan text ke bentuk capitalize
            else:
                print(f"\nInput {perintah} tidak ada dalam daftar. Masukkan kembali.")
        elif function == 'isdigit' and text.isdigit():
            return int(text)  # validasi angka dan mengembalikan text ke tipe integer

        
        print(f"\nInput {perintah} harus berupa {bentuk}. Masukkan kembali.")

def tambah_data(database):
    """
    Fungsi untuk menambahkan data kemiskinan ke database. Fungsi ini akan meminta input data berupa nama, kelurahan, anggota keluarga, dan pendapatan bulanan. Data yang diinputkan akan di validasi terlebih dahulu untuk memastikan input data berupa huruf atau angka.
    
    Parameters:
    - database (list): database yang berisi data kemiskinan
    
    Returns:
    None
    """
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

        database.append(data)  #menambahkan data ke database
        print(f"\nData untuk nama {data['Nama']} berhasil ditambahkan.\n")
        print("\nDATA STATUS KEMISKINAN KABUPATEN KULONPROGO 2024/2025\n")
        print(tabulate(database, headers='keys', tablefmt='fancy_grid', colalign=("center", "center", "center")))
    
        if not konfirmasi("Apakah ingin menambahkan data lagi? (y/n) "):
            return
            
                
