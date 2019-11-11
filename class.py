# # # # ##buat angka biasa ke romawi dan sebliknya
# # # # ### class adalah cetakan buat unit objek
# # # # class Manusia:
# # # #     def __init__ (self, nama) :
# # # #         self.nama = nama

# # # # objA = Manusia ('Andi')
# # # # print (vars(objA))


# # # # #properti pria
# # # # class Pria(Manusia):
# # # #     def __init__ (self,nama):
# # # #         Manusia.__init__(self,nama)
# # # #         self.gender = 'Laki-laki'

# # # # #properti wanita
# # # # class Wanita(Manusia):
# # # #     def __init__ (self,nama):
# # # #         Manusia.__init__(self,nama)
# # # #         self.gender = 'Wanita'

# # # # #properti mc
# # # # objA = Manusia ('Andi')
# # # # objB = Manusia ('Andi')
# # # # objC = Manusia ('Andi')

# # # # print (vars(objA))
# # # # print (vars(objB))
# # # # print (vars(objC))


# # # #### class yang berhubungan satu dengan yang lain : multilevel inderi teks
# # # # class X :
# # # #     def __init__(self, x) :
# # # #         self.x = x

# # # # class Y (X) :
# # # #     def __init__(self, x, y) :
# # # #         y.__init__(self, x)
# # # #         self.y = y

# # # # class Z (Y) :
# # # #     def __init__(self, x, y, z) :
# # # #         z.__init__(self, x, y)
# # # #         self.z = z

# # # # objA = Z ('Andi','PNS','True')
# # # # print(vars(objA))


# # # ## multiple inheritance
# # # class Karnivora :
# # #     def __init__ (self) :
# # #         self.daging = True
# # #         self.nama = 'Karnivora'

# # # class Herbivora :
# # #     def __init__ (self) :
# # #         self.tumbuhan = True
# # #         self.nama = 'Herbivora'
# # # class Omnivora (Karnivora, Herbivora) :
# # #     def __init__ (self) :
# # #         Karnivora.__init__(self)
# # #         Herbivora.__init__(self)
# # #         self.mcD = True
# # #         self.nama = 'Omnivora'

# # # objA = Omnivora ()
# # # print (vars(objA))
# # # print(Omnivora.__mro__)
        
# # ### waktu sekarang
# # import datetime as dt
# # x = dt.datetime.now ()
# # print (x)

# # # print (x.strftime ('%d')) #tgl
# # # print (x.strftime ('%A')) # hari
# # # print (x.strftime ('%m')) # bln
# # # print (x.strftime ('%B')) # nama bln
# # # print (x.strftime ('%Y')) # tahun

# # # ## untuk waktu sampai menit
# # # print (x.strftime ('%H')) # 24 JAM
# # # print (x.strftime ('%I')) # 12 JAM
# # # print (x.strftime ('%p')) # AM/PM
# # # print (x.strftime ('%M')) #MIN
# # # print (x.strftime ('%S')) # SEC

# # # print (x.strftime ('%c')) 
# # # print (x.strftime ('%x')) 
# # # print (x.strftime ('%X')) 


# # # print (x.strftime (' Hari ini hari %A'))
# # # print (x.strftime (' Sekarang jam %H :%M :%S WIB'))

# # ###buat file python dalamnya ada class/ object dalam bhs indo
# # ## waktu.hari =
# # ## waktu.tanggal =
# # ## waktu.bulan =
# # ## waktu.tahun =
# # ## waktu.jam =
# # ## waktu.menit =
# # ## waktu.detik =




# # from datetime import datetime
# # current = datetime.now()
# # hari = current.day
# # Tanggal = current.date
# # bulan = current.month
# # tahun = current.year
# # jam = current.hour
# # menit = current.minute
# # detik = current.second
# # print("{}/{}/{}/{}/{}/{}/{}".format(hari,Tanggal, bulan, tahun, jam, menit, detik))


# ##cara lain
# import datetime as dt
# x = dt. datetime.now()
# listHari = {
#     'Monday' : 'Senin', 'Tuesday' :
#     'Selasa','Wednesday' : 'Rabu','Thursday' :
#     'Kamis', 'Friday' :'Jumat','Saturday' :
#     'Sabtu', 'Sunday' : 'Minggu'
# }
# class sekarang :
#     def __init__(self) :
#         self.hari = listHari[x.strftime ('%A')]
#         self.tanggal = x.strftime ('%d')
#         self.tahun = x.strftime ('%Y')
#         self.jam = x.strftime ('%H')
#         self.menit = x.strftime ('%M')
#         self.detik = x.strftime ('%S')

# nama = 'Andi'
# waktu=sekarang()

# ### output hasil utk print ada di rabu21.py

# ### import statistic

# import statistics
# x = [1,3,9,6,2,4,7,8,5,5]
# print (statistics.mean(x))
# print (statistics.median(x))
# print (statistics.mode(x))

import statistics

# listHari = {
#     'Monday' : 'Senin', 'Tuesday' :
#     'Selasa','Wednesday' : 'Rabu','Thursday' :
#     'Kamis', 'Friday' :'Jumat','Saturday' :
#     'Sabtu', 'Sunday' : 'Minggu'
# }
# class sekarang :
#     def __init__(self) :
#         self.hari = listHari[x.strftime ('%A')]
#         self.tanggal = x.strftime ('%d')
#         self.tahun = x.strftime ('%Y')
#         self.jam = x.strftime ('%H')
#         self.menit = x.strftime ('%M')
#         self.detik = x.strftime ('%S')

# nama = 'Andi'
# waktu=sekarang()

# x = [1, 2, 3, 4, 5,6,7,4] 
# n = len(x) 
  
# get_sum = sum(x) 
# mean = get_sum / n 
  
# print("Mean adalah: " + str(mean)) 

# n_num = [1, 2, 3, 4, 5] 
# n = len(n_num) 
# n_num.sort() 
  
# if n % 2 == 0: 
#     median1 = n_num[n//2] 
#     median2 = n_num[n//2 - 1] 
#     median = (median1 + median2)/2
# else: 
#     median = n_num[n//2] 
# print("Median is: " + str(median)) 


# n_num = [1, 2, 3, 4, 5, 5] 
# n = len(n_num) 
  
# data = Counter(n_num) 
# get_mode = dict(data) 
# mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
# if len(mode) == n: 
#     get_mode = "No mode found"
# else: 
#     get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
      
# print(get_mode) 

###cara lain pakai modul class
from functools  import reduce
class Statistik :
    def rataRata (self, x) :
        total = reduce (lambda a,b : a+b, x)
        return total / len(x)

    def median( self, x) :
        x.sort()
        if len (x) % 2 != 0 :
            iTengah =[int(len(x)/2)]
        else :
            iTengah = [int(len(x)/2)-1, int (len(x)/2)]
            aTengah = list (map(lambda a : x[a], iTengah))
            total = reduce (lambda x,y : x+y, aTengah)
            return total / len (aTengah)

stat = Statistik ()
print (stat.median ([1,2,3,4,5,6,7,2,3,]))
