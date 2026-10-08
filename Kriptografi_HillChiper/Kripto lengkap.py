# Hill Cipher Kripto lengkap
mod = 95

# INPUT MATRIKS KUNCI
K = [
    [1, 3],
    [2, 4],
    [5, 7],
    [6, 8]
]

# LANGKAH 1
# TRANSPOSE
# T = K^T

T = []

for j in range(len(K[0])):
    baris = []
    for i in range(len(K)):
        baris.append(K[i][j])
    T.append(baris)

print("Transpose")
for i in T:
    print(i)

# LANGKAH 2
# TK = T x K

TK = []

for i in range(len(T)):
    baris = []
    for j in range(len(K[0])):
        jumlah = 0
        for k in range(len(K)):
            jumlah += T[i][k] * K[k][j]
        jumlah = jumlah % mod
        baris.append(jumlah)
    TK.append(baris)

print("\nTK")
for i in TK:
    print(i)

# LANGKAH 3
# Determinan

det = (TK[0][0] * TK[1][1]) - (TK[0][1] * TK[1][0])
det = det % mod

print("\nDeterminan =", det)

# LANGKAH 4
# Invers Determinan
# (sesuai jurnal hasilnya 73)

inv_det = 73
print("Invers Determinan =", inv_det)

# LANGKAH 5
# Adjoin

adj = [
    [TK[1][1], -TK[0][1]],
    [-TK[1][0], TK[0][0]]
]

for i in range(2):
    for j in range(2):
        adj[i][j] %= mod

print("\nAdjoin")
for i in adj:
    print(i)

# LANGKAH 6
# Invers TK
# (TK)^-1 = inv_det x adj

invTK = []

for i in range(2):
    baris = []
    for j in range(2):
        nilai = (inv_det * adj[i][j]) % mod
        baris.append(nilai)
    invTK.append(baris)

print("\n(TK)^-1")
for i in invTK:
    print(i)

# LANGKAH 7
# M = (TK)^-1 x T

M = []

for i in range(2):
    baris = []
    for j in range(4):
        jumlah = 0
        for k in range(2):
            jumlah += invTK[i][k] * T[k][j]
        jumlah %= mod
        baris.append(jumlah)
    M.append(baris)

print("\nPseudo Invers")
for i in M:
    print(i)

# LANGKAH 8
# Enkripsi
# C = K x P

P = [17,26,33,26,44,34,26,62,54,52,53,55,81,62]
cipher = []
print("\n===== HASIL ENKRIPSI PER BLOK =====")
nomor = 1

for i in range(0, len(P), 2):
    blok = [P[i], P[i+1]]
    hasil = []
    for r in range(4):
        nilai = (K[r][0] * blok[0] + K[r][1] * blok[1]) % mod
        hasil.append(nilai)
    cipher.append(hasil)
    print("C" + str(nomor), "=", hasil)
    nomor += 1

# LANGKAH 9
# Dekripsi
# P = M x C

plain = []
nomor = 1
for c in cipher:
    hasil = []
    for r in range(2):
        jumlah = 0
        for k in range(4):
            jumlah += M[r][k] * c[k]
        hasil.append(jumlah % mod)
    plain.append(hasil)
    print("P" + str(nomor), "=", hasil)
    nomor += 1

# hasil chipertext

ciphertext = []
for i in range(len(cipher)):
    print("C" + str(i+1), "=", cipher[i])

    for angka in cipher[i]:
        ciphertext.append(angka)

print("\nCiphertext =")
print(ciphertext)

# plaintext hasil

plaintext = []

for i in range(len(plain)):
    print("P" + str(i+1), "=", plain[i])

    for angka in plain[i]:
        plaintext.append(angka)

print("\nPlaintext =")
print(plaintext)