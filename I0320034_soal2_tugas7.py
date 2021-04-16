# Contoh program menggunakan fungsi numerik
# Mengitung nilai mutlak suatu bilangan
print("Menghitung nilai mutlak suatu bilangan")
angka1 = int(input("Masukkan angka : "))
print("a =", angka1)
print("|a| =", abs(angka1))

print("*"*20)

# Membulatkan bilangan
import math
print("Membulatkan bilangan")
a = float(input("Masukkan angka : "))
print("a =", a)

# Pembulatan ke atas
print("Hasil pembulatan ke atas = ", math.ceil(a))

# Pembulatan ke bawah
print("Hasil pembulatan ke bawah = ", math.floor(a))
