
#kameradan alinan goruntuyu kaydetmek

import cv2

kamera = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*"XVID")  # .avi
# fourcc = cv2.VideoWriter_fourcc(*"MJPG")  # .jpeg
fourcc = cv2.VideoWriter_fourcc(*'m','p','4','v') # .mp4 uzantili. videonun kaydedilme algoritmasi fourcc

kayit = cv2.VideoWriter('kamera_kayit.mp4',fourcc,24.0,(640,480))
#cv2.VideoWriter(video adi,kaydedilme algoritmasi, saniyede alinan kare sayisi,cozunurluk boyutlari)

#kayit ne zaman baslayacak kamera acildi ise baslayacak
while kamera.isOpened():
    ret,video = kamera.read()
    if ret == True: # video varsa true yoksa false
        video = cv2.flip(video,1)#kameray dondurme islemi ters video 0 ters 1 duz
        kayit.write(video)
        cv2.imshow('goruntu',video)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

kamera.release()
kayit.release()
cv2.destroyAllWindows()















