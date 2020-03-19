# -*- coding: utf-8 -*-
#%% OpenCV BGR Mantigi 

import cv2 

resim = cv2.imread("../Resimler/bradpitt.jpg")

print(type(resim))#resmin tipini doner 
print(resim.size)#piksel sayisini doner 
print(resim.shape)#yuksel , genislik , ve kac tane renk kanalindan olusuyor (channel)
print(resim.dtype) #veriler hangi turde saklaniyor 
cv2.imshow("Brad Pitt",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
import cv2 

resim = cv2.imread("../Resimler/bradpitt.jpg")#resim eger gri olursa 

print(resim)#resmin tipini doner 
print(resim.size)#piksel sayisini doner 
print(resim.shape)#yuksel , genislik , ve kac tane renk kanalindan olusuyor (channel)
print(resim.dtype) #veriler hangi turde saklaniyor 
cv2.imshow("Brad Pitt",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2 

resim = cv2.imread("../Resimler/bradpitt.jpg",0)#resim eger gri olursa 

print(resim)#resim gri iken dondurulecek matris 
cv2.imshow("Brad Pitt",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2 

resim = cv2.imread("../Resimler/bradpitt.jpg",0)#resim eger gri olursa 

#print(resim.item(200,200),0)#pikselin degeri hangi BGR degerini icerdigi 0 -> mavi , 1 -> yesil , 2->kirmizi
#200 e 200 pikseldeki bgr degeri dondurur deger 0-255 arasindadir 

print(resim.item(100,200),0)#Blue
print(resim.item(100,200),0)#Green 
print(resim.item(100,200),0)#Red
cv2.imshow("Brad Pitt",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''