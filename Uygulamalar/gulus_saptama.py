import cv2

yuzCascade = cv2.CascadeClassifier(
    '../Cascades/haarcascade_frontalface_default.xml'
)

gulCascade = cv2.CascadeClassifier(
    '../Cascades/haarcascade_smile.xml'
)

kamera = cv2.VideoCapture(0)
kamera.set(3,640)
kamera.set(4,480)


while True:
    _, kare = kamera.read()
    kare = cv2.flip(kare,1)
    gri = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    yuzler = yuzCascade.detectMultiScale(
        gri,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x,y,w,h) in yuzler:
        cv2.rectangle(kare, (x, y), (x + w, y + h), (255, 0, 0), 2)
        gri_kutu = gri[y:y+h, x:x+w]
        renkli_kutu = kare[y:y+h, x:x+w]

        gulusler = gulCascade.detectMultiScale(
            gri_kutu,
            scaleFactor=1.5,
            minNeighbors=18,
            minSize=(30,30)
        )

        for (sx,sy,sw,sh) in gulusler:
            cv2.rectangle(renkli_kutu,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
    cv2.imshow('kare',kare)

    k = cv2.waitKey(10) & 0xff
    if k == 27 or k == ord('q'):  # press 'ESC' or 'q' to quit
        break
kamera.release()
cv2.destroyAllWindows()
