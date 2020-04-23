import cv2

#siniflandirici yuklenmesi
yuzCascade = cv2.CascadeClassifier(
    '../Cascades/haarcascade_frontalface_default.xml')
kamera = cv2.VideoCapture(0)

while True:
    _, kare = kamera.read() #kameradan okuma islemi
    #ilk deger _ frame in dogru okunup okunmadigini kontrol eder (true-false)
    #ikinci deger kare yakalanan kareyi ifade eden narraydir
    kare = cv2.flip(kare,1)#kamera ters ise -1 , aynalama icin 1
    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)#griye cevirme islemi
    #yuz saptama islemini gri tonlamada yapiyoruz

    # detectMultiScale goruntu icerisinde birden fazla yuz varsa onlari yakalar
    yuzler = yuzCascade.detectMultiScale(
        gri,
        scaleFactor = 1.2,#Her görüntü ölçeğinde görüntü boyutunun ne kadar azaltılacağını belirten parametre.
        minNeighbors = 5,#Her aday dikdörtgenin kaç tane komşu tutması gerektiğini belirten parametre.
        minSize = (20, 20)# mumkun olan en kucuk nesne boyutu bundan kucukleri gozardi edilir
    )
    #detectMultiScale Giriş görüntüsünde farklı boyutlardaki nesneleri algılar.
    # Algılanan nesneler dikdörtgenler listesi olarak döndürülür.

    #(x,y) => sol ust kose koordinalari (w,h) => genislik ve yukseklik
    for (x,y,w,h) in yuzler:
        # rectangle dikdortgen cizme islemi yapar
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),2)
        #cv2.rectangle(dikdortgeni cizecegi alan,yuzun basladigi sol ust kosesi, yukseklik ve genisligi,
        #dikdortgen rengi, cizgi kalinligi)

    cv2.imshow('kare',kare) # goruntuleme islemi
    k = cv2.waitKey(1) & 0xff
    if k == 27 or k==ord('q'):break

kamera.release()
cv2.destroyAllWindows()