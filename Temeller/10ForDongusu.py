# for i in range(10): # 0dan10a 1er artarak
#     print(i,end=" ")
# print()
# for i in range(2,10): # 2den10a 1er artarak
#     print(i,end=" ")
# print()
# for i in range(2,10,2): # 0dan10a 2ser artarak
#     print(i,end=" ")
# print()
# for i in range(30,1,-1): # 30dan1e 1er azalarak
#     print(i,end=" ")
# print()
# for i in range(30,0,-3): # 30dan0a 3ser azalarak
#     print(i,end=" ")

'''
    100e kadar olan çiftler
'''

# for i in range(101):
#     if i%2==0:
#         print(i)

'''
kullanıcının girdiği iki sayının obeb ve okek degerlerini bulun.
'''

# s1 = input("Sayi1 :")
# s2 = input("Sayi2 :")
# ebob=1
# if s1.isdigit() and s2.isdigit():
#     s1,s2 = int(s1),int(s2)
#     minSayi = min(s1,s2)
#     for i in range(1,minSayi+1):
#         if s1%i==0 and s2%i==0:
#             ebob=i
#     print("Ebob :",ebob)
#     print("Ekok :",int(s1*s2/ebob))
# else:
#     print("Duzgun giriş yapın !")

'''
    24-> 1,2,3,4,6,8,12,24. 8 tane var. 24 8'e tam bölündüğü için Tau dur. Kullanıcın girdiği 
    deger Tau mudur?
'''
# sayi = input("Sayi giriniz :")
# sayac = 0
# if sayi.isdigit():
#     sayi = int(sayi)
#     for i in range(1,sayi+1):
#         if sayi%i==0:
#             sayac+=1
#     if sayi%sayac==0:
#         print("Taudur ")
#     else:
#         print("Değildir")

'''
28-> 1,2,4,7,14 toplamları 28 ise mukemmel sayıdır.
kullanıcının girdiği sayı mukemmel mı?
'''
# topla=0
# sayi = input("Sayi giriniz :")
# if sayi.isdigit():
#     sayi=int(sayi)
#     for i in range(1,int(sayi/2)+1):
#         if sayi%i==0:
#             topla+=i
#     if topla==sayi:
#         print("Mukemmel")
#     else:
#         print("değğil")

# dizi = [12,312,423,312,123,5,True,False,32,123,12,443,",asd",52,42,34,123]

# for i in range(len(dizi)):
#     if dizi[i]%2==0:
#         print(dizi[i])

# for i in range(len(dizi)):
#     if type(dizi[i])==bool:
#         print(dizi[i])

# for i in range(1,10):
#     if i==3:
#         continue
#     print(i)
#     if i==5:
#         break
# else:
#     print("For-Else")
# print("For bitti")

'''
kullanıcın girdiği sayı asal mıdıR?

'''

# sayi = input("Sayi giriniz :")
# asal = True
# if sayi.isdigit():
#     sayi = int(sayi)
#     for i in range(2,int(sayi/2)+1):
#         if sayi%i==0:
#             asal=False
#             break
#     if asal:
#         print("{} sayisi asaldır ".format(sayi))
#     else:
#         print("{} sayisi asal değildir ".format(sayi))
#
# else:
#     print("UYGUN SAYI GIRMEDINIZ")

# KISAYOL

# sayi = input("Sayi giriniz :")
# if sayi.isdigit():
#     sayi = int(sayi)
#     for i in range(2,int(sayi/2)+1):
#         if sayi%i==0:
#             print("Asal değildir !")
#             break
#     else:
#         print("Asaldır")
#
# else:
#     print("UYGUN SAYI GIRMEDINIZ")
# sayac=0
# for i in range(1,11):
#     for j in range(1,11):
#         print("{}x{}={}".format(i,j,i*j))


# for i in range(3,1000000):
#     sonuc = 0
#     for j in range(1,int(i/2)+1):
#         if i%j==0:
#             sonuc+=j
#     if i==sonuc:
#         print(i)
'''
10000e kadar olan Tau sayılarını
10000e kadar olan asal sayıları yazdırın.
'''

# for i in range(1,1000000):
#     sayac = 0
#     for j in range(1,i+1):
#         if i%j==0:
#             sayac+=1
#     if i%sayac==0:
#         print(i)

# for i in range(2,10001):
#     asal = True
#     for j in range(2,int(i/2)+1):
#         if i%j==0:
#             asal=False
#             break
#     if asal:
#         print(i)

# for j in range(2,100000):
#     j = str(j)
#     toplam = 0
#     for i in range(len(j)):
#         toplam += int(j[i]) ** len(j)
#     if toplam==int(j):
#         print(j,len(j))

liste = [12,31,23,645,63,45,234,123,12,312,453,46,34]
# for i in range(len(liste)):
#     print(liste[i])

# ad = "adqweqads"
# for item in liste:
#     print(item)

taban = input("Taban giriniz :")
us = input("Üs giriniz :")
toplam =0
if taban.isdigit() and us.isdigit():
    us,taban = int(us),int(taban)
    sonuc = taban**us

    for item in str(sonuc):
        toplam+=int(item)
    print(toplam)