
# class Urun:
#     def __init__(self,ad,marka,barkod):
#         self.setAd(ad) # private yaptık. __ getirerek. Diğer classlardan erişim kısıtlandı--> capsulation
#         self.__marka=marka
#         self.__barkod=barkod
#
#     def getAd(self):
#         return str(self.__ad).capitalize() # encapsulation
#
#     def setAd(self,newAd):
#         if len(newAd)>2 and str(newAd).isalpha():
#             self.__ad=newAd
#         else:
#             self.__ad=""
#
# u1 = Urun("kumanda1","sony","123")
# print(u1.getAd())


class Urun:
    def __init__(self,ad,marka,barkod):
        self.__ad=ad # private yaptık. __ getirerek. Diğer classlardan erişim kısıtlandı--> capsulation
        self.__marka=marka
        self.__barkod=barkod

    @property
    def Ad(self):
        return str(self.__ad).capitalize()

    @Ad.setter
    def Ad(self,newAd):
        if len(newAd) > 2 and str(newAd).isalpha():
            self.__ad=newAd
        else:
            self.__ad="Hatali giriş"

u1 = Urun("kumanda1","sony","123")
u1.Ad="dsfjkl1"

print(u1.Ad)





