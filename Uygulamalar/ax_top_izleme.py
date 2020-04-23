import cv2
import imutils

deltax = 0
deltay = 0


GENISLIK = 600
SADECE_MAX = False
#renk araliklarimiz
YESIL = ((29,86,6),(64,255,255))
KIRMIZI = ((139,0,0),(255,160,122))
MAVI = ((110,50,50),(130,255,255))
TURUNCU = ((160,100,47),(179,255,255))
SARI = ((10,100,100),(40,255,255))

altRenk, ustRenk = SARI



kamera = cv2.VideoCapture(0)

cv2.namedWindow('kare')
cv2.moveWindow('kare',10,10)
cv2.namedWindow('maske')
cv2.moveWindow('maske',GENISLIK+deltax,10)

while True:
    (ok,kare) = kamera.read()

    kare = imutils.resize(kare,GENISLIK) #en boy oraninin korunmasini saglar genislik degerine gore yuksekligi oranliyor
    hsv = cv2.GaussianBlur(kare,(25,25),0) # detaylari azaltmak icin bulaniklastirma
    hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)#bgrdan HSV'ye donusturme islemi

    maske = cv2.inRange(hsv,altRenk,ustRenk)#deger araliklari
    maske = cv2.erode(maske,None,iterations=3)
    maske = cv2.dilate(maske,None,iterations=3)
    kopya = maske.copy()


    sonuc = cv2.bitwise_and(kare,kare,mask= maske)
    cv2.imshow('kare',kare)
    cv2.imshow('maske',maske)
    cv2.imshow('sonuc',sonuc)

    cv2.waitKey(4)

kamera.release()
cv2.destroyAllWindows()