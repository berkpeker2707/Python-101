# i = 0
# while i < 10:
#     print("asd")
#     i += 1
#     if i == 10:
#         break
#
# while True:
#     veri = input("Veri giriniz: ")
#     if veri == "-1":
#         break
#
# # kullanıcı 1 girene kadar girdiği tüm değerleri çarpan, (harf olmaması lazım, harf ise uyarı verir)
# # 1 girdiğinde ise sonucu yazdıran
# carp = 1
# while True:
#     sayi = input("Sayi giriniz: ")
#     if sayi.isdigit():
#         sayi = int(sayi)
#         carp = carp * sayi
#         if sayi == 1:
#             print("Sayınız: " + str(carp))
#             break
#     else:
#         print("Hata")
#
# # kullanıcı ad = "admin" ve pw = "123" girmediği sürece giriş yapmayı dener.
# # yanlış giriş yaparsa lütfen tekrar deneyiniz diyecek,
# # eğer 3 defa hatalı giriş yaparsa limit doldu deyip dögü sonlanacak
# yan = 1
# while True:
#     ad = input("Lütfen kullanıcı adı giriniz: ")
#     pw = input("Lütfen kullanıcı şifresi giriniz: ")
#     if ad != "admin" and pw != "123":
#         print("Lütfen tekrar deneyiniz.")
#         yan += 1
#         if yan == 4:
#             print("Giriş hakkınız doldu.")
#             break
#     else:
#         print("Hoş geldin Admin")
#         break
#
# # continue keyword'ü, alttaki kodları okumaz ve while döngüsünün şart işlemine geri döner
# # break ise döngüyü sonlandırır
# i = 0
# while True:
#     i += 1
#     if i % 2 == 1:
#         continue
#     print(i)
