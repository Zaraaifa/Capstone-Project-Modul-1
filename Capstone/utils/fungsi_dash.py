from tabulate import tabulate
from .fungsi_confirm import konfirmasi
from rich.console import Console
from rich.table import Table
from rich import print
from rich.prompt import Confirm


console = Console()

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

    summary_table = Table(title="[bold]Rangkuman Data Kemiskinan Kabupaten Kulon Progo 2024/2025", show_header=True, header_style="bold blue", style="dim")
    summary_table.add_column("Keterangan", justify="center", style="bold cyan")
    summary_table.add_column("Nilai", justify="center", style="bold")

    summary_table.add_row("Max Pendapatan", f"Rp {max_pendapatan:,}")
    summary_table.add_row("Min Pendapatan", f"Rp {min_pendapatan:,}")
    summary_table.add_row("Persentase Miskin", f"{persen_miskin:.2f}%")
    summary_table.add_row("Persentase Tidak Miskin", f"{persen_tidak_miskin:.2f}%")

    console.print(summary_table)

    kelurahan_table = Table(title="[bold]Jumlah Masyarakat Terdata di Tiap Kelurahan", show_header=True, header_style="bold", style="dim")
    kelurahan_table.add_column("Kelurahan", style="bold cyan")
    kelurahan_table.add_column("Jumlah", justify="center", style="bold green")

    kelurahan_data = [[kel, jumlah] for kel, jumlah in jumlah_terdata.items()]
    for kel, jumlah in kelurahan_data:
        kelurahan_table.add_row(kel, f"{jumlah}")

    console.print(kelurahan_table)

    if not konfirmasi("Apakah ingin kembali ke menu utama? (y/n) "):
        show_dashboard(database)