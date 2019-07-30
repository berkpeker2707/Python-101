# print ("Hellü")
# print("Berk")
# print("Berko \nLatto")  # \n bir aşağı satıra atlar
# print("Berko \tLatto")  # \t bir tab boşluk bırakır
# print("Berko \aLatto")  # \a bip sesi çıkartır
#
# end parametresi bir sonraki print ile ilişkinin ne olacağını belirtiyor
# print("merhaba", end="-")
# print("ahmet", end="*")
# print("fatih")
# print("fatih2")
# print("testoo", end="?")
#
# print("merhaba", "dünya", sep="*", end="++++")
# print("benim", "adım", "berk", sep="?")
#
# # kodu düzenleme: ctrl + alt + l
#
# isim = "Berk"
# soyad = "Peker"
# print(isim + " " + soyad)  # + operatörle yan yana basar
# print(isim, soyad)  # virgülle birleştirmede sep değerine göre yan yana ekler
# print(isim, soyad, sep="\t")  # sep keyword'ü ezildiği için - karakterine göre birleştirir (seperator)
# print(isim, soyad, end="\n")  # end keyword'ü sayesinde, bundan sonraki ilk print işlemine nasıl başlayacağını belirler.
# print(*"TBMM", sep=".")  # string ifadenin başına * getirirsen her harf arasına erişebilirsin.
#
# # kaçış karakterleri
# print("Babam 'eve geç kalma' dedi")
# print('Babam "eve geç kalma" dedi')
# print("Babam \"eve geç kalma\" dedi")
# print('Babam \'eve geç kalma\' dedi')
# print("C:\\rtabzon\\nigde\\adana")
# print("Kaçış karakterleri: \\n, \\t, \\a")
# print(r"Kaçış karakterleri: \n, \t, \a")
#
# ad = "Ahmet"
# soyad = "Avcı"
# numara = 4
# print("Merhaba {} {}, Hoş geldiniz. Numaranız: {}. İyi akşamlar dileriz.".format(ad, soyad, numara))
# print("Merhaba %s %s, Hoş geldiniz. Numaranız: %s. İyi akşamlar dileriz." % (ad, soyad, numara))
#
# # \n yazılmadığı sürece "" içinde istediğin kadar enter'a bas; bir sonraki satıra geçmiş şekilde print etmez.

"""
yazar = string
kitap = string
kitapTarihi = int

.. yazarın .. kitabı .. yılında çıkmış. Okudun mu?
Artı operatörüyle yazın, sonra format, sonra %s ile.
"""
yazar = "Martial"
kitap = "Epigramlar"
kitapTarihi = 5
print(yazar + " " + "yazarının" + " " + kitap + " " + "kitabı" + " " + str(kitapTarihi) + " " + "yılında çıkmış. Okudun mu?")
print("{} yazarının {} kitabı {} yılında çıkmış. Okudun mu?".format(yazar, kitap, kitapTarihi))
print("%s yazarının %s kitabı %s yılınad çıkmış. Okudun mu?" % (yazar, kitap, kitapTarihi))
