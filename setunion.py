# #set/himpunan : no indexing
# #1. no indexing
# #2. duplicate elements not allowed
# #3. set mutable. tapi elemen2nya immutable

# # biar tau berapa yang unik
# z = {1,2,3,1,2,3}
# print(list(set(z))) 
# #tambah elemen di z : z.add('a')
# # atau z.add(('c','d','e'))
# #1
# z = {1,2,3,1,2,3}
# z = list(z)
# print (z[0])

# #2
# a = []
# for i in z :
#         a.append(i)
# print(a)

# #masukin elemen tanpa list kedalam set
# z = {1,2,3,1,2,3}
# z.update('andi')
# z.update ('Andi')
# z.update ([6,7,8])
# z.update({'z','budi'})
# print(z)
# #kalau mau cek budi ada didalam z?
# print('budi' in z)
# #kalau mau hapus jika ada di z
# z.remove ('budi')
# print(z)
# #hapus tapi ga eror jika tidak ada dalam z : z.discard ('deni)
# z.pop() #untuk hapus
# print(z)

# #kalau mau hapus semua elemen
# z.clear() #isi didalam z atau elemen jadi kosong
# print(z)

# #kalau semua terhapus baik isi maupun var
# del z
# print (z)


#latihan himpunan
a = list ('abcde')
b = list ('bcfgh')
print(a)
print(b)

#cara mencari irisan atau A n B = {b,c}
#1.karena dalam bentuk list maka ubah dulu kedalam set karena untuk set ga bisa langsung dari list
#caranya : a = set(a); b = set (b)
#2. cari irisan : print (a.intersection(b)) ; print(b.intersection(a)); print ( a & b); print (b & a)
a = list ('abcde')
b = list ('bcfgh')
print(a)
print(b)
a = set(a)
b = set (b)
print (a.intersection(b))
print(b.intersection(a))
print ( a & b)
print (b & a)

#mencari union
a = list ('abcde')
b = list ('bcfgh')
print(a)
print(b)
a = set(a)
b = set (b)
print (a.union(b))
print(b.union(a))
print ( a | b)
print (b | a)

#selisih himpunan adalah himpunan A yang ga ada di B = A-B
a = list ('abcde')
b = list ('bcfgh')
print(a)
print(b)
a = set(a)
b = set (b)
print (a.difference(b))
print(b.difference(a))
print ( a - b)
print (b - a)

#selsan irisan
a = list ('abcde')
b = list ('bcfgh')
print(a)
print(b)
a = set(a)
b = set (b)
print (a.symmetric_difference(b))
print(b.symmetric_difference(a))
print ( a ^ b)
print (b ^ a)

#kerjakan soal irisan
# P = {1,2,4,7,9,19}
# Q = {5,6,7,9,12,16,17,19}
# R = {3,8,6,19}
# print ( P & Q)
# print (Q & P)
# print (P & Q & R)
 
#soal2
P = {-4,-3,-2,-1,0,1,2,3,4}
Q = {-7,-6,-5,-4,-3,-2,-1,0,1}
R = {-1,0,1,2,3,4,5,6,7}

P = set (P)
Q = set (Q)
R = set (R)

print(P)
print(Q)
print(R)

print ( P| Q)
print ( P| R)
print ( Q| R)

#soal3

#frozenset = set immutable
x = set ([1,2,3])
y = frozenset([1,2,3])
x.remove(2)
#y.add(2)
print(x)
print(y)