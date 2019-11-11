###lamda function : function yang ga punya nama dan hanya satu ekspresion

# x = lambda a : a
# print (x(2))

# def y (a) : ##sama hal dengan yang diatas
#     return a
# print (y(4)) 

# ##contoh lain
# x = lambda a,b,c : a+b+c
# print (x(2,3,4))

# def y (a,b,c) : ##sama hal dengan yang diatas
#     return a+b+c
# print (y(2,3,4)) 

##contoh untuk buat function dalam function
# def myFunction(x) :
#     return lambda a : a ** x

# pangkat2 = myFunction(2) ##jadi yang  merupakan pangkat ad/ kurung  dalam set myfunction
# pangkat3 = myFunction(3)
# pangkat4 = myFunction(2)
# pangkat = myFunction(4)

# print (pangkat3(3))
# print(pangkat2(4))
# print(pangkat(5)) 


###kalau pakai if else untuk lamda
# x = lambda a : True if  a % 2 == 0 else False
# print (x(4))

##lainya if else langsung
# x = lambda a : 'angka genap' if  a % 2 == 0 else 'angka ganjil'
# print (x(4))
# print (x(15))

# # kalau pakai return dengn if dan else
# def y(a):
#     if a % 2 == 0 :
#         return True
#     else :
#         return False
# print (y(3))
# print (y(4))


### map python : eksekusi function tertentu uk setiap elemen variabel yang iterable ( list,map,dll)
# def y(a) :
#     return len(a)
# a = ['andi', 'vhylla','takoy']

# x = map (y,a)
# print (x)
# print(list(x))


##contoh
# x = [2,4,6,8,10]
# def pangkat2(a) :
#     return  a ** 2

# y = map(pangkat2, x)
# print(list(y))

# ##cara lain pakai map
# z = map ( lambda a : a**2,x)
# print (list(z))

# ##cara lain pakai looping
# b =[]
# for i in x :
#     b.append (i ** 2)
# print (b)


### pakai filter
# x = range (11)

# def kurang5(x) :
#     if x < 5 :
#         return False
#     else : 
#         return True

# y = filter (kurang5, x)
# print (list(y))


# ##cara pakai lamda
# z = filter (lambda a : True if a >= 5 else False, x)
# print(list(z))


###cara mengerjakan pangkat pakai map
# x = pow (2, 2)
# y = pow (3, 3)
# print (x)
# print(y)

##kalau pakai map lamda
## z = map (lambda a: pow (2,3)(2,3), x)

### pakai filter untuk lihat angka mana saja yang ada di x dan y
# x = [1,2,3,4,5,99]
# y = [1,2,6,7,8,99]
# z = list(filter( lambda a : a in x,y)) #cara cepat
# print(z)

# ##cara lain
# z = list(filter( lambda x : True if x < 3 else False, x))
# print(z)
# z = list(filter( lambda x :  x < 3 ,x))
# print (z)

# ##latihan
# angka = [1,2,3,4]
## cari cara untuk output : 1 x 2 x 3 x 4 = 64
##jawab pakai looping
# hasil = 1
# for i in angka :
#     hasil *= i
# print (hasil)

## cara pakai functools reduce 
# from functools import reduce
# z = reduce (lambda x,y : x*y, angka)
# print (z)

## kalau pakai import
# kata = ['ini','ibu','budi']
# print (" ".join(kata))

# ##kalau pake reduce
# from functools import reduce
# z = reduce (lambda x,y : x+y, kata)
# print (z)

### filter() in map ()
# angka = [1,2,3,4]
# z = tuple (map(lambda x : x *2,angka))
# print (z)

## kalau mau filter
# angka = [1,2,3,4]
# z = list(map(lambda x : x *2,filter (lambda x : x>3,angka))) ##filter dalam map
# print (z)

# z = list(filter(lambda x : x >3,map (lambda x : x*2,angka))) ##map dalam filter
# print (z)

###latihan
## punya list dari 1-100, pengen olah hanya angka genap saja,
## setiap angka genap kalikan angka 2, 
## semua hasilnya di jumlakan satu sama lain
# x = list(range(1,101))
# print(x)
# ab=list(map (lambda b : b*2,filter(lambda a : a % 2 ==0,x))) #kerja dari kanan
# print (ab)
# from functools import reduce
# z = reduce (lambda a,b : a + b, ab)
# print (z)

# ab =filter(lambda a : a%2 == 0, x)
# print (list(ab))
# c = list(map(lambda a : a*2,ab))z
# print(c)


##soal berikut
## tampilkan bilangan prima 0-100, 2,3,5,7,11,...

def prima(x) :
    if x > 1 :
        if x == 2 :
            return True
        else : 
            for i in range (2, x) :
                if x % i ==0 :return False; break
                else :
                    return True
    else : 
        return False
        return a

z = list(filter(prima, range(101)))
print (prima(100))

##cobain pake lamda function