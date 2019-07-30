
# list deki ekleme çıkarma işlemleri olmaz !.
# daha hızlıdır.

# w3resources.com -> pratik
# youtube.com/sinanurun --> basic
# sadi evren şeker -> advanced

tupleDizisi = ()
print(type(tupleDizisi))
dizi = [123,32,654,12,43,734,532,432,12,3465,"qasdf","2134wetgdtfr"]

dizi = tuple(dizi) # tuple çevirme
print(dizi.count(12)) # kaç tane var
print(dizi.index("qasdf")) # kaçıncı indexte var
print(123 in dizi) # var mı
print(dizi.__contains__(123)) # varmı
print(len(dizi))
print(dizi[5])
print(dizi[5:])
print(dizi[:5])


