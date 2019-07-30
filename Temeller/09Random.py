import random

# liste = ["ankara", "izmir", "çorlu"]
#
# print(random.random())
# print(random.randint(0, 12))  # 0 ile 12 arası döner. 12 dahil
# print(random.randrange(0, 12))  # 0 ile 12 arası döner. 12 dahil değil
# print(random.choice(liste))  # liste içinden rastgele eleman çeker
#
# liste = random.sample(range(10, 100), 5)  # kaç tane lazımsa o kadar sayiyi listeye atar
# # 10 ile 100 arası 5 tane bu örnekte
# print(liste)
#
# # bilgisayardan rastgele sayı üretilir. 0 - 100
# # kullanıcı bu sayıyı bilene kadar bu sayiyi tahmin etmesi istenir
# # eğer üretilen sayi kullanıcının girdiğinden küçükse YÜKSELTİN;
# # büyük ise DÜŞÜRÜN
# # eşit ise TAM İSABET diyecektir.
# # kullanıcının bu sayıyı kaç defada bildiğini yazdırın.

tut = 0
tahmin = 0
sayi = random.randint(0, 100)
print(sayi)
while sayi != tahmin:
    tahmin = input("Tahmin giriniz: ")
    tahmin = int(tahmin)
    if sayi > tahmin:
        print("Lütfen daha büyük değer giriniz.")
        tut += 1
    elif sayi < tahmin:
        print("Lütfen daha küçük değer giriniz.")
        tut += 1
    else:
        print("Doğru tahmin.")
        print(tut)
