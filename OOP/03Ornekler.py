# class Sistem():
#     def Login(self,ad,pw):
#         for item in Kullanici.liste:
#             if item.ad==ad and item.pw==pw:
#                 return True
#         return False
#
# class Kullanici:
#
#     liste = []
#     def __init__(self,ad,pw):
#         self.ad=ad
#         self.pw=pw
#         Kullanici.Ekle(self)
#
#     @classmethod
#     def Ekle(cls,kisi):
#         cls.liste.append(kisi)
#
# k1 = Kullanici("admin","123")
# k2 = Kullanici("admi2","123")
# s = Sistem()
#
# ad = input("Ad :")
# sifre = input("Pw :")
# if s.Login(ad,sifre):
#     print("Hoşgeldin ",ad)
# else:
#     print("HATALI GİRİŞ")


class Atm:
    def __init__(self, ad):
        self.ad = ad
        self.islemUcreti = 10

    def AyniBankaMi(self, kul):
        if kul.bankAd == self.ad:
            return True
        else:
            return False

    def ParaCek(self, kul, miktar):
        if kul.para > miktar:
            kul.para -= miktar
            if not self.AyniBankaMi(kul):
                kul.para -= self.islemUcreti
                print("{} Tl işlem ücreti alındı !".format(self.islemUcreti))
            print("{} Tl para çekildi.".format(miktar))
        else:
            print("Yetersiz bakiye !")

    def ParaYatir(self,kul,miktar):
        kul.para+=miktar
        if not self.AyniBankaMi(kul):
            kul.para -= self.islemUcreti
            print("{} Tl işlem ücreti alındı !".format(self.islemUcreti))
        print("{} Tl para yatırıldı".format(miktar))

class User:
    def __init__(self,ad,soyad,bankAd,para):
        self.ad=ad
        self.soyad=soyad
        self.bankAd=bankAd
        self.para=para

    def Yazdir(self):
        return "{} {} {} {}".format(self.ad,self.soyad,self.bankAd,self.para)

u1 = User("Ahmet","Avci","İş",1000)
atm = Atm("İş")
print(u1.Yazdir())

atm.ParaCek(u1,500)
atm.ParaYatir(u1,400)
print(u1.Yazdir())