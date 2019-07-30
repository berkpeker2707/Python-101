# geri dönüş olmayan ve parametresiz
# fonk ismi genelde buyuk harfle baslar.

def IslemYap():
    global s1
    s1 = input("Sayi1 :")
    s2 = input("Sayi2 :")
    print(s1 + s2)

# s1=5
# IslemYap()
# print(s1)

# geri dönüş olmayan ve parametreli
def Carp(a, b="100"):  # default deger ataması yapılabilir
    print(a + b)


def Carp1(a, b):  # default deger ataması yapılabilir
    print(a + b)

def Hesapla(*degerler):
    for item in degerler:
        print(item)
# Hesapla(123,346,3542,4,1234,123,123,12,312,321,3,123)

# s1 = input("s1:")
# s2 = input("s2:")
#
# Carp1(b=12,a=123)


# login fonk(kulAdi,kulPw) eğer kullanıcı admin ve pw=123 ise hoşgeldin, değilse hatalı giriş yazacak
# kulAd ve pw degerleri kullanıcıdan alınacak


# parametresiz geri dönüşlü

def Sonuc():
    a = int(input("Deger 1:"))
    b = int(input("Deger 2:"))
    if a == 1:
        return a + b
    else:
        return a - b
    # print("qasd") # buraya bu kod gelmez !


def SayiAl():
    a = int(input("Deger 1:"))
    b = int(input("Deger 2:"))
    return a, b

# x1, x2 = SayiAl()

# donen = Sonuc()
# print(donen)

# parametreli geri dönüşlü

def Cikar(sayi1, sayi2):
    return sayi1 - sayi2


# print(Cikar(5, 2))

'''
    DegerAl() ->  Kullanıcıdan string bir deger alır ve bu degeri döndürür
    Bul(donen)->       DegerAl'dan dönen string içinde kaç tane rakam var bulur ve yazdırır
'''

def DegerAl():
    deger = input("Deger giriniz :")
    return deger

def Bul(donen):
    toplam = 0
    for item in donen:
        if item.isdigit():
            toplam += 1
    print(toplam)

# x = DegerAl()
# Bul(x)

'''
    DegerAl()- kullanıcıdan alınan degeri döndürür
    isAsal(donen) - kullanıcıın girdiği değer asal ise True döndürür, değilse False döndürür
    Yazdir(asal) - asal True ise ASALDIR, değilse ASAL DEĞİLDİR yazdırır.
'''