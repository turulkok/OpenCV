import cv2
import numpy as np
import sys

deltax = 0
deltay = 0

img = cv2.imread("../Resimler/monalisa.jpg")
maske = np.ones(img.shape,dtype="uint8")*255 #beyaz bir resim olusturduk
    #img.shape resmin boyutu kadar bir pencere olusturmamizi sagliyor
maske[:,260:] = [0,0,0]#resmin ortasina kadar siyah alan olusturmak


maskeli = cv2.bitwise_and(img,maske)#maskenin siyah bolgeleri siyah kalir beyaz kisimlari diger resim ile doldurulcak
        #cv2.bitwise_and(ilk girdi dizisi,ikinci girdi dizisi)
        #ilk parametre okuttugumuz resmimiz ikincisi ise olusturdugumuz siyah maske
        #bitwise_and iki resmin bitsel birlesimini saglar
cv2.imshow('img',img)#resim gosterme islemi
cv2.moveWindow('img',10,10)#resmin nerede cikagi
cv2.imshow('maske',maske)#maske gosterimi
cv2.moveWindow('maske',img.shape[1]+deltax,10)#resmin nerede cikacagi
cv2.imshow('maskeli',maskeli)#maske gosterimi
cv2.moveWindow('maskeli',380,img.shape[0]+deltay)#maskeli resmin nerede cikacagi

cv2.waitKey(0)
cv2.destroyAllWindows()