# # Tanımlama
# class Insan1:
#     pass
#
#
# class Insan2():
#     pass
#
#
# class Insan3(object):
#     pass
#
#
# # Başlangıç
# class Insan:
#     # attribute - özellik
#     ad = ""
#     soyad = ""
#     boy = 35
#     kilo = 3
#
#
# i1 = Insan()  # nesne üretmek, instance almak, örnek oluşturmak
# i2 = Insan()
#
# i1.ad = "Ahmet"
# i1.soyad = "Avcı"
# i1.kilo = 70
# i1.boy = 170
#
# i2.boy = 45
#
# print(i1.boy)
# print(i2.boy)
#
# class Insan:
#     # nesne oluşturulduğun anda, kod kurucu methoda gelir ve atamalarını yapar. self kavramı önemlidir.
#     def __init__(self):  # kurucu, constructor, yapıcı method
#         self.adi = ""
#         self.soyad = ""
#         self.boy = 40
#         self.kilo = 3
#         self.ozellik = []
#
#
# i1 = Insan()
# i1.adi = "Ahmet"
# i1.ozellik.append("Tembel1")
# i1.ozellik.append("Tembel2")
#
# i2 = Insan()
# i2.adi = "Mesut"
# i2.ozellik.append("Çalışkan")
#
# print(i1.ozellik)
# print(i2.ozellik)
#
# class Insan:
#     # parametre girilmesi zorunludur
#     def __init__(self, ad, soyad, kilo, boy, tc="-1"):
#         self.ad = ad
#         self.soyad = soyad
#         self.kilo = kilo
#         self.boy = boy
#         self.tc = tc
#
#     def Yazdir(self):
#         return "Ad: {}, Soyad: {}, Kilo: {}, Boy: {}, TC: {}".format(self.ad, self.soyad, self.kilo, self.boy, self.tc)
#
#     def suIc(self, litre):
#         print("{} {} {} lt su içti.".format(self.ad, self.soyad, litre))
#
#     def nefes(self):
#         print("{} {} doya doya nefes aldı.".format(self.ad, self.soyad))
#
#
# i1 = Insan("Ahmet", "Avci", 70, 175)
# i2 = Insan("Fatih", "Avci", 80, 165, "123415145")
# # print(i1.ad, i1.soyad, i1.kilo, i1.boy, i1.tc)
# # print(i2.ad, i2.soyad, i2.kilo, i2.boy, i2.tc)
#
#
# print(i1.Yazdir())
# print(i2.Yazdir())
# i1.suIc(5)
# i2.nefes()
#
# """
# Araba classı,
# - marka, model motor,fiyat,renk attribute
# - yas ozelligi kullanıcı girmeyecek ama self olacaktır. (Modele göre, 2013 model mesela 6)
# - Calistir() -> .. marka modeli araba çalıştı.
# - Hızlan (hiz) -> arabanın hızı (hiz) kadar arttı.
# -BilgiVer arabanın tüm özelliklerini yazdırır
# 1 tane araba nesnesi oluşur, tüm değerleri kullanıcı girecek. yani kullanıcıdan 5 tane deger alınıp nesne olusturulacak
# """
#
#
# class Araba:
#
#     def __init__(self, marka, model, fiyat, renk):
#         self.marka = marka
#         self.model = model
#         self.fiyat = fiyat
#         self.renk = renk
#         self.yas = 2019 - int(model)
#
#     def Calistir(self):
#         print("{} marka {} modeli araba çalıştı.".format(self.marka, self.model))
#
#     def Hizlan(self):
#         print("Arabanın hızı artrtı.")
#
#     def BilgiVer(self):
#         print("Markası: {}, Modeli: {}, Fiyatı: {}, Rengi: {}, Yasi: {}".format(self.marka, self.model, self.fiyat,
#                                                                                 self.renk,
#                                                                                 self.yas))
#
#
# marka = input("Arabanın markası: ")
# model = input("Arabanın model: ")
# fiyat = input("Arabanın fiyat: ")
# renk = input("Arabanın renk: ")
#
# a1 = Araba(marka, model, fiyat, renk)
# a1.Calistir()
# a1.Hizlan()
# a1.BilgiVer()
#
"""
Calisan class,
ad, soyad, departman, maas -> Attribute
BilgiVer() -> Kullanıcının herseyini yazdır
ZamYap(miktar) -> eger miktar degeri, calisanin maasinin yarısından fazlaysa
emin misin diye sor, cevap E ise zam yap.
İster kullanıcıdan al, ister elle gir kullanıcı bilgilerini
"""


class Calisan:
    def __init__(self, ad, soyad, departman, maas):
        self.ad = ad
        self.soyad = soyad
        self.departman = departman
        self.maas = maas

    def BilgiVer(self):
        return "Adı: {}, Soyadı: {}, Departman: {}, Maaş: {}".format(self.ad, self.soyad, self.departman, self.maas)

    def ZamYap(self, miktar):
        if self.maas / 2 > miktar:
            self.maas += miktar
            print("Zam yapıldı.")
        else:
            cevap = input("Emin misin?")
            if cevap == "e":
                self.maas += miktar
                print("Zam yapıldı.")
            else:
                print("Zam yapılmadı.")


c1 = Calisan("Ahmet", "Avci", "Yazılım", 6000)
print(c1.BilgiVer())
c1.ZamYap(500)
print(c1.BilgiVer())
