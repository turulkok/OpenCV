import cv2
#Nesne kenarlarinin saptanmasi
deltax = 0
deltay = 0
imaj1 = cv2.imread('../Resimler/bina.jpg')
imaj = cv2.resize(imaj1,(500,500))
kenarlar = cv2.Canny(imaj, 50, 150)
#geri dondurulen kenar haritasi
'''
cv2.Canny()
    Parameters:
        image – tek kanalli 8 bit giris goruntusu.
        threshold1 – kesiklik islemi icin ilk esik
        threshold2– kesiklik islemi icin ikinci esik
'''
maske = cv2.bitwise_not(kenarlar)
# bitwise_not() Bir dizinin her bitini tersine çevirir.
# parametresi giris arrayi
maske = cv2.erode(maske,(5,5),iterations = 2)
# erode kenarlari inceltme islemi

#maske = kenarlar

imaj2 = cv2.bitwise_and(imaj,imaj,mask = maske)
#bitwise_and iki resmin (maske ve imaj) bitsel birlesimini saglar
cv2.imshow('imaj',imaj)
cv2.imshow('maske',maske)
cv2.imshow('imaj2',imaj2)
cv2.moveWindow('imaj',10,10)
cv2.moveWindow('maske',imaj.shape[1] + deltax,10)
cv2.moveWindow('imaj2',imaj.shape[1] + maske.shape[1] + deltax, 10)

cv2.waitKey(0)
cv2.destroyAllWindows()
