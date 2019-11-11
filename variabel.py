# string
# print ("jum'at")
# print ('jum\'at')
#  #\t itu tab kalau \n berarti enter
# print ('purwadhika\tSchool')
# x = 'hahaha'
# print(x.islower())
# print(x.isupper())

# nama = 'python'
# print (len(nama))

# #contoh lain
# nama ="python oke sekali"
# print  (len(nama))
# print (nama [11:len(nama)]

#string conth lain
#x= 'abcdefghijklmnopqrstuvwxyz'
#kalau mau ngambil karakter ke berapa syntax : print (x[start : stop : step]) atau print (x[0:5:2])
#jika mau cek varibael atau karakter pada variabel string syntax : print ('g' in x)
# berapa jumlah g dalam kata atau var tersebut : (x.count('g'))

#example

kalimat = 'Hari ini Andi tidak kuliah'
cari = 'h'
print (cari.lower() in kalimat.lower())
print(kalimat.lower().count(cari.lower()))
#harus salah satu dibuat lower biar bisa terbaca semua "h" yang ada dalam kalimat, tapi jika hanya cari h atau H maka diganti di tanda "" saja.

# latihan string
text1 = "takoy berkata, 'kemarin kemana ?'"
text2 = "vhylla menjawab,'nonton koy'"
print (text1,text2)

#latihan soal modul1 intro
nama = input("Nama kamu? : ")
umur = input("Umur kamu? : ")
kelamin = input("Kelamin kamu? : ")
pekerjaan = input("Pekerjaan kamu? : ")
print("Nama : " + nama)
print("Umur : " + umur)
print("Kelamin : " + kelamin)
print("Pekerjaan : " + pekerjaan)

#number dan aritmetich
usiaAndi = 40
usiaBudi = 20
print(usiaAndi * usiaBudi)
print(usiaAndi / usiaBudi)
print(usiaAndi + usiaBudi)
print(usiaAndi - usiaBudi)
print(usiaAndi % usiaBudi)
print(usiaBudi ** 2)


# x = [' Andi', 'Budi', 'Caca', 123, True]
# print( x [0]) #memanggil kata yang pertama atau satu elemen
# print (type (x)) #cek type data 
# print( x [len(x)-1]) #melihat komponen terakhir

# #list
# hari = [ ' mon', 'tue', 'wed','thu', 'fri', 'sat', 'sun']
# today = input('hari apa hari ini?')
# print (today)

# #sekarang hari WED, hari apakah 100 hari lagi?
# jumlah = 100
# sisa= jumlah%7
# print ((sisa))
# elemen =hari.index(today)
# print (elemen)

# # 14x7 = 98 , maka 100-98 = 2. 98 hari kedepan masih hari rabu maka jia ditambah dua untuk 100 itu masuk hari jumat.
# #harike = sisa + elemen
# print(hari[sisa + elemen])

#cara lain
# hari = [ ' mon', 'tue', 'wed','thu', 'fri', 'sat', 'sun']
# now ='wed'; brpahari = 100;
# iNow = hari.index (now)
# sisahari= brpahari % len(hari) 
# hariyangdicari = hari [(iNow + sisahari) % 7]
# print(hariyangdicari)

# masukin hari atau tambah : hari.insert(4, 'senin2') jadi akan nyelip berdasarkan permintaan di angka 4.
hari = [ ' mon', 'tue', 'wed','thu', 'fri', 'sat', 'sun']
hari.insert (4, 'senin2')
print (hari)
#hapus elemen : hari.remove ('senin2') untuk elemen string ; print (hari)
#hapus elemen terakhir : hari.pop () untuk pakai indeks : print (hari)
# diurutkan berdasarkan urutan huruf atau konten: hari.sort , untuk kembali ke awal hari.sort (reverse = true)
#  membalik index hari.reserve
# membalik index ada 3 cara :
#1. hari.reverse() 2. hari = hari

x= [1,2,3,4,5,6,7,8,9]
y = x[0::2]. copy()
print(x)
print(y)
print(x+y)
print(y * 2)
#mengkopi elemen y = x[0::2]. copy()  : akan memunculkan angka ganjil, print(y)

usiaAndi = 40;
usiaBudi = 20;
usiaAndi += 3;
# usiaAndi = usiaAndi + 3;
usiaBudi *= 4;
# usiaBudi = usiaBudi * 3;
print(usiaAndi);
print(usiaBudi);

#latihan soal
x = 4
y = 3
z = 2

print [(x+y+z)/x*y]**z