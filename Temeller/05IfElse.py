# sayi = int(input("Sayı giriniz: "))
# if sayi > 0:
#     print("Sayı pozitif.")
# elif sayi == 0:
#     print("Sayı 0.")
# else:
#     print("Sayı negatiftir.")
#
# # else bir üstteki if veya elif'le grup kurar
# # bütün kosullarda if kullanırsak optimizasyon olarak yanlışlık yapmış oluruz
#
# if sayi > 0:
#     print("Pozitif")
# if sayi == 0:
#     print("0")
# else:
#     print("Sayı negatif.")
#
#     if sayi == 1:
#         print("bir")
#     elif sayi == 2:
#         print("iki")
#     elif sayi == 3:
#         print("üç")
#     elif sayi == 4:
#         print("dört")
#     elif sayi == 5:
#         print("beş")
#     else:
#         print("başka bir değer")
#
# ad = input("kullanıcı adı: ")
# if ad == "admin":
#     pw = input("kullancı pw: ")
#     if pw == "123":
#         print("giriş yaptınız")
#     else:
#         print("yanlış şifre")
# else:
#     print("isim yanlış")
#
# ad = input("kullanıcı adı: ")
# pw = input("kullanıcı pw: ")
# # and keyword'ü tüm koşulların sağlandığı durumda True döndürür
# if ad == "admin" and pw == "123":
#     print("Hoş geldin admin")
# else:
#     print("hata")
#
# # or keyword'ü herhangi bir şart True olduğunda True döndürür
# if ad == "admin" or pw == "123":
#     print("hg")
# else:
#     print("hata")
#
# sayi = input("Sayi giriniz: ")
# if sayi.isdigit():
#     sayi = int(sayi)
#     print(sayi + 2)
# else:
#     print("Hata")
#
# # aynı
# sayi.isdigit()
# sayi.isdigit() is True
# not sayi.isdigit() is False
#
# if sayi.isdigit()
#     print("Hata oluştu.")
# else:
#     sayi = int(sayi)
#     print(sayi + 2)
#
# """
# kullanıcının girdiği iki sayının ortalaması.
# """
# s1 = input("ilk sayı: ")
# s2 = input("ikinci sayı: ")
# if s1.isdigit() and s2.isdigit():
#     s1, s2 = int(s1), int(s2)
#     print((s1 + s2) / 2)
# else:
#     print("Hata")
#
# """
# kullanıcının girdiği sayı tek midir çift midir?
# """
# say = input("Sayınızı giriniz: ")
# if say.isdigit():
#     say = int(say)
#     if say % 2 == 0:
#         print("Sayınız çifttir.")
#     else:
#         print("Sayınız tektir.")
# else:
#     print("Hata.")
#
# """
# kullanıcıdan vize-final notları alınır.
# -vize ve final yüzden büyük olamaz. not olarak harf giremez.
# -ortalama = vizenin yüzde %40 + final % 60
#
# ortalama:
# 100 - 90 = AA
# 90 - 85 = BA
# 85 - 75 = BB
# 70 - 75 = CB
# 70 - 60 = CC
# 60 - 50 = DC
# 50 - 45 = DD
# 45 - 0 = FF
#
# Çıktı:
# Vize: ..., Final: ..., Ortalama: ... olan notun harf karşılığı: ....
# """
# vi = input("Vize notunuzu giriniz: ")
# fi = input("Final notunuzu giriniz: ")
# if vi.isdigit() and fi.isdigit():
#     vi, fi = int(vi), int(fi)
#     if (vi <= 100 and fi <= 100) and (vi >= 100 and fi >= 100):
#         ort = vi * 0.4 + fi * 0.6
#         if 100 >= ort >= 90:
#             harf = "AA"
#         elif 90 > ort >= 85:
#             harf = "BA"
#         elif 85 > ort >= 75:
#             harf = "BB"
#         elif 75 > ort >= 70:
#             harf = "CB"
#         elif 70 > ort >= 60:
#             harf = "CC"
#         elif 60 > ort >= 50:
#             harf = "DC"
#         elif 50 > ort >= 45:
#             harf = "DD"
#         else:
#             harf = "FF"
#         print("Vize: {}, Final: {}, Ortalama: {} olan notun harf karşılığı {}.".format(vi, fi, ort, harf))
#     else:
#         print("Vize ve Final notları 0 ile 100 arasında olmalıdır.")
# else:
#     print("Sayıyla giriş yapınız.")

"""
fabrikada işçilere ikramiye verilecektir.
-işçiden çocuk sayısı ve maaş verisi alınacaktır.

-eğer çocuk sayısı 3+ ise maaşın yüzde 10'u kadar,
2 ise maaşın yüzde 5'i kadar,
1 ise maaşın yüzde 3'ü kadar ikramiye verilecektir.

Çıktı:
Maaşı: ... TL, Çocuk Sayısı: ... olan işçinin bu ayki maaşı ... TL'dir.
"""
# ma = input("Maaşınızı giriniz: ")
# co = input("Çocuk sayınızı giriniz: ")
# if ma.isdigit() and co.isdigit():
#     ma, co = int(ma), int(co)
#     if co >= 1 and co <= 3:
#         if co >= 3:
#             yema = ma * 0.10 + ma
#         elif co == 2:
#             yema = ma * 0.05 + ma
#         elif co == 1:
#             yema = ma * 0.03 + ma
#         print("Maaşı: {} TL, Çocuk Sayısı: {} olan işçinin bu ayki maaşı {} TL'dir.".format(ma, co, yema))
#     else:
#         print("Lütfen 1 ile 3 arasında değer giriniz.")
# else:
#     print("Lütfen sayısal değerler girin.")

"""
boy = float -- 1.85
harf içeremez ağırlık ve boy

vke = agirlik/boyun karesi
vke ->
0 - 18.49 -> zayıf
18.5 - 24.9 -> normal
25 - 29.9 -> fazla kilolu
30 - 34.9 -> 1.sınıf obez
35 - 44.9 -> 2.sınıf obez
45+ -> 3.sınıf obez
"""

# bo = float(input("Boyunuzu giriniz: "))
# ag = input("Ağırlığınızı giriniz: ")
# if ag.isdecimal():
#     ag = int(ag)
#     vke = ag / (bo **2)
#     vke = float(vke)
#     print(vke)
#     if 0 <= vke <= 18.49:
#         print("zayif")
#     elif 18.5 <= vke <= 24.99:
#         print("Normal")
#     elif 25 <= vke <= 29.9:
#         print("Fazla Kilolu")
#     elif 30 <= vke <= 34.9:
#         print("1.Sınıf obez")
#     elif 35 <= vke <= 44.9:
#         print("2.sınıf obez")
#     else:
#         print("3.sınıf obez")
# else:
#     print("Hata")

"""
delta = b^2 - 4ac
delta > 0 ->> iki kök vardır.
kok1 = (-b-kökö(delta))/2a  kok2= (-b+kök(delta))/2a
delta == 0 ->> kök yoktur.
çıktı: 2 kok vardır. x1:.. x2:..
"""

# a = input("a değerini giriniz: ")
# b = input("b değerini giriniz: ")
# c = input("c değerini giriniz: ")
# if a.isdigit() and b.isdigit() and c.isdigit():
#     a, b, c = int(a), int(b), int(c)
#     delta = (b ** 2) - (4 * a * c)
#     if delta > 0:
#         kok1 = (-b - (delta ** (1 / 2))) / 2 * a
#         kok2 = (-b + (delta ** (1 / 2))) / 2 * a
#         print("İki kök vardır. x1: {}, x2: {}".format(kok1, kok2))
#     elif delta == 0:
#         kok1 = kok2 = -b / (2 * a)
#         print("İki kök vardır. x1: {}, x2: {}".format(kok1, kok2))
#     elif delta < 0:
#         print("Kök yoktur.")
# else:
#     print("Lütfen rakam giriniz.")

"""
Kullanıcıdan bir kelime, bir de rakam alınır.
Rakam ne kadarsa o indise kadar harf büyük yazılır.
"""
kelime = input("Kelime giriniz: ")
rakam = input("Rakam giriniz: ")
if rakam.isdigit() and kelime.isalpha():
    rakam = int(rakam)
    print(kelime[0:rakam].upper() + kelime[rakam:])
else:
    print("Lütfen verileri uygun şeklide giriniz.")
