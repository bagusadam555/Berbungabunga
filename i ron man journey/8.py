for i in range (3) :
    IPK = float(input("Masukkan IPK Anda "))  # Mengubah input menjadi integer (casting = mengubah string jadi integer atau sebaliknya {int(...)})
#float untuk desimal
#integer tidak bisa untuk desimal
    if IPK >= 3.50 :
        print("Ciyee cumlaude")
    elif 3 <= IPK <  3.50 :
        print("selamat")
    else:
        print("Tetap semangat, Anda calon bos di masa depan")
