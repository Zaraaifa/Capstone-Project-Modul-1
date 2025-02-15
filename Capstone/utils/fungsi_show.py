from tabulate import tabulate
from .fungsi_confirm import konfirmasi

data_kelurahan = ['Hargorejo', 'Hargowilis', 'Sendangsari']
def tampilkan_data(database):
    while True:
        print("\nPilih tampilan data:")
        print("1. Tampilkan berdasarkan data Kelurahan")
        print("2. Tampilkan berdasarkan data Status Kemiskinan")
        print("3. Tampilkan seluruh data (tanpa filter)")
        
        pilihan = input("Masukkan pilihan (1/2/3): ")

        # Inisialisasi variabel filter
        kelurahan = None
        status_kemiskinan = None

        if pilihan == "1":
            print("\nPilih kelurahan yang ingin ditampilkan:")
            print("1. Hargorejo")
            print("2. Hargowilis")
            print("3. Sendangsari")
            
            kelurahan_pilihan = int(input("Masukkan pilihan (1/2/3): "))

            kelurahan_dict = {
                1: "Hargorejo",
                2: "Hargowilis",
                3: "Sendangsari"
            }

            kelurahan = kelurahan_dict.get(kelurahan_pilihan)

            if kelurahan is None:
                print("Pilihan kelurahan tidak valid.")

        elif pilihan == "2":
            print("\nPilih status kemiskinan yang ingin ditampilkan:")
            print("M. Miskin")
            print("TM. Tidak Miskin")

            status_pilihan = input("Masukkan pilihan (M/TM): ").upper()

            status_dict = {
                "M": "Miskin",
                "TM": "Tidak Miskin"
            }

            status_kemiskinan = status_dict.get(status_pilihan)

            if status_kemiskinan is None:
                print("Pilihan status tidak valid.")  

        elif pilihan == '3':
            if len(database) == 0:
                print("Tidak ada data yang tersimpan.\n")
                return
            else:
                jmlh_miskin = sum(1 for data in database if data['Status'] == 'Miskin')
                jmlh_tidak_miskin = sum(1 for data in database if data['Status'] == 'Tidak Miskin')
                print("\nDATA STATUS KEMISKINAN KABUPATEN KULONPROGO 2024/2025\n")
                print(tabulate(database, headers='keys', tablefmt='fancy_grid', stralign='center'))
                print(f"""Persentase Miskin = {(jmlh_miskin/len(database)*100):.2f}%
Persentase Tidak Miskin = {(jmlh_tidak_miskin/len(database)*100):.2f}%""")
 
        else:
            print("\n\u26A0 Pilihan tidak valid.")
            continue  # Kembali ke awal loop

        # Filter data 
        filtered_data = [
            data for data in database
            if (kelurahan is None or data['Kelurahan'] == kelurahan) and 
               (status_kemiskinan is None or data['Status'] == status_kemiskinan)
        ]
        
        if len(filtered_data) == 0:
            print("Tidak ada data yang sesuai dengan filter yang diberikan.\n")
        else:
            jmlh_miskin = sum(1 for data in filtered_data if data['Status'] == 'Miskin')
            jmlh_tidak_miskin = sum(1 for data in filtered_data if data['Status'] == 'Tidak Miskin')

            print("\nDATA STATUS KEMISKINAN KABUPATEN KULONPROGO 2024/2025\n")
            print(tabulate(filtered_data, headers='keys', tablefmt='fancy_grid', stralign='center'))
            print(f"""Persentase Miskin = {(jmlh_miskin/len(filtered_data)*100):.2f}%
Persentase Tidak Miskin = {(jmlh_tidak_miskin/len(filtered_data)*100):.2f}%""")

        # Tanya user apakah ingin mencari data lagi
        if not konfirmasi("\n Apakah Anda ingin mencari data lagi? (y/n) "):
            print("\n\u21A9 Kembali ke menu utama\n")
            return

            