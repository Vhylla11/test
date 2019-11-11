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


### konversi nama hari
days = {
    'senin': 'monday', 'selasa' :  'tuesday', 'rabu' : 'wednesday', 'kamis' : 'thursday', 'jumat' : 'friday', 'sabtu' : 'saturday', 'minggu' : 'sunday'
}
#id = engl
# input('ketik nama hari: ')
# input('Bahasa Inggrisnya minggu = sunday' )

# #cara lain fix
# hari = input('ketik nama hari: ')
# print(f'Bahasa Inggrisnya {hari.upper()} = {days.get(hari.lower())}')

## english = id
print(list(days))
print(list(days.values()))
hari = list(days)
day = list(days.values())
x = input ('ketik nama hari dalam (ENG/ID) :')
if x.lower () in hari :
    enghari = day[hari.index(x.lower())]
    print(f'Bhs Inggris {x.lower()} adalah {enghari}')
else: 
    idDay = hari [day.index(x.lower())]
    print (f'Bhs Indonesia {x.lower()} adalah {idDay}')
