import cv2

deltax = 0
deltay = 0

imaj = cv2.imread('../Resimler/pou400.png')
# (imaj,kernel_boyutu)
blur = cv2.medianBlur(imaj,11)# tek sayi olmak zorunda

cv2.imshow('imaj',imaj)
cv2.imshow('medianBlur',blur)
cv2.moveWindow('imaj',10,10)
cv2.moveWindow('medianBlur',blur.shape[1]+deltax,10)

cv2.waitKey(0)
cv2.destroyAllWindows()