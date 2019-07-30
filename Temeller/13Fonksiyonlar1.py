# region parametresiz ve geri dönüşsüz
from Tools.demo import ss1


def IslemYap():
    s1 = int(input("Sayi 1:"))
    s2 = int(input("Sayi 2:"))
    print(s1 + s2)


def Degistir():
    global s1, s2
    s1 = 10
    s2 = 20
    print(s1, s2)


# IslemYap()
# IslemYap()
# IslemYap()

# s1=100
# s2=200
# Degistir()
#
# print(s1,s2)

# endregion

# region parametreli ve geri dönüşsüz

def Topla(sayi1, sayi2):
    sonuc = sayi1 + sayi2
    print(sonuc)


def Carp(s1, s2=12, s3=5):
    print(s1 * s2 * s3)


# s1 = int(input("Sayi1 giriniz :"))
# s2 = int(input("Sayi2 giriniz :"))
#
# Topla(s1, s2)
# print(s1,s2)

# Carp(s3=10, s1=2)

# endregion

# region parametresiz-parametreli ve geri dönüşlü

def Toplam():
    s1 = input("Sayi 1:")
    s2 = input("Sayi 2:")
    toplam = int(s1) + int(s2)
    return toplam


def DegerAl():
    s1 = input("Sayi 1:")
    s2 = input("Sayi 2:")
    return s1, s2


def Bol(sayi1, sayi2):
    print(sayi1 * 2, sayi2 * 2)


# print(Toplam())
# x, y = DegerAl()
# # print(x * 2, y * 2)
# Bol(x,y)

# endregion

# region SORU 1

'''
    DegerAl() -> kullanıcıdan tek deger alır ve bunu geri döndürür,( sayi )
    KareHesapla(sayi) -> gelen bu sayı parametresinin karesini yazdırır
'''
# def DegerAl1():
#     sayi = int(input("Sayi griniz :"))
#     return sayi
#
# def KareHesapla(s1):
#     print(s1 ** 2)
#
# donen = DegerAl1()
# KareHesapla(donen)

# endregion

# region SORU 2
'''
    DegerAl() kullanıcıdan iki tane sayı alır ve bunları döndürür
    AralikGetir(baslangic,bitis) bu iki deger arasındaki çift sayıları yazdırır. baslangıc< bitis !!!
'''


def DegerAl():
    s1 = int(input("Sayi1 :"))
    s2 = int(input("Sayi2 :"))
    return s1, s2


def AralikGetir(baslangic, bitis):
    if baslangic < bitis:
        for i in range(baslangic, bitis + 1):
            if i % 2 == 0:
                print(i)
    else:
        print("HATALI GİRİŞ")


# sayi1, sayi2 = DegerAl()
# AralikGetir(sayi1,sayi2)
# endregion

# region SORU 3

# alfabe = "abcdefghijklmnoprstuvyz"
# alfabeBoyut = len(alfabe)

# def MetinAl():
#     metin = input("Şifrelenecek metini giriniz :")
#     return metin
#
#
# def Sifrele(metin):
#     sifrelenmisMetin = ""
#     for item in metin:
#         indexx = alfabe.index(item)
#         #print(alfabe[(indexx+4)%alfabeBoyut],end="") #1.yazdırma yontemı
#         sifrelenmisMetin += alfabe[(indexx+4)%alfabeBoyut] # 2. yöntem
#     print(sifrelenmisMetin)
#     Coz(sifrelenmisMetin)
#
# def Coz(metin):
#     sifrelenmisMetin = ""
#     for item in metin:
#         indexx = alfabe.index(item)
#         #print(alfabe[(indexx+4)%alfabeBoyut],end="") #1.yazdırma yontemı
#         sifrelenmisMetin += alfabe[(indexx-4)] # 2. yöntem
#     print(sifrelenmisMetin)
#
# m = MetinAl()
# Sifrele(m)

# endregion

''' UYGULAMA 1
degerAl() -> kullanıcıdan iki sayı alır ve geri döndürür
Bul(s1,s2) -> bu iki sayının ebob ve ekokunu bulup yazdırır 
'''

''' UYGULAMA 2

sayiAl() kullanıcıdan sayı alır ve döner (sayi)
isAsal(sayi) bu girilen sayı asal mıdır? evetse True değilse False döner
Yazdir(asalMi) isAsaldan dönen deger True ise Asaldır değilse asal değildir yazar
'''

''' UYGULAMA 3
Sezar algoritmasının geri çözümünü yapınız.
'''

'''
Degeral() sayı döner
Decimal2Binary(sayi)

'''


def DegerAl2():
    return int(input("Deger Giriniz :"))


def Binary2Decimal(sayi):
    binary = list()
    while True:
        binary.append(sayi % 2)
        sayi = int(sayi / 2)
        if sayi == 0:
            binary.reverse()
            for item in binary:
                print(item, end="")
            break


def Binary3Decimal(sayi):
    binary = ""
    while True:
        binary += str(sayi % 2)
        sayi = int(sayi / 2)
        if sayi == 0:
            binary=list(binary)
            binary.reverse()
            for item in binary:
                print(item, end="")
            break

# Binary2Decimal(DegerAl2())
# Binary3Decimal(DegerAl2())

def Sayi():
    return input("Sayi giriniz :")

def Hesapla(sayi):
    t=0
    for item in sayi:
        t+=Faktoriyel(int(item))

    if t==int(sayi):
        print("DİGİT FAKTORİYEL")
    else:
        print("DEĞİLDİR")

def Faktoriyel(deger):
    toplam=1
    for i in range(1,deger+1):
        toplam*=i
    return toplam
Hesapla(Sayi())

