print("Akrep ile Yelkovan Arasındaki Açıyı Bulan Program")
zaman = input("Lutfen Saati Giriniz: ")
time = zaman.split(":")
a = time[0]
b = time[1]
print("Saat:",a)
print("Dakika:",b)
ampm = int(a)%12
akrep = ampm*30
yelkovan = int(b)*6
ilerlemepayi = int(b)/2
açı = akrep-yelkovan
sonuç = abs(açı)
if akrep > yelkovan:
    sonuç += ilerlemepayi
elif yelkovan > akrep:
    sonuç -= ilerlemepayi
if sonuç > 180:
    yenisonuç = 360 - sonuç
    print("Akrep ve Yelkovan arasındaki açı: ",yenisonuç)
else:
    print("Akrep ve Yelkovan arasındaki açı: ", sonuç)