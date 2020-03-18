'''ASCII Destekli Fontlarla Yazi Yazmak'''

import cv2
import numpy as np

fontlar = [
    'FONT_HERSHEY_SIMPLEX', 'FONT_HERSHEY_PLAIN',
    'FONT_HERSHEY_DUPLEX','FONT_HERSHEY_COMPLEX',
    'FONT_HERSHEY_TRIPLEX','FONT_HERSHEY_COMPLEX_SMALL',
    'FONT_HERSHEY_SCRIPT_SIMPLEX',
    'FONT_HERSHEY_SCRIPT_COMPLEX']#font listesi olusturduk
imaj = np.ones((720,780,3),np.uint8)*255#beyaz imaj (resim)
for j in range(8):
    cv2.putText(imaj,fontlar[j],(20,40+j*40),j,1.1,(0,0,0),1)
    '''
        putText fonksiyonun parametreleri
        birinicisi Hangi görsele ekleyeceğimizi
        ikincisi Ne yazacağımızı
        üçüncüsü Görselin hangi kısmına ekleyeceğimizi
        dördüncüsü Hangi formatta yazacağımızı
        beşincisi Skalamızı ekliyoruz (boyut)
        altıncısı Hangi renk ile yazacağımızı
        yedincisi de kalınlık belirtir
        biz burada opencv'nin bize sunduğu tüm fontlar ile yazı yazdık bunu for döngüsü içerisinde yaptık
    '''

italik = 16
for j in range(8):
    cv2.putText(imaj,fontlar[j]+'(italik)',(20,400+j*40),j+italik,1.1,(0,0,0),1)

cv2.imshow('imaj',imaj)

cv2.waitKey(0)
cv2.destroyAllWindows()
