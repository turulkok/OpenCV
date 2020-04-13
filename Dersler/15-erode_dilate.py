import cv2
import numpy as np

imaj = cv2.imread('../Resimler/1.png',0)
kernel = np.ones((5,5),np.uint8)

#sinirlari inceltme
erosion = cv2.erode(imaj, kernel, iterations = 1)
#sinirlari kalinlastirma
dilation = cv2.dilate(imaj, kernel, iterations = 1)
'''
    1-imaj : siyah beyaz resim
    2-kernel : cekirdek
    3-iterations : inceltme ve kalinlastirma isleminin tekrarlanma sayisi
'''

#uc goruntuyu dusey olarak birlestirme
dusey = np.vstack((imaj, erosion, dilation))
#vstack 3 resmi alt alta birlestirme yapar
cv2.imshow('dusey',dusey)
cv2.moveWindow('dusey',600,50)

cv2.waitKey(0)
cv2.destroyAllWindows()