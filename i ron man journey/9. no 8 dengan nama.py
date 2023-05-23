nama_mahasiswa = ["Mawar", "Melati", "Semuanya", "Indah", "Bunga", "Bintang", "Felix"] #sama dengan variabel cukup 1, sama dengan dobel itu untuk if else
for nama in nama_mahasiswa  :
    IPK = float(input(f"Masukkan IPK kamu {nama} "))  # Mengubah input menjadi integer (casting = mengubah string jadi integer atau sebaliknya {int(...)})
#float untuk desimal
#integer tidak bisa untuk desimal
    if IPK >= 3.50 :
        print(f"Ciyee {nama} cumlaude") #f memasukkan variabel di dalam string
    elif 3 <= IPK <  3.50 :
        print(f"selamat {nama}")
    else:
        print(f"Tetap semangat {nama}, Anda calon bos di masa depan")
