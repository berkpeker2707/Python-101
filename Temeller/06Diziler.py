liste = []  # tanımlama 1
liste1 = [1123, True, False, "Str deger", 1.041]
liste2 = list()  # içi boş tanımlama, tanımlama 2

# print(liste1[0])
# print(liste1[0:3])
# print(liste1[:])
# print(liste1)
# print(liste1[1:])
# print(liste[:4])
# print(liste1[-1])

# ekleme işlemi
liste2.append(123)
liste2.append(True)
liste2.append(0.123)
liste2.append(False)
liste2.append([12, 3, 123, 12, True])  # dizinin içine dizi eklenebilir
print(liste2)

liste2.extend([12, 3, 123, 12, True])  # açarak ekleme işlemi
print(liste2)

liste2.insert(3, "eklenen")  # istenilen elemana ekleme yapar
print(liste2)

# çıkarma işlemi
liste2.pop()  # en son elemanı çıkartır
print(liste2)
liste2.pop()  # girilen indexe göre çıkartır
print(liste2)

if "eklenen2" in liste2:  # içinde mi
    liste2.remove("eklenen2")  # girilen objeyi çıkarır
else:
    print("eklenen2 değeri listede yok")
print(len(liste2))  # boyut getirir
print(liste2)
liste2.reverse()  # ters çevirir
print(liste2)
print(liste2.index("eklenen"))  # bu object hangi indexte, yoksa hata verir
print(liste2.count(123))  # eleman kaç tane var verir

a = liste2.copy()  # kopyalar
liste2.clear()
print(liste2)  # içini temizler
siralanacak = [1623, 1323, 1223, 12, 31, 23, 1.04]
siralanacak2 = ["abc", "abe", "er", "abd"]
siralanacak.sort(reverse=True)  # büyükten küçüğe
siralanacak2.sort()  # küçükten büyüğe
print(siralanacak)
print(siralanacak2)

'''
kullanıcıya sorulur:
1- Ekleme -> Eklenecek eleman :
2- Çıkarma -> Çıkarılacak eleman : Eğer leman listede yoksa uyarı verir, varsa cıkart
3- Listeleme -> tüm liste yazdırılır
4- Araya ekleme -> kaçıncı elemana ekleyceksın: Eleman : 
Seçiminiz:
'''
soruListe = ["123", "6", "3"]
secim = input("""
1- Ekleme -> Eklenecek eleman :
2- Çıkarma -> Çıkarılacak eleman : Eğer leman listede yoksa uyarı verir, varsa cıkart
3- Listeleme -> tüm liste yazdırılır
4- Araya ekleme -> kaçıncı elemana ekleyceksın: Eleman : 
Seçiminiz:""")

if secim == "1":
    ekle = input("Eklenecek Eleman : ")
    soruListe.append(ekle)
    print("Ekleme işlemi gerçekleşti")
    print(soruListe)
elif secim == "2":
    cikar = input("Cıkarılacak Eleman : ")
    if cikar in soruListe:
        soruListe.remove(cikar)
        print("{} eleman cıkartıldı".format(cikar))
        print(soruListe)
    else:
        print("{} eleman yok".format(cikar))
elif secim == "3":
    print(soruListe)
elif secim == "4":
    index = int(input("kaçıncı elemana :"))
    eleman = input("Eklenecek :")
    soruListe.insert(index, eleman)
    print(soruListe)
else:
    print("HATALI GİRİŞ")
