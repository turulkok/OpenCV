import cv2

deltax = 0
deltay = 0

imaj = cv2.imread('../Resimler/pou400.png')
# (imaj, kernel)
blur = cv2.blur(imaj,(5,5))
#kernel (cekirdek) boyutu arttilirdikca detaylarin kaybolmasi durumu artar
cv2.imshow('imaj',imaj)
cv2.imshow('blur',blur)
cv2.moveWindow('imaj',10,10)
cv2.moveWindow('blur',imaj.shape[1]+deltax,10)

cv2.waitKey(0)
cv2.destroyAllWindows()