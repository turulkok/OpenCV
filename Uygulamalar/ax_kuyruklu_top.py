# ax_kuyruklu_top.py

import cv2
import imutils
from collections import deque
import numpy as np


GENISLIK = 800  # GENISLIK
NOKTA_SAYISI=100 #cizgiyi olusturan nokta sayisinin max 100 olmasini istiyoruz
YESIL = ((29, 86, 6), (64, 255, 255))
KIRMIZI = ((139, 0, 0), (255, 160, 122))
MAVI = ((110, 50, 50), (130, 255, 255))
TURUNCU = ((160, 100, 47), (179, 255, 255))
SARI = ((10, 100, 100), (40, 255, 255))

altRenk, ustRenk = MAVI


kamera = cv2.VideoCapture(0)


noktalar= deque(maxlen=NOKTA_SAYISI) #boru mekanizmasi
#deque(doubly ended queue) - cift uclu kuyruk hizli ekleme islemi yapar o yuzden listeye gore tercih edilir
cv2.namedWindow('kare')
cv2.moveWindow('kare', 10, 10)
while True:
    (ok, kare) = kamera.read()

    kare = imutils.resize(kare, GENISLIK)
    hsv = cv2.GaussianBlur(kare, (25,25), 0)
    hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)

    maske = cv2.inRange(hsv, altRenk, ustRenk)
    maske = cv2.erode(maske, None, iterations=1)
    maske = cv2.dilate(maske, None, iterations=1)
    kopya = maske.copy()

    _,konturlar,_ = cv2.findContours(kopya, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
    merkez = None
    if len(konturlar) > 0:
        cmax = max(konturlar, key=cv2.contourArea)#konturlarin icerisinde en buyuk alana sahip olani bulur
        for ctr in konturlar:
            (x, y), yaricap = cv2.minEnclosingCircle(cmax)#cmax'i icerisine alabilecek en kucuk cember
            #minEnclosingCircle 2 ciktisi var birisi merkez birisi yaricap
            mts = cv2.moments(cmax) #agirlik hesaplama araci
            merkez = int(mts['m10']/mts['m00']),\
                     int(mts['m01']/mts['m00'])
            #agirlik merkezi hesaplama islemi
            if yaricap >= 30: #nesnemizin yaricapi 30dan buyukse etrafina daire ciz demis olduk
                cv2.circle(kare, (int(x), int(y)),
                           int(yaricap), (255, 255, 0), 4)
                #cv2.circle(imaj,merkez,yaricap,renk,kalinlik)
            noktalar.appendleft(merkez)#appenleft soldan eklemeye basla demek
            for i in range(1,len(noktalar)):
                if noktalar[i] and noktalar[i-1]:

                    cizgi_kal=2 #cizgi kalinligini sabitleme islemi
                    cv2.line(kare,noktalar[i-1],
                             noktalar[i],(0,255,255),cizgi_kal)
                    #kare uzerine cizilecek noktalar[i-1] ile noktalar[i] arasinda sari renginde ve cizgi kalinligi 2

    cv2.imshow("kare", kare)


    key = cv2.waitKey(10) & 0xFF
    if key == ord('q') or key == 27:
        break

kamera.release()
cv2.destroyAllWindows()

