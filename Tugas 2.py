# Input nama
while True:
    nama = input("Masukan nama anda : ")
    if len(nama) > 0 and len(nama) <= 10:  # nama pendek (max 10 karakter)
        print(f"Halo, {nama}! Lanjut ke program selanjutnya.")
        break
    else:
        print("silahkan coba lagi")

# Input angka untuk tabel perkalian
angka = int(input("Masukkan angka: "))

# Tampilkan tabel perkalian 1-10
for i in range(1, 11):
    print(f"{angka} x {i} = {angka * i}")