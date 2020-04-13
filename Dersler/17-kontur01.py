import cv2
import numpy as np

imaj = cv2.imread('../Resimler/python.png')

# resmin boyutunu buyutme

y = imaj.shape[0]*2
x = imaj.shape[1]*2

imaj = cv2.resize(imaj,(x,y))

gri = cv2.cvtColor(imaj,cv2.COLOR_BGR2GRAY)

'''
cv2.cvtColor()
    Parameters:
        src: rengi degistirilecek goruntu
        code: renk alani donusturme kodu
'''
_,sb = cv2.threshold(gri,127,255,cv2.THRESH_BINARY)
#_ = esik degeri , sb = yeni olusan esik goruntusudur
konturlar = cv2.findContours(sb,cv2.RETR_EXTERNAL,
                              cv2.CHAIN_APPROX_SIMPLE)[-2]

# cv2.findContours(orjinal imaj = imaj, mod = cv2.RETR_EXTERNAL, metod = cv2.CHAIN_APPROX_SIMPLE)
#mod : kontur bulma yontemi (RETR_LIST,RETR_EXTERNAL,RETR_CCOMP,RETR_TREE)
#metod : kontur yaklasim yontemi (approximation)

imaj2 = cv2.drawContours(imaj.copy(),konturlar,-1,(0,0,255),2)

'''
cv2.drawContours()
    Parameters:
        image – Hedef goruntu.
        contours – Tüm giriş konturları. Her kontur bir nokta vektörü olarak saklanır.
        contourIdx – Çizilecek konturu gösteren parametre. Negatifse, tüm konturlar çizilir.
        color - kontur rengi
        thickness – konturlarin cizgi kalinligi

'''

#iki resmi dusey olarak birlestirme
imaj3 = np.vstack((imaj,imaj2))
cv2.imshow('imaj3',imaj3)
cv2.moveWindow('imaj3',10,10)

cv2.waitKey(0)
cv2.destroyAllWindows()