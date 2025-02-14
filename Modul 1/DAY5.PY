#SOAL NOMOR 4

harga = {'reguler': 50000,
         'vip' : 100000,
         'vvip' : 150000}

while True:
    try:
        tiket = input("Masukkan jenis tiket (Reguler, VIP, VVIP): ").lower()
        print(f"Jenis tiket yang dipilih : {tiket}")
        if tiket.isalpha():
            if tiket in harga:
                jumlah = int(input("Masukkan jumlah tiket yang akan dibeli : "))
                print(f"Jumlah tiket = {jumlah}")
                member = input("Apakah Anda member? (Ya/Tidak): ").lower()
                if member == 'ya':
                    print("Anda adalah Member, dapat diskon 10%")
                    print(f"Harga tiket {tiket} = Rp {(harga[tiket] * 0.9) * jumlah:,}")
                    break
                elif member == 'tidak':
                    print("Anda bukan member")
                    print(f"Harga tiket {tiket} = Rp {harga[tiket] * jumlah:,}")
                    break
                else:
                    print("Jawaban tidak valid. Coba lagi hanya dengan 'Ya' atau 'Tidak'")
            else:
                print("Jenis tiket tidak valid. Coba lagi")
        else:
            print("Jawaban tidak valid. Coba lagi hanya dengan 'Reguler', 'VIP', atau 'VVIP'")
    except ValueError: 
        print("Masukan Anda tidak valid. Masukkan jenis tiket lagi")
