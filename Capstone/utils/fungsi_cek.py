from .fungsi_confirm import konfirmasi
from .fungsi_add import input_data
data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

def cek_kemiskinan(pendapatan, anggota_keluarga):
    batas_pendapatan_kulonprogo = 416870  # Batas pendapatan sesuai dengan batas kemiskinan Kab. Kulon Progo
    return 'Miskin' if (pendapatan/anggota_keluarga) < batas_pendapatan_kulonprogo else 'Tidak Miskin'

def cek_status(database):
    nama = input_data("Nama Kepala Keluarga", "isalpha", "huruf", data_kelurahan).title().strip()
    if nama.replace(" ", "").isalpha():
        for data in database:
            if data['Nama'].capitalize() == nama.capitalize():
                status = cek_kemiskinan(data['Pendapatan'], data['Anggota_Keluarga'])
                print("\n\u2705 Data berhasil ditemukan\n")
                print(f"Hasil Cek Status kemiskinan {nama}: {data['Status']}\n")
                if not konfirmasi("Apakah ingin cek status lain? (y/n)"):
                    print("\n\u21A9 Kembali ke menu utama")
                    return

            elif nama not in data['Nama'].capitalize():
                print("\n\U0001F4E2 Data belum ada di database.")
                if konfirmasi("Apakah ingin menambahkan data ke database? (y/n) "):
                    from fungsi_add import tambah_data
                    tambah_data(database)
                else:
                    return
    
