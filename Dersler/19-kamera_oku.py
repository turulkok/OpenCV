
import cv2
def ana():
    # kamera = cv2.VideoCapture(0)
    kamera = cv2.VideoCapture("../Videolar/tomandjerry.mp4")
    #VideoCapture fonksiyonuna istersek video dosyamizi istersekte kamera index imizi verebiliriz.
    # 0. kamera index i varsayilan kameramizdir.

    while(True):
        #videodan goruntu alma islemi
        ret, kare = kamera.read()

        #goruntu alindimi kontrol et alinmadiysa durdur
        if not ret: break
        cv2.imshow('kare',kare) #goruntuyu gosterme islemi
        cv2.moveWindow('kare',10,10)
        cv2.waitKey(0) #degerini sifir yaparsak kare kare yakalama islemini gerceklestirebiliriz.
        #cv2.waitKey(25) video oynamaya devam eder
    #kameranin acilip acilmadigin kontrol eder
    if kamera.isOpened():
        #VideoCapture Sinifini kapatir
        kamera.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    ana()























