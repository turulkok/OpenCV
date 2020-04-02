import cv2
import numpy as np

deltax = 0
deltay = 0

imaj = cv2.imread('../Resimler/pou400.png')
n = 11
kernel = np.ones((n,n),np.float32) / (n*n*1.0) #matris isleme girdiginde en fazla 0-1 arasinda deger almasi saglaniyor
#(kaynak, derinlik, kernel, capa, delta, sinirtipi)
blur = cv2.filter2D(imaj,-1,kernel)
                        #-1 orjinal resmin boyutlarina gore islem yapilmasini saglar
cv2.imshow('imaj',imaj)
cv2.imshow('filter2D',blur)
cv2.moveWindow('imaj',10,10)
cv2.moveWindow('filter2D',imaj.shape[1]+deltax,10)
cv2.waitKey(0)
cv2.destroyAllWindows()