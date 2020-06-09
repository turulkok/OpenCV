import cv2

deltax = 0
deltay = 0

kamera = cv2.VideoCapture(0)
kamera.set(3,640) #3 genislik
kamera.set(4,480) #4 yuksekligi ifade eder

while True:
    ret, kare = kamera.read()
    kare = cv2.flip(kare,1)
    gri = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY) #griye cevirme islemi
    blur = cv2.GaussianBlur(gri,(7,7), 0 ) #bulaniklastirma islemi-ayrintilari azaltmak icin ve canny'nin daha iyi sonuc vermesi icin
    canny = cv2.Canny(blur,30,50)#kenarlar tespiti icin
    canny = cv2.bitwise_not(canny)
    #bitwise_not() dizinin herbir elemanini terse cevirir
    imaj = cv2.bitwise_and(kare,kare,mask = canny)
    #iki resmin bitsel olarak birlesimini saglar
    cv2.imshow('imaj',imaj)
    cv2.moveWindow('imaj',10,10)
    cv2.imshow('canny',canny)
    cv2.moveWindow('canny',imaj.shape[1]+deltax,10)

    cv2.waitKey(25)

kamera.release()
cv2.destroyAllWindows()