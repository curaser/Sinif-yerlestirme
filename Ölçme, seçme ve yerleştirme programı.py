import random
sinif=[]

print("========================================================================")
print("=================Ölçme, seçme ve yerleştirme programı===================")
print("================Serkan CURA tarafından hazırlanmıştır===================")
print("=======Bu proje, GNU Affero Genel Kamu Lisansı ile lisanslanmıştır.=====")
print("===========Daha fazla bilgi ve proje için www.serkancura.ml=============")
print("========================================================================")
print("Yazar notu: Çıkan sonuca göre çiftler öğretmen masasının önündeki masadan\nbaşlamak kaydıyla yan taraftaki sıranın arkasından devam ederek sıralara\nyerleşeceklerdir.")

def yerlestirme():
    if teksayi==0:
        uzunluk=len(sinif)
        while uzunluk > 0:
            a1=random.choice(sinif)
            sinif.remove(a1)
            a2=random.choice(sinif)
            sinif.remove(a2)
            print(a1 +" ile "+ a2 +" kişisi yan yana oturacaktır.")
            uzunluk=len(sinif)
    if teksayi==1:
        print("")
        print("========================================================================")
        sinif.append("tek")
        uzunluk=len(sinif)
        while uzunluk > 0:
            a1=random.choice(sinif)
            sinif.remove(a1)
            a2=random.choice(sinif)
            sinif.remove(a2)
            if (a1=="tek") or (a2=="tek"):
                if a1=="tek":
                    print(a2 + " kişisi tek oturacaktır.")
                    uzunluk=len(sinif)
                if a2=="tek":
                    print(a1 + " kişisi tek oturacaktır.")
                    uzunluk=len(sinif)
            else:
                print(a1 +" ile "+ a2 +" kişisi yan yana oturacaktır.")
                uzunluk=len(sinif)
        if uzunluk==0:
            print("========================Yerleştirme tamamlandı==========================")

sinifsayi=int(input("Sınıf mevcudunu giriniz... "))
if (sinifsayi)%2==0:
    teksayi=0
else:
    teksayi=1

print("Sınıftaki kişilerin isimlerini teker teker giriniz... ")
while sinifsayi>0:
    ogrenci=input(">>_ ")
    sinif.append(ogrenci)
    sinifsayi=sinifsayi-1

if sinifsayi == 0:
    yerlestirme()

input()
