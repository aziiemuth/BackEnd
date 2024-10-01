# Program Menghitung Gaji Karyawan dengan Inputan

def hitung_gaji():
    # Input data karyawan
    nama = input("Masukkan nama karyawan: ")
    golongan = input("Masukkan golongan (A/B/C/D): ").upper()
    jam_kerja = int(input("Masukkan jumlah jam kerja: "))

    # Menentukan upah per jam berdasarkan golongan
    if golongan == 'A':
        upah_per_jam = 5000
    elif golongan == 'B':
        upah_per_jam = 7000
    elif golongan == 'C':
        upah_per_jam = 8000
    elif golongan == 'D':
        upah_per_jam = 10000
    else:
        print("Golongan tidak valid.")
        return

    # Menghitung gaji pokok
    gaji_pokok = upah_per_jam * jam_kerja

    # Menghitung uang lembur jika ada
    if jam_kerja > 48:
        jam_lembur = jam_kerja - 48
        uang_lembur = jam_lembur * 4000
    else:
        uang_lembur = 0

    # Total gaji
    total_gaji = gaji_pokok + uang_lembur

    # Output hasil
    print("\n## Program Python Menghitung Gaji Karyawan ##")
    print("=============================================")
    print(f"Nama Karyawan: {nama}")
    print(f"Golongan: {golongan}")
    print(f"Jumlah jam kerja: {jam_kerja}")
    print(f"{nama} menerima upah Rp. {total_gaji} per minggu\n")

# Memanggil fungsi hitung_gaji
hitung_gaji()