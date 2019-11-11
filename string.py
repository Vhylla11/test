## menghitung jumlah huruf tertentu dalam kalimat tanpa count()
nama = 'Hari ini Hari tidak sekolah'
#cari huruf 'h'
cari = 'h'
x = nama.upper().replace(cari.upper(),'')
print (x)
jmlcari = len (nama) - len (x)
print(f'jumlah huruf\'{cari}\'ada = {jmlcari}')


### menghitung jumlah kata tertentu tanpa count ()
## jumlah kata 'hari'
nama = 'Hari ini Hari tidak sekolah karena hari Minggu'
cari = 'hari'
x = nama.upper().replace(cari.upper(),'')
print (x)
jmlcari = ( len (nama) - len (x))/ len (cari)
print(f'jumlah kata\'{cari}\'ada = {jmlcari}')