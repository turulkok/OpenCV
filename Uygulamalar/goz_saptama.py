import cv2
yuzCasCade = cv2.CascadeClassifier(
    '../Cascades/haarcascade_frontalface_default.xml'
)
gozCascade = cv2.CascadeClassifier(
    '../Cascades/haarcascade_eye.xml'
)
kamera = cv2.VideoCapture(0)
while True:
    _, kare = kamera.read()
    kare = cv2.flip(kare,1)
    gri = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    yuzler = yuzCasCade.detectMultiScale(
        gri,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20,20)
    )
    for (x,y,w,h) in yuzler:
        cv2.rectangle(kare, (x, y), (x + w, y + h), (255, 0, 0), 2)
        gri_kutu = gri[y:y+h,x:x+w] # y'den (y+h)'ye kadar ve x'den (x+w)'ye kadar
        renkli_kutu = kare[y:y+h, x:x+w]

        gozler = gozCascade.detectMultiScale(gri_kutu)
        for (ex,ey,ew,eh) in gozler:
            cv2.rectangle(renkli_kutu, (ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('kare',kare)

    k = cv2.waitKey(10) & 0xff
    if k == 27 or k==ord('q'):break

kamera.release()
cv2.destroyAllWindows()