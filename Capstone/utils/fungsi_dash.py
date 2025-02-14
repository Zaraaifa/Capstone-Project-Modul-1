from tabulate import tabulate
from .fungsi_confirm import konfirmasi

def calculate_data(database):
    if not database:
        print("Tidak ada data yang tersimpan.")
        return None

    max_pendapatan = max(data['Pendapatan'] for data in database)
    min_pendapatan = min(data['Pendapatan'] for data in database)
    total_data = len(database)
    jmlh_miskin = sum(1 for data in database if data['Status'] == 'Miskin')
    jmlh_tidak_miskin = total_data - jmlh_miskin
    persen_miskin = (jmlh_miskin / total_data) * 100
    persen_tidak_miskin = 100 - persen_miskin

    jumlah_terdata = {}
    for data in database:
        kelurahan = data['Kelurahan']
        jumlah_terdata[kelurahan] = jumlah_terdata.get(kelurahan, 0) + 1

    return max_pendapatan, min_pendapatan, persen_miskin, persen_tidak_miskin, jumlah_terdata

def show_dashboard(database):
    hasil = calculate_data(database)
    if hasil is None:
        return
    
    max_pendapatan, min_pendapatan, persen_miskin, persen_tidak_miskin, jumlah_terdata = calculate_data(database)

    summary_table = [
        ["Max Pendapatan", f"Rp {max_pendapatan:,}"],
        ["Min Pendapatan", f"Rp {min_pendapatan:,}"],
        ["Persentase Miskin", f"{persen_miskin:.2f}%"],
        ["Persentase Tidak Miskin", f"{persen_tidak_miskin:.2f}%"]
    ]

    print("\nRANGKUMAN DATA KEMISKINAN KABUPATEN KULONPROGO 2024/2025")
    print(tabulate(summary_table, tablefmt='fancy_grid', stralign='center'))

    kelurahan_table = [[kel, jumlah] for kel, jumlah in jumlah_terdata.items()]
    print("\nJUMLAH MASYARAKAT TERDATA DI TIAP KELURAHAN\n")
    print(tabulate(kelurahan_table, headers=["Kelurahan", "Jumlah"], tablefmt="fancy_grid"))

    if not konfirmasi("Apakah ingin kembali ke menu utama? (y/n) "):
        show_dashboard(database)