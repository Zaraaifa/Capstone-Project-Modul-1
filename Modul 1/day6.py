while True:
    def cek_angka():
        angka = int(input("Masukkan angka: "))
        if angka%2 == 0:
            print(f"Anda Benar. {angka} adalah angka genap")
            return
        else:
            print(f"Anda salah. Masukkan lagi ")

    if cek_angka():
        break