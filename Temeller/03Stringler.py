cumle = ",,,,,buGün hAVA çok GÜzel.      "
print(cumle.upper())  # bütün harfleri büyültür
print(cumle.lower())  # bütün harfleri küçüktür
print(cumle.capitalize())  # ilk elemanı büyültür, diğerlerini küçültür
print(cumle.title())  # bütün kelimelerin ilk harflerini büyültür
print(cumle.swapcase())

# region
# açılır kapanan bir bölüm yaratır (region ve endregion arası)
# endregion

kelime = "Arabalar"
# süsleme
print(kelime.center(20, "*"))  # sağına ve soluna süsleme işareti
print(kelime.ljust(20, "*"))  # soluna süsleme işareti
print(kelime.rjust(20, "*"))  # sağına süsleme işareti
print(kelime[3])  # tek harf verir
print(kelime[1:6])  # 1.indisten 6.indise kadar değerleri getirir. 6 dahil değil
print(kelime[1:91])  # eğer sağ taraf sınır aşarsa problem yok
print(kelime[1:7:2])  # 1'den başlar 7'ye kadar gider, 2'şer 2'şer
print(kelime[-1])  # son elemanı verir
print(kelime)
print(kelime[:])
print(kelime[2:])  # 2'den sonuna kadar gider
print(kelime[5:])  # baştan başlar, 5'e kadar gider

print(kelime.startswith("A"))  # içindeki harf ile mi başlıyor
print(kelime.endswith("z"))  # içindeki harf ile mi bitiyor
print(kelime.count("a"))  # kaç tane bu string'ten var
print(kelime.index("b", 1, 4))  # hangi index'te
print(kelime.__contains__("b"))  # varsa True yoksa False
print("b" in kelime)  # içinde var mı
print(cumle.replace("buGün", "!****!"))  # değiştirme işlemi
print(cumle.strip(","))  # sağdaki ve soldaki değerleri siler, eğer parametre girmezsen boşlukları siler
print(cumle.lstrip())  # soldaki boşlukları veya değerleri siler
print(cumle.rstrip(' '))  # sağındaki değerleri siler

print(cumle.split())  # ayırma işlemi yapar, eğer parametre girmezsen space'e göre ayırır
x = cumle.split('.')
print(len(kelime))  # boyut verir

isim = "sayı1"
print(isim.isalnum())  # .,:? vesaire varsa False, yoksa True döner
print(isim.isalpha())  # sadece harfse True, harf haricinde en az bir karakter varsa False der
print(isim.isdigit())  # sadece rakam mı
print(isim.isdecimal())  # sadece rakam mı
print(isim.islower())  # hepsi küçük harf mi
print(isim.isupper())  # hepsi büyük harf mi
print(isim.isspace())  # hepsi space mi
print(isim.istitle())  # hepsi büyük harf mi
print(isim.isidentifier())  # değişken ismi verilebilir mi

print(isim.upper().replace("ı", "i").capitalize())
