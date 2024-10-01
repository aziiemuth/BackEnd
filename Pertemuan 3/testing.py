def sapa(nama):
    print(f"Halo, {nama}! Selamat datang di Python.")

def hitung_luas_jajargenjang(alas, tinggi):
    luas = alas * tinggi
    return luas

# Menggunakan function sapa
sapa("Athiief")

# Menggunakan function hitung_luas_jajargenjang
alas_jajargenjang = 6
tinggi_jajargenjang = 4
luas = hitung_luas_jajargenjang(alas_jajargenjang, tinggi_jajargenjang)
print(f"Luas jajargenjang dengan alas {alas_jajargenjang} dan tinggi {tinggi_jajargenjang} adalah {luas}")