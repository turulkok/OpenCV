import cv2
import numpy as np

bekle = True
#tusa bastigimizda false 'a doner
arkaplan = np.ones((800,800,3),dtype=np.uint8)*255#800x800 boyutlarinda beyaz arkaplan
if bekle:
    cv2.imshow('arkaplan',arkaplan)#arkaplani goster
    cv2.waitKey(0)

#Arkaplanin ortasina 360piksel yaricapli siyah bir daire cizimi
maske = cv2.circle(arkaplan,(400,400),360,(0,0,0),-1)
#beyaz arkaplanin uzerine 400x400 piksel ve capi 360px olan bir siyah cember cizdiriyoruz
if bekle:
    cv2.imshow('maske',maske)
    cv2.waitKey(0)

#ters maske islemi
tersmaske = (255-maske)#bu islem maskedeki 0'lari 255'e , 255'leri 0'a cevirir yani beyazlar siyah,siyahlar beyaz olur
if bekle:
    cv2.imshow('tersmaske',tersmaske)
    cv2.waitKey(0)
#resim yukleme
img = cv2.imread('../Resimler/monalisa(800x800).jpg')
if bekle:
    cv2.imshow('img',img)
    cv2.waitKey(0)
#ters maskeyi img ye uygula

img = cv2.bitwise_and(img,tersmaske)#resim uzerine tersmaskeyi uyguluyoruz
#resmin orta kisminda monalisa (maskenin beyaz yerleri) dis kisminda siyah alan olusacak
if bekle:
    cv2.imshow('img',img)
    cv2.waitKey(0)

#diger resmi yukle ve maske uygula
img2 = cv2.imread('../Resimler/uzay(800x800).jpg')
if bekle:
    cv2.imshow('img2',img2)
    cv2.waitKey(0)
img2 = cv2.bitwise_and(img2,maske)#uzay resmimize maskeyi uyguluyoruz
#resmin ortasi siyah kenarlari beyaz oluyor.Beyaz(dis) kisma uzay resmimiz gelmis oluyor.
if bekle:
    cv2.imshow('img2',img2)
    cv2.waitKey(0)
#iki resim birlestirme islemi
img3 = img + img2#maske ve tersmaske uygulanmis resimleri birlestiriyoruz
cv2.imshow('img3',img3);cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Calisma Asamalari:
    1-arkaplan olusacak
    2-maske olusacak
    3-tersmaske olusacak
    4-monalisa resmini yukledik
    5-monalisaya ters maske uyguladik
    6-uzay resmini yukledik
    7-uzay resmine maske uyguladik
    8-son olarak iki maske uygulanmis goruntuyu birlestirme islemini gerceklestirdik
'''



