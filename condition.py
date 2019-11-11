#buatlah sebuah function 1 parameter untuk menentukan value paramaeter : ganjil atau genap
# def gangen(x) :

#     if x % 2 == 0:
#          print (x, ' tergolong genap' )
#     else:
#         print (x, ' tergolong ganjil' )
# gangen(round(float(input ('masukan angka : '))))

# gangen(20)
# gangen(3) 

### fungsi pangkat dan kuadrat
# # var angka
# x=18
# y=2
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(int(x/y))

# # absolut
# x = -90.321
# print (abs(x))

# #akar pangkat?
# #akar pangkat 2 dari 4 = 4**0.5 atau 1/2
# # akar pangkat 3 dari 7 = 3 **1/3
# print (4**(1/2))
# print (27**(1/3))

# print (max(1,2,3,4,5,6,7,8,9,10))
# print (min(1,2,3,4,5,6,7,8,9,10))
# #pembulatan
# print (round(3.67856))
# print (round(3.67856,2))
# print (round((0.1+0.2),1))

# #pakai library
# import math
# print(math.pi)
# #kalau mau buletin ke bawah
# print(math.floor (3.9))
# print (math.ceil(3.1)) #buletin keatas
# print(math.sqrt(196))

# #faktorial
# #3! = berapa
# print(math.factorial(3))


# ##latihan soal
# # 1-15, bilangan kelipatan 3 = fizz, kelipatan 5 buzz, kel 3 dan 5 = fizzbuzz
# for i in range (1,16):
#     if i %3 == 0 :
#         print ( 'Fizz')
#     elif i%5== 0 :
#         print ('Buzz')
#     elif 3%i%5 ==0 :
#         print ('FizzBuzz')
#     else :
#         print ('YAAHH')

# ###cara bapak
# def fizzbuzz(x):
#     for i in range (1,16):
#         print(i)
#         if i %3 == 0 :
#          print ( 'Fizz')
#         elif i%5== 0 :
#          print ('Buzz')
#         elif i % 3 ==0 and i % 5 ==0 :
#          print ('FizzBuzz')
#         else :
#          print ('YAAHH')

# fizzbuzz(15)

##untuk membalik list
 #1.reverse > x.reverse ()
            # print(x)

 #3. reversed()> print(list(reversed(x)))

 #2. print(x[::-1])

 
##membalik posisi elemen
# x = [1,2,3,4,5,6,7]
# y = ['Andi','Budi','Caca']

# def balikpos(mylist) :
#     hasil =[]
#     for i in range(len(mylist)):
#         hasil.insert (0, mylist[i])
#     return hasil

# print (balikpos(x))
# print (balikpos(y))


##rumus lain
# x = ['Andi','Budi','Caca']
# y = [1,2,3,4,5,6]
# def balikpos(mylist) :
#     hasil =[]
#     for i in range(round(len(mylist)/2)):
#         asli = mylist[i]
#         mylist [i] = mylist[len(mylist)-1-i]
#         mylist[len(mylist)-1-i] = asli 
#     return mylist

# print(balikpos(x))  

# print(balikpos(y))  


###ubah lintang jadi lontong tapi tanpa replace
# def ubahVokal (kata) :
#     output = ''
#     for huruf in kata:
#         if huruf in 'aiueo' :
#             output = output + 'o'
#         else :
#             output = output + huruf
#     return output
# print (ubahVokal('lintang'))
# print (ubahVokal('vhylla'))


##function yang digunakan untuk cek suatu kata itu palindrome atau tdk ( balik atau ga balik artinya ttp sama)
# def cekPalindrome(kata):
#     panjang_kata = len(kata)
#     panjang_kata_array = panjang_kata - 1
#     kata_dibalik = ''
 
#     for p in range(panjang_kata):
#         kata_dibalik += kata[panjang_kata_array - p]
 
#         print('--> "{0}" kalau dibalik menjadi "{1}"'.format(kata, kata_dibalik))
 
#     if kata_dibalik == kata:
#         print('--> Wah, ternyata "{0}" merupakan palindrome'.format(kata))
#     else:        
#         print('--> Hmm... "{0}" bukan merupakan palindrome...'.format(kata))
 
# print(cekPalindrome('malam'))
 
# print(cekPalindrome('makan'))


# kata=input().lower()
# kata2=""
# for i in range(len(kata)-1,-1,-1):
#     kata2+=kata[i]
#     if(kata==kata2):
#         print("palindrom")
#     else:
#         print("bukan palindrom")


### buatlah sebuah function kalau saya jalankan kalimat = ' Hai Aku Lintang ' jadi ' iah uka gnatnil
def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str 
    return str 

s = "Hai Aku Lintang" 
print ("String awal : ",end="") 
print (s) 

print ("String yang sudah dibalik : ",end="") 
print (reverse(s)) 

