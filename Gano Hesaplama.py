while True:
    derssayisi = int(input("Lütfen, ders sayinizi giriniz: "))
    if derssayisi <= 0:
        print("Lütfen geçerli ders sayisi giriniz.")
        continue
    else:
        break
dersismi, derskredisi, dersharfnotu,toplamkredi = [], [], [], []
i = 0
while (i < derssayisi):
    dersismi.append(input(("Lutfen dersinizin adını giriniz: ")))
    derskredisi.append(float(input("Lütfen dersinizin kredisini giriniz: ")))
    i += 1

toplamkredi = 0
genelpuan = 0

for i in range(0,derssayisi):
    harfnotu = input(str(dersismi[i])+" dersinden geçtiğiniz harf notu: ")
    if harfnotu == "AA":
        sonuç = derskredisi[i] * 4
    elif harfnotu == "BA":
        sonuç = derskredisi[i] * 3.5
    elif harfnotu == "BB":
        sonuç = derskredisi[i] * 3
    elif harfnotu == "CB":
        sonuç = derskredisi[i] * 2.5
    elif harfnotu == "CC":
        sonuç = derskredisi[i] * 2
    elif harfnotu == "DC":
        sonuç = derskredisi[i] * 1.5
    elif harfnotu == "DD":
        sonuç = derskredisi[i] * 1
    elif harfnotu == "FD":
        sonuç = derskredisi[i] * 0.5
    elif harfnotu == "FF":
        sonuç = derskredisi[i] * 0

    toplamkredi += derskredisi[i]
    genelpuan += sonuç

print(genelpuan/toplamkredi)