# class Canli:
#
#     def __init__(self,ad,tur,yas):
#         self.ad=ad
#         self.tur=tur
#         self.yas=yas
#         print("canlı")
#
#     def Dogma(self):
#         print("{} Doğdu".format(self.ad))
#
#     def Olme(self):
#         print("{} Öldü".format(self.ad))
#
#     def Iletisim(self):
#         print("{} Iletisim".format(self.ad))
#
#     def Gelisme(self):
#         print("{} Gelisme".format(self.ad))
#
# class Hayvan(Canli):
#     def Avlanma(self):
#         print("Hayvan avlanma")
#
# class Kedi(Hayvan):
#     def Tirmanma(self):
#         print("Kedi tırmanma")
#
# class Insan(Canli):
#     def __init__(self, ad, tur, yas,soyad):
#         super().__init__(ad, tur, yas)
#         self.soyad=soyad
#         print("insan")
#
#     def Konusma(self):
#         pass
#
# class Erkek(Insan):
#     def Askerlik(self):pass
#     def Sunnet(self): pass
#     def Iletisim(self): pass # override - polymhorphism
#
# e = Erkek("ahmet","asd",12,"avci")
# e1 = Erkek("fatih","asd",12,"avci")
# e.Dogma()
# e1.Olme()

# class Sekil:
#     def __init__(self,k1,k2):
#         self.k1=k1
#         self.k2=k2
#
#     def AlanHesapla(self):
#         return self.k1*self.k2
#
#     def CevreHesapla(self):
#         return (self.k1+self.k2)*2
#
# class Dikdortgen(Sekil):
#     def __init__(self, k1, k2):
#         super().__init__(k1, k2)
#         self.k3=k1
#         self.k4=k2
#
#
# class Kare(Sekil):
#     def __init__(self, k1, k2):
#         if k1==k2:
#             super().__init__(k1, k2)
#         else:
#             super().__init__(1,1)
#         self.k3=k1
#         self.k4=k2
#
# class Ucgen(Sekil):
#     def __init__(self, k1, k2,k3):
#         super().__init__(k1, k2)
#         self.k3=k3
#
#     def AlanHesapla(self):
#         return self.k1*self.k2/2
#
#     def CevreHesapla(self):
#         return self.k1+self.k2+self.k3
#
# u = Ucgen(5,6,7)
# d = Dikdortgen(5,6)
# k = Kare(5,5)
#
# print(u.CevreHesapla())
# print(u.AlanHesapla())
#
# print(d.AlanHesapla())
# print(d.CevreHesapla())
#
# print(k.AlanHesapla())
# print(k.CevreHesapla())


class Yuruyen:
    def HizliYuru(self): pass
    def YavasYuru(self): pass
    def Ziplama(self):  pass

class Ucabilen:
    def Suzulme(self): pass
    def Kanatlanma(self): pass
    def Dalis(self): pass

class Yuzebilen:
    def Kurbagalama(self): pass
    def Baliklama(self): pass

class Insan(Yuruyen,Yuzebilen):
    pass


