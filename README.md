# Database Kemiskinan Kabupaten Kulon Progo

## 📌 Deskripsi
Program ini adalah sistem manajemen data kemiskinan di Kabupaten Kulon Progo. Program ini memungkinkan pengguna untuk menambah, memperbarui, menghapus, menampilkan, serta mengembalikan data yang telah terhapus (restore). Selain itu, terdapat fitur untuk mengecek status kemiskinan dan menampilkan dashboard analisis.

## 🛠️ Fitur Utama
1. **Tambah Data** – Memasukkan data masyarakat baru ke dalam database.
2. **Update Data** – Memperbarui data yang sudah ada.
3. **Hapus Data** – Menghapus data dari database dan menyimpannya di Recycle Bin.
4. **Tampilkan Data** – Menampilkan semua data kemiskinan yang tersimpan.
5. **Kembalikan Data yang Terhapus** – Mengembalikan data dari Recycle Bin ke database utama.
6. **Cek Status Kemiskinan** – Menentukan status kemiskinan berdasarkan kriteria tertentu.
7. **Tampilkan Dashboard** – Menampilkan rangkuman dari data kemiskinan.
8. **Keluar** – Menghentikan program.

## 📦 Instalasi & Penggunaan
### 1. Clone Repository
```bash
git clone https://github.com/Zaraaifa/Capstone-Project-Modul-1
cd Capstone-Project-Modul-1
```

### 2. Install Dependencies
Pastikan Python sudah terinstall, lalu jalankan:
```bash
pip install -r requirements.txt
```

### 3. Jalankan Program
```bash
python main_program.py
```

## 🏗️ Struktur Folder
```
repo-name/
│── main_program.py         # Program utama
│── data/
│   ├── database.json       # File penyimpanan data
│── modules/
│   ├── fungsi_add.py       # Modul tambah data
│   ├── fungsi_cek.py       # Modul cek status kemiskinan data
│   ├── fungsi_confirm.py   # Modul konfirmasi data
│   ├── fungsi_dash.py      # Modul dashboard data
│   ├── fungsi_delete.py    # Modul hapus data
│   ├── fungsi_restore.py   # Modul restore data
│   ├── fungsi_show.py      # Modul tampilan data
│   ├── fungsi_update.py    # Modul update data
│── README.md               # Dokumentasi
```

## ⚡ Teknologi yang Digunakan
- **Python** – Bahasa utama
- **Tabulate** – Untuk menampilkan tabel
- **JSON** – Untuk penyimpanan data
- **Rich** – Untuk tampilan terminal yang lebih interaktif
- **Re** – Untuk memproses teks dan pencocokan pola (regular expressions)
- **Random** – Untuk menghasilkan angka acak

### Format Data
Data disimpan dalam format JSON. Berikut adalah contoh struktur data dalam `database.json`:
```json
[
  {
    "ID": "RA07",
    "Nama": "Ramina",
    "Kelurahan": "Hargorejo",
    "Pendapatan": 5000000,
    "Anggota_Keluarga": 2,
    "Pendapatan_Perkapita": 2500000,
    "Status": "Tidak Miskin"
  },
  {
    "ID": "TO12",
    "Nama": "Toni",
    "Kelurahan": "Hargorejo",
    "Pendapatan": 6000000,
    "Anggota_Keluarga": 4,
    "Pendapatan_Perkapita": 500000,
    "Status": "Tidak Miskin"
  }
...
]


## 👨‍💻 Kontributor Abdillah Zaraaifa Al Farisa

## 📄 Lisensi
Proyek ini dilisensikan di bawah Proyek ini dilisensikan di bawah [MIT License](LICENSE).
MIT License - Lihat [LICENSE](LICENSE) untuk detail lebih lanjut.

---
Jika ada pertanyaan atau masukan, silakan ajukan di [GitHub Issues](https://github.com/Zaraaifa/Capstone-Project-Modul-1/issues).

