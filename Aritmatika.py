kakikambing = 4
kakiayam = 2
kakimereka = 32
jiwa = 13

# # #4*k + 2*a = 32
# # #2*k + 2*a = 26
# # #2k = 6
# # #k = 3

nkambing= abs(kakimereka-(kakiayam)*jiwa)/abs(kakikambing-kakiayam)
print(nkambing)


### cara lain
totalhewan= input('ketik total hewan?:')
print(totalhewan)
totalkakihewan= input('ketik total kaki hewan?:')
print(totalkakihewan)
kakiA= input('ketik total jumlah kaki hewan A?:')
print(kakiA)
kakiB= input('ketik total jumlah kaki hewan B?:')
print(kakiB)
JenisHewan= input('hewan A = x, hewan B = y ')
print(JenisHewan)

selisihkaki= (str)(kakiA-kakiB)
nkambing= abs(totalkakihewan-(kakiB*totalhewan))/(selisihkaki)
print(nkambing)


### cara pak lintang
totalhewan= input('ketik total hewan?:')
print(totalhewan)
totalkakihewan= input('ketik total kaki hewan?:')
print(totalkakihewan)
kakiA= input('ketik total jumlah kaki hewan A?:')
print(kakiA)
kakiB= input('ketik total jumlah kaki hewan B?:')
print (kakiB)
JenisHewan= input('hewan A = x, hewan B = y ')
print(JenisHewan)

jmlhewan = 13
jmlkakihewan = 32
jmlkakiayam = 2
jmlkakikambing = 4

#rumus untuk kambing
kambing = (jmlkakihewan - (jmlkakiayam*jmlhewan)) / (jmlkakikambing - jmlkakiayam)
print(kambing)

ayam = (jmlhewan - kambing)
print(ayam)

#rumus untuk ayam
ayam = (jmlkakihewan-(jmlkakikambing*jmlhewan)) / (jmlkakiayam - jmlkakikambing)
print (ayam)