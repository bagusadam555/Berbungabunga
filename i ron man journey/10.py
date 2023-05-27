nama_mahasiswa = ["Mawar", "Melati", "Semuanya", "Indah", "Bunga", "Bintang", "Felix"] #sama dengan variabel cukup 1, sama dengan dobel itu untuk if else
for i in range (7)  :
    IPK = float(input(f"Masukkan IPK kamu {nama_mahasiswa[i]} : "))  #[i] menggabungkan angka range dengan nama mahasiswa # Mengubah input menjadi integer (casting = mengubah string jadi integer atau sebaliknya {int(...)})#integer tidak bisa untuk desimal
    if IPK >= 3.50 :
        print(f"Ciyee {nama_mahasiswa[i]} cumlaude") #f memasukkan variabel di dalam string
    elif 3 <= IPK <  3.50 :
        print(f"selamat {nama_mahasiswa[i]}")
    else:
        print(f"Tetap semangat {nama_mahasiswa[i]}, Anda calon bos di masa depan")
