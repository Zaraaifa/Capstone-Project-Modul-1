from .fungsi_confirm import konfirmasi  #
from .fungsi_add import input_data
data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']

def cek_kemiskinan(pendapatan, anggota_keluarga):
    """
    Cek status kemiskinan berdasarkan pendapatan bulanan dan jumlah anggota keluarga.

    Parameters:
    - Pendapatan bulanan.
    - Jumlah anggota keluarga.

    Returns;
    Status kemiskinan, "Miskin" jika pendapatan perkapita kurang dari 416870 dan "Tidak Miskin" jika sebaliknya.
    """

    batas_pendapatan_kulonprogo = 416870  # Batas pendapatan sesuai dengan batas kemiskinan Kab. Kulon Progo
    return 'Miskin' if (pendapatan/anggota_keluarga) < batas_pendapatan_kulonprogo else 'Tidak Miskin'  # Jika pendapatan perkapita kurang dari batas kemiskinan, maka status kemiskinan adalah "Miskin", jika sebaliknya maka status kemiskinan adalah "Tidak Miskin"

def cek_status(database):
    """
    Cek status kemiskinan berdasarkan nama kepala keluarga

    Parameters:
    - database (list): List of dictionaries yang berisi data

    Returns:
    None
    """
    while True:
        nama = input_data("Nama Kepala Keluarga", "isalpha", "huruf", data_kelurahan)
        if nama is None:
            return #jika input data bernilai None maka akan kembali ke menu utama

        found_data = []  #untuk mengecek apakah nama ditemukan atau tidak

        for data in database:
            if nama.capitalize() in data['Nama'].capitalize():
                found_data.append(data)

        if found_data:  #jika data ditemukan
            print("\nData berhasil ditemukan\n")
            for data in found_data:
                status = cek_kemiskinan(data['Pendapatan'], data['Anggota_Keluarga'])
                print(f"""Hasil Cek Status kemiskinan:
        Nama      : {data['Nama']} 
        Kelurahan : {data['Kelurahan']}
        Status    : {data['Status']}\n""")

        else:
            print("\nData belum ada di database.")
            if konfirmasi("Apakah ingin menambahkan data ke database? (y/n) "):
                from .fungsi_add import tambah_data
                tambah_data(database)

        if not konfirmasi("Apakah ingin cek status lain? (y/n): "):
            print("\nKembali ke menu utama")
            return # kembali ke menu utama

