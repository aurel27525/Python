# ==== ARRAY
# Biasanya kalau pakai variabel biasa
# maka hanya dapat menyimpan 1 data
varA= "Jovano"
varB= "Michella"
varC= "Yvent"

# Kalau pakai array
# maka dapat menyimpan banyak data
arrNama=["Jovano", "Michella", "Yvent"]
#            0          1         2

# Cara print salah satu saja
print(arrNama[1])

# Cara merubah salah satu data saja
arrNama[1]="Irwansyah"
print(arrNama[1])

# Cara mengetahui banyak data
print(len(arrNama))

# Cara menambahkan data
arrNama.append("Grace")
print(arrNama)

# Cara menghapus data
arrNama.pop(2)
print(arrNama)

arrNama.remove("Jovano")
print(arrNama)

# STRING
murid = "Jovano"
print(murid[4])

print()
print()

# Contoh 
A = [4, 7, 2, 9, 5]
print(A[0]+A[1]+A[2]+A[3]+A[4])

temp=0
for x in A:
    print(f"Nilai x: {x}")
    print(f"Nilai Temp Sebelum: {temp}")
    temp=temp+x
    print(f"Nilai Temp Sesudah: {temp}")
    print()
    
print(sum(A))

# Nilai Max
A = [4, 7, 2, 9, 5]
print(min(A))
temp = A[0]
idx = 0
ctr = 0

for x in A:
    if temp<x:
        temp=x
        idx=ctr
    ctr=ctr+1
print(temp)
print(idx)