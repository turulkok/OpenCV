# yeniden_boyutlama.py

import cv2
import random

imaj = cv2.imread('../Resimler/sardunya2.jpg')
cv2.imshow('imaj',imaj)

oran = 0.8
imajlar=[]#resimleri bir liste icerisinde tutucaz
for j in range(10):
    oran = random.randint(1,25)/25 # 0 ile 1 arasinda bir sayi olusturur
    rx = int(imaj.shape[1]*oran) #Yeni imajin genisligi
    ry = int(imaj.shape[0]*oran) #yeni imajin yukseligi
    x = random.randint(100,1600)#100-1600 arasinda rastgele x koordinati
    y = random.randint(100,800)#100-800 arasinda rastgele y koordinati
    imajlar.append((str(oran),cv2.resize(imaj,(rx,ry))))
    #listeye ekleme fonksiyonu, cv2.resize(orjinal_imaj,(yeni_yukseklik,yeni_genislik)
    cv2.imshow(imajlar[j][0],imajlar[j][1])
    #pencere ismi olarak kullanilan orani ve yeni olusturan imajin kendisini kullaniyoruz
    cv2.moveWindow(imajlar[j][0],x,y)
    #bir ust satirda kullanidigimiz isimdeki pencerenin x ve y random komutlarini aliyoruz
cv2.waitKey(0)
cv2.destroyAllWindows()
