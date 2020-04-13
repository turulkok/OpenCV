import cv2

#cozunurlukler
cozwh = [(1920,1080),(1600,900),(1366,768),(1280,720),
         (1024,576),(960,544),(640,480),(320,240)]

def ana():
    kamera = cv2.VideoCapture(0)
    for j in range(len(cozwh)): #cozunurlukler
        w0 = int(cozwh[j][0])#genislik
        h0 = int(cozwh[j][1])#yukseklik degerleri sirasiyla hep denenecek

        kamera.set(3,w0) #genislik w0 genislik
        kamera.set(4,h0) #yukseklik h0 yukseklik

        #kameranin olusan cozunurluk degerleri (VideoCapture ozellikleri )
        #desteklenen boyutlara gore degisim saglar
        w1 = kamera.get(3)
        h1 = kamera.get(4)

        #print(f"Test: ({w0},{h0}) sonuc: ({w1},{h1})")
        print("Test: ({},{}) sonuc: ({},{})".format(w0,h0,w1,h1))

    if kamera.isOpened():
        kamera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    ana()



























