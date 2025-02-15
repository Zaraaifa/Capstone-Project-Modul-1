def konfirmasi(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["y", "n"]:
            return value in ["y"]
        print("\n\u26A0 Input tidak valid. Masukkan 'y' atau 'n'.")