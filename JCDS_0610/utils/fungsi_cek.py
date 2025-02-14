def cek_kemiskinan(pendapatan, anggota_keluarga):
    batas_pendapatan_kulonprogo = 416870  # Batas pendapatan sesuai dengan batas kemiskinan Kab. Kulon Progo
    return 'Miskin' if (pendapatan/anggota_keluarga) < batas_pendapatan_kulonprogo else 'Tidak Miskin'

def cek_status(database):
    nama = input("Masukkan nama untuk cek status kemiskinan: ")
    for data in database:
        if data['Nama'].capitalize() == nama.capitalize():
            status = cek_kemiskinan(data['Pendapatan'], data['Anggota_Keluarga'])
            print(f"Hasil Cek Status kemiskinan {nama}: {data['Status']}\n")
            return
    print("Nama tidak ditemukan.\n")
    return
