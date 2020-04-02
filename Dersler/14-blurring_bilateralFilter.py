import cv2

deltax = 0
deltay = 0

imaj = cv2.imread('../Resimler/pou400.png')
# (imaj,komsuluk_capi,sigma_renk,sigma_uzay)
blur = cv2.bilateralFilter(imaj,11,175,175)
# ne kadar uzak renklerin birbirine karistirilacagini belirler
'''
cv2.bilateralFilter(imaj, boyut, sigmaColor(piksel renk araliklari), sigmaSpace(piksel renk araliklari))
'''

cv2.imshow('imaj',imaj)
cv2.imshow('bilateralFilter',blur)
cv2.moveWindow('imaj',10,10)
cv2.moveWindow('bilateralFilter',blur.shape[1]+deltax,10)

cv2.waitKey(0)
cv2.destroyAllWindows()