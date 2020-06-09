import cv2
import numpy as np

# altRenk = np.array([30,60,60])
# ustRenk = np.array([64,255,255])
# RENK='YESIL'
# altRenk=(10, 100, 100)
# ustRenk=(40, 255, 255)
# RENK='SARI'
# altRenk=(170, 100, 100)
# ustRenk=(190, 255, 255)
# RENK='KIRMIZI'
altRenk=(75, 100, 100)
ustRenk=(130, 255, 255)
RENK='MAVi'

kamera = cv2.VideoCapture(0)
#cozunurlugun ayarlanmasi
kamera.set(3,640)
kamera.set(4,480)
cember = True

while True:
    if not kamera.isOpened():break #kamera kontrolu
    _, kare = kamera.read()
    #Bgr renk uzayindan hsv renk uzayina cevirme islemi
    hsv = cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)
    #deger araliklari
    maske = cv2.inRange(hsv,altRenk,ustRenk)
    #cekirdek boyutunun belirlenmesi
    kernel = np.ones((5,5),'int')

    maske = cv2.dilate(maske,kernel)#genisletme islemi
    #konturlarin bulunmasi
    konturlar = cv2.findContours(maske.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # cv2.findContours(orjinal imaj = imaj, mod = cv2.RETR_EXTERNAL, metod = cv2.CHAIN_APPROX_SIMPLE)
    # mod : kontur bulma yontemi (RETR_LIST,RETR_EXTERNAL,RETR_CCOMP,RETR_TREE)
    # metod : kontur yaklasim yontemi (approximation)
    say = 0

    for kontur in konturlar:
        #alan bulma islemi
        alan = cv2.contourArea(kontur)
        #alan 600'den buyukse
        if alan > 600:
            #nesne sayisini 1 arttir
            say += 1
            #boundingRect Bir nokta kümesinin sağ üst sınırlayıcı dikdörtgenini hesaplar.
            (x,y,w,h) = cv2.boundingRect(kontur)
            #dikdortgen cizme islemi
            cv2.rectangle(kare,(x,y),(x+w,y+h),(0,255,0),2)
            #cember true ise yukarida true yaptik
            if cember:
                #en kucuk cemberin merkezini ve capini buluyor
                (x,y), ycap = cv2.minEnclosingCircle(kontur)
                merkez = (int(x),int(y))
                ycap = int(ycap)
                #cember cizme islemi
                img = cv2.circle(kare,merkez,ycap,(255,0,0),2)
    #sayi 0'dan buyukse ekrana ve terminale yazi yazdir
    if say > 0:
        cv2.putText(kare,f"{say} {RENK} nesne bulundu",(10,80), cv2.FONT_HERSHEY_SIMPLEX,1,1)

    cv2.imshow('kare',kare)
    k = cv2.waitKey(4) & 0xFF
    if k == 27: break

if kamera.isOpened():
    kamera.release()
cv2.destroyAllWindows()
