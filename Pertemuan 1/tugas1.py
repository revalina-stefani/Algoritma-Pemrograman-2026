# # ==========================================
# TUGAS 1 ALGORITMA DAN PEMROGRAMAN
# Program Menentukan Faktor Persekutuan Terbesar (FPB)
# Menggunakan Algoritma Euclidean
# ==========================================

# Fungsi untuk menentukan FPB dari dua bilangan
def fpb(a, b):
    
    # Perulangan dilakukan selama nilai b tidak sama dengan 0
    while b != 0:
        
        # Algoritma Euclidean menggunakan operasi modulus
        a, b = b, a % b
    
    # Mengembalikan hasil FPB
    return a


# ==========================================
# PROGRAM UTAMA
# ==========================================

print("PROGRAM MENENTUKAN FPB")
print("=======================")

# Data bilangan pertama
bilangan1 = 24
bilangan2 = 36

# Memanggil fungsi fpb
hasil1 = fpb(bilangan1, bilangan2)

# Menampilkan hasil
print("\nFPB dari", bilangan1, "dan", bilangan2, "adalah", hasil1)


# Data bilangan kedua
bilangan3 = 48
bilangan4 = 18

# Memanggil fungsi fpb
hasil2 = fpb(bilangan3, bilangan4)

# Menampilkan hasil
print("FPB dari", bilangan3, "dan", bilangan4, "adalah", hasil2)


# ==========================================
# SELESAI
# ==========================================