import cv2

deltax = 0
deltay = 0

imaj = cv2.imread('../Resimler/pou400.png')

#(imaj,kernel,standart sapma)
blur = cv2.GaussianBlur(imaj,(11,11),0) #pozitif tek sayi

cv2.imshow('imaj',imaj)
cv2.imshow('GaussianBlur',blur)
cv2.moveWindow('imaj',10,10)
cv2.moveWindow('GaussianBlur',imaj.shape[1]+deltax,10)
cv2.waitKey(0)
cv2.destroyAllWindows()