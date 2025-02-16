def konfirmasi(prompt):
    """
    Meminta konfirmasi dari pengguna dengan cara mengulang pertanyaan sampai pengguna memasukkan 'y' atau 'n'.
    
    Parameter:
    prompt (str): Pertanyaan yang akan di tampilkan ke pengguna
    
    Return:
    bool: True jika pengguna memasukkan 'y', False jika pengguna memasukkan 'n'
    """
    while True:
        value = input(prompt).strip().lower()
        if value in ["y", "n"]:
            return value in ["y"]
        print("\nInput tidak valid. Masukkan 'y' atau 'n'.")