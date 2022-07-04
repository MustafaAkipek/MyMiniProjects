print("Akrep ile Yelkovan Arasındaki Açıyı Bulan Program")
zaman = input("Lutfen Saati Giriniz: ")
time = zaman.split(":")
a = time[0] #saati a değişkenine atadık
b = time[1] #dakikayı b değişkenine atadık
print("Saat:",a)
print("Dakika:",b)
ampm = int(a)%12 #saat 12 'den önce veya sonra sıkıntı çıkarmasın diye 12 'ye göre mod aldık
akrep = ampm*30 #her saat başı akrep 30 derece ilerlerdiği için 30 'la çarptık
yelkovan = int(b)*6 #her dakikda başı yelkovan 6 derece ilerlediği için 6 'la çarptık
ilerlemepayi = int(b)/2 #dakika kaç ise o dakikanın yarısı derecede akrep ilerler
açı = akrep-yelkovan #akrep ve yelkovanı çıkartarak aradaki açıyı bulduk
sonuç = abs(açı) #sonuç negatif olmasın diye abs fonksiyonu ile daima pozitif yaptık.
if akrep > yelkovan: #akrep yelkovandan önde ise akrep yelkovan ile arasındaki mesafeyi açacağı için ilerleme payı pozitif etki yapar
    sonuç += ilerlemepayi
elif yelkovan > akrep:
    sonuç -= ilerlemepayi #yelkovan önde ise akrep yelkovan ile arasındaki mesafeyi kapatacağı için ilerleme payı negatif etki yapar
print("Akrep ve Yelkovan arasındaki açı: ",sonuç)