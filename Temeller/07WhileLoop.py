# # while içindeki koşuş doğru olduğu sürece altındaki kodlar çalışır
# i = 0
# while i < 10:
#     print(i)
#     # i = i+1 # i değerini 1 arttırır
#     i += 1  # değerini 1 arttırır
#
#     # i +=1
#     # i -=2
#     # i *=3
#     # i /=4
#
# i = 0
# while i < 10:
#     print("Merhaba" + str(i))
#     i += 1
#
#     # 100'e kadar olan tek sayıları yazdıralım
# i = 0
# while i < 100:
#     i += 1
#     if i % 2 != 0
#         print(i, end=" ")
#
# # 1'den 10'a kadar olan sayıların toplamı
# i = 0
# t = 0
# while i <= 10:
#     t = i + t
#     i += 1
# print(t)
# print((10 * 11) / 2)
#
# # 5! hesabını yapalım
# i = 5
# t = 1
# while i > 0:
#     t = t * i
#     i -= 1
# print(t)
#
# # kullanıcın girdiği değere kadar olan tek sayıların toplamını yazdırın
# # kullanıcı sadece sayı girebilir
# to = 0
# sa = input("Sayı giriniz: ")
# if sa.isdigit():
#     sa = int(sa)
#     while sa >= 0:
#         if sa % 2 != 0:
#             to = sa + to
#         sa -= 1
#     print(to)
# else:
#     print("Hatalı giriş.")
#
# # kullanıcının girdiği sayıya kadar 5 ve 7'ye bölünen kaç atne sayı vardır
# # liste = []
# # sayi = input("Sayi giriniz: ")
# # if sayi.isdigit():
# #     sayi = int(sayi)
# #     while sayi > 0:
# #         if sayi % 5 == 0 and sayi % 7 == 0:
# #             liste.append(sayi)
# #         sayi -= 1
# #     print(len(liste))
# # else:
# #     print("Hatalı giriş.")
#
# i = 1
# sayi = input("Sayi giriniz: ")
# total = 0
# if sayi.isdigit():
#     sayi = int(sayi)
#     while i <= sayi:
#         if i % 5 == 0 and i % 7 == 0:
#             total += 1
#         i += 1
#     print(total)
# else:
#     print("Hata")
#
# # 1 ile 1000 arası üsleri kendi sayılarıyla aynı olan bir toplamın sonucunun son 9 basamağını yazdırın
# i = 1
# liste = []
# toplam = 0
# while i < 1000:
#     toplam = i ** i + toplam
#     i += 1
# toplam = str(toplam)
# liste.append(toplam)
# print(toplam[-9:])
#
# dizi = [1, 23, 145, 13, 123, "123", True, 1.0123, False]
# i = 0
# # while i < len(dizi):
# # print(dizi[i])
# # i += 1
# # bu dizinin içindeki int olan değerleri yazdırın
# while i < len(dizi):
#     if type(dizi[i]) == int:
#         print(dizi[i])
#     i += 1

# kullanıcının girdiği sayıyı ayırın
# çıktı 1 4 5 3
# algoritması: 10'a modunu al, int'e çevir. tekrarla.
sayi = input("Lütfen sayınızı giriniz: ")
if sayi.isdigit():
    sayi = int(sayi)
    liste = []
    while sayi > 0:
        liste.append(sayi % 10)
        sayi = int(sayi / 10)
    liste.reverse()
    i = 0
    while i < len(liste):
        print(liste[i], end=" ")
        i += 1
else:
    print("Hata.")
