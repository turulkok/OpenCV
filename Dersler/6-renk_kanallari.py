# renk_kanallari.py

import cv2

deltax=0
deltay=0

img = cv2.imread('../Resimler/monalisa.jpg')
m = img.copy()
m[:,:,1]=0
m[:,:,2]=0
# mavi renk filtresini elde etmek icin yesil ve kirmizi renk kanallarini sifira esitliyoruz

y = img.copy()
y[:,:,0]=0
y[:,:,2]=0
# Yesil renk filtresini elde etmek icin mavi ve kirmizi renk kanallarini sifira esitliyoruz

k = img.copy()
k[:,:,0]=0
k[:,:,1]=0
# Kirmizi renk filtresini elde etmek icin yesil ve kirmizi renk kanallarini sifira esitliyoruz
print(img.shape)#resmin boyutlarini verir -> yukseklik, genislik, renk kanallari

#renk kanallarinin hepsinin ayni anda olmasi resmimizin orijinal halinin ortaya cikmasini sagliyor
cv2.imshow("Orijinal",img);cv2.moveWindow('Orijinal',10,10)
'''
    Yükseklik, genişlik ve kanal sayısına img.shape
    ile erişebiliriz: Yükseklik indeks 0'da,
    Genişlik indeks 1'de; ve indeks 2'deki kanal sayısı.
'''

cv2.imshow('MAVi',m)
cv2.moveWindow('Mavi',10,img.shape[0]+deltay)
#moveWindow(x = 10,ya = yukselik + deltay)

cv2.imshow('Kirmizi',k)
cv2.moveWindow('Kirmizi',img.shape[1]+deltax,10)
#moveWindow(x = genislik + deltax , y = 10)

cv2.imshow('Yesil',y)
cv2.moveWindow('Yesil',img.shape[1]+deltax,img.shape[0]+deltay)
#moveWindow(x = genislik + deltax , yukseklik + deltay)
#moveWindow() ile pencerelerin acilma konumlarini ayarliyoruz
cv2.waitKey(0)
cv2.destroyAllWindows()