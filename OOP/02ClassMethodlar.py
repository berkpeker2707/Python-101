
class Calisan():
    calisanListe = []
    def __init__(self,ad,soyad,departman):
        self.ad=ad
        self.soyad=soyad
        self.departman=departman
        Calisan.Ekle(self)

    @classmethod
    def Ekle(cls,kisi):
        cls.calisanListe.append(kisi)

    @classmethod
    def Parcala(cls,string):
        x = str(string).split(',')
        return cls(x[0],x[1],x[2])

    def Yazdir(self):
        return "{} {} {}".format(self.ad,self.soyad,self.departman)

c1 = Calisan("ahmet","avci","yazılım")
c3 = Calisan("mesut","kaba","makine")
c2 = Calisan("canan","sakal","elektrik")
c4 = Calisan("serkan","reis","yazılım")
Calisan.Parcala("aysenur,gelir,yazılım")

for item in Calisan.calisanListe:
    if item.departman=="yazılım":
        print(item.Yazdir())