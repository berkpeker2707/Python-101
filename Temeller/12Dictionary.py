# # key:value ilişkisi vardır. d[key] = value
# d1 = {}
# d2 = dict()
#
# telefonListesi = {"051454":"Annem","1232351asd":"Babam","13asd13":"Ahmet"}
# print(telefonListesi["1232351asd"])
#
# d3 = {2:"cengiz","Ali": "Mühendis", "Ahmet": "Sekreter", 6: "Sanane", 1.6: True}
#
# # EKLEME
# d3["Ezgi"]="Yazar"
# d3[2]="Işıl" # eğer aynı keyde eleman varsa eskisinin üzerine basar-siler, öyle ekler
# print(d3)
#
# print(d3.keys()) # keyleri verir
# print(d3.values()) # value verir
# print(d3.get("Ezgi1")) # keyin karsılındakı value verir
# # print(d3["asd"]) # yoksa hata verir
# if "Işıl" in d3:
#     print(d3["asd"])
# else:
#     print("Bu eleman yoktur !")
#
# # SİLME
# if "Ezgi" in d3:
#     print(d3.pop("Ezgi")) # siler ve sildiği değeri geri döndürür
#     print(d3.popitem()) # son elemanı siler ve geri döndürür

# d1 = {"Ahmet Fatih":["Tel1","Tel2"]}
#
# d2 = {"Sisli":{"Muhendis":["Ahmet","Serkan"],"TeknikServis":["Mesut","Ezgi"]},
#       "Kadikoy":{"Muhendis":["Ali","Mesut"]}}
# #print(d2["Kadikoy"]["Muhendis"])
#
# for item in d2.keys():
#     print(d2[item])

'''
    tr-ing sözlük:
    bailangıçta kendiniz 3-5 tane key-value ekleyin.
    kullanıcıya sorulur:
    1-Ekleme
    2-Arama
    3-Çıkış

    1->> ingilizcesi eklenecek olan kelime giriniz :
        bunun karşılığı nedir: bu key-value ilişkisi eklenir
    2->> araacak olan tr kelimesi griniz:
        bu kelime varsa karşılığı yazıdlır yoksa yoktur yazılır ve
        bu değeri sozluge eklemek ister msiniz: E ise value istenir ve diziye eklenir,
                                                H ise tamam denilir
    3->> çıkış yapılıyor.

'''

sozluk = {"car": "araba", "white": "beyaz", "black": "siyah"}

while True:
    secim = input("""
1-Ekleme
2-Arama
3-Çıkış
Seçiminiz:""")
    if secim == "1":
        ing = input("ING giriniz :")
        tr = input("TR giriniz :")

        sozluk[ing] = tr
        print("Ekleme gerçekleşti !")
    elif secim == "2":
        ing = input("ING kelime giriniz :")
        if ing in sozluk:
            print("{}->{}".format(ing, sozluk[ing]))
        else:
            yrd = input("bu veri yoktur. yardımcı olmak ister msin:")
            if yrd == "E":
                tr = input("TR girinzi :")
                sozluk[ing] = tr
                print("Teşekkürler")
            else:
                print("Peki yardım etsen nolurdu. !")
    elif secim == "3":
        print("Çıkış yapılyıor ")
        break
    else:
        print("Hatalı giriş yaptınız !")










