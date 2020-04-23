import cv2
import numpy as np

deltax = 0
deltay = 0

kamera = cv2.VideoCapture(0)

kamera.set(10, 0.8)#parlaklik

while True:
    ret, kare = kamera.read()
    kare = cv2.flip(kare,1)
    ycrcb = cv2.cvtColor(kare, cv2.COLOR_BGR2YCrCb)#bgr renk uzayinin YCrCb'ye donusturuyoruz.
    ycrcb = cv2.inRange(ycrcb, (0,137,85),(255,180,135))#renk araliginin tanimlanmasi
    #morphologyEx() fonksiyonu kendi icerisinde hem erode hem dilate islemini yapar
    ycrcb = cv2.morphologyEx(ycrcb,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))

    '''
    cv2.morphologyEx()
    Parameters
        src	= Kaynak goruntu
        op = Morfolojik operasyon tipi
        kernel = Yapilandirma elemani, morfolojik islemlerin yapilacagi boyut
    '''
    ycrcb = cv2.medianBlur(ycrcb, 5)
    #kucuk ayrintilarin kaybolmasi icin bulaniklastirma islemini yapiyoruz
    sonuc = cv2.bitwise_and(kare,kare,mask = ycrcb)
    #burada bitwise_and arkaplanin siyah olmasi icin kullaniliyor(maskeleme islemi)
    #cv2.imshow('kare',kare)
    #cv2.imshow('maske',ycrcb)
    cv2.imshow('sonuc',sonuc)
    #cv2.moveWindow('kare',10,10)
    #cv2.moveWindow('maske',10,kare.shape[0])
    cv2.moveWindow('sonuc',10,10)

    cv2.waitKey(25)

kamera.release()
cv2.destroyAllWindows()

'''
Morfolojik filtreler genelde iki temel işlemden türetilmiştir.
Bunlar erosion ( aşındırma ) ve dilation ( genişletme ) işlemleridir.
Aşındırma ikili bir görüntüde bulunan nesnelerin boyutunu seçilen yapısal
elemente bağlı olarak küçültürken, genişletme nesnenin alanını artırır.
Bu işlemlerden erosion işlemi birbirine ince bir gürültü ile bağlanmış iki
veya daha fazla nesneyi birbirinden ayırmak için kullanılırken, dilation
işlemi ise aynı nesnenin bir gürültü ile ince bir şekilde bölünerek ayrı
iki nesne gibi görünmesini engellemek için kullanılır.
'''