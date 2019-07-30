# def aa(sayi):
#     return sayi + 5

# deneme = lambda x: x + 5
# print(deneme(6))
# print(aa(6))


# topla = lambda x,y:x+y
# print(topla(8,10))

# dizi = [12,321,321,3,123,123,213,12,312,12,3,13,12]
#
# def Getir():
#     yeniListe =[]
#     for item in dizi:
#         if item%2==0:
#             yeniListe.append(item)
#     return yeniListe
# print(Getir())
#
# print(list(filter(lambda x:(x%2==0),dizi))) # dizi içinde elemanları ayıklamak için kullanılır
# print(list(filter(lambda item:(item%2)==0,dizi)))
#
# print(list(map(lambda x:x*2,dizi))) # dizi içidneki tüm elemanlara etki etmek için kullanılır.

class Kisi:
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad

    def __str__(self):
        return "{} {}".format(self.ad,self.soyad)

liste = []
liste.append(Kisi("Ahmet","Avcı"))
liste.append(Kisi("Serkan","Kara"))
liste.append(Kisi("Kadir","Canan"))
liste.append(Kisi("Kadir","Avcı"))
print(liste)
dizi = list(filter(lambda x:x.ad=="Kadir",liste))

for i in dizi:
    print(i)
