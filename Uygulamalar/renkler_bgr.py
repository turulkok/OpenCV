# -*- coding: utf-8 -*-
#%% BGR renklerin kodlanmasi ve yazdirilmasi 

import cv2
import numpy as np #numpy kutuphanesinden bir modul kullanacagim zaman onu np adiyla cagirmayi ifade ediyor 

def bgr_renkler():
    img = np.ones((510,510,3),np.uint8)*80 

    
    '''
        circle fonksiyonu daire cizmeye yarar birinci deger nereye cizecegini belirtir.
        biz onceden img adinda bir pencere olusturduk gri renkte 
        ikinci parametre dairenin merkezinden sola ve uste olan uzakligini ifade eder
        ucuncu parametre radiustur yani dairenin yuvarlaklik derecesini ayarlar
        dorduncu parametre ise pozitif ise daireye dis cizgi ekler negatif ise dairenin disinda bir cizgi olmaz tam dolulukta daire cizilmis olur 
    '''
    
    cv2.circle(img,(90,90),80,(255,0,0),-1)
    
    cv2.circle(img,(250,90),80,(0,255,0),-1)
    cv2.circle(img, (410,90),80,(0,0,255),-1)

    cv2.circle(img,(90,250),80,(255,255,0),-1)
    cv2.circle(img,(250,250),80,(255,0,255),-1)
    cv2.circle(img,(410,250),80,(0,255,255),-1)
    
    cv2.circle(img,(170,410),80,(0,0,0),-1)
    cv2.circle(img,(330,410),80,(255,255,255),-1)
    
    #Dairelerin ortalarina renk degerlerini yazalim
    
    font = cv2.FONT_HERSHEY_SIMPLEX #opencvnin destekledigi fontlardan birisi ASCII destekli fontlar
    cv2.putText(img, '(255,0,0)', (15 + 30, 95), font, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, '(0,255,0)', (175 + 30, 95), font, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, '(0,0,255)', (335 + 30, 95), font, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, '(255,255,0)', (15 + 20, 250), font, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, '(255,0,255)', (175 + 20, 250), font, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, '(0,255,255)', (335 + 20, 250), font, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, '(0,0,0)', (95 + 40, 410), font, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, '(255,255,255)', (255 + 5, 410), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    '''
        putText fonksiyonun parametreleri:
        birinicisi Hangi görsele ekleyeceğimizi
        ikincisi Ne yazacağımızı
        üçüncüsü Görselin hangi kısmına ekleyeceğimizi
        dördüncüsü Hangi formatta yazacağımızı
        beşincisi Skalamızı ekliyoruz (boyut)
        altıncısı Hangi renk ile yazacağımızı
        yedincisi kalınlık belirtir
        sekizincisi lineType i belirtir(cizgi turu)- yazim turu gibi LINE_AA-8 ve 4 degerleri bulunmakta aralarinda ufak farkliliklar var
    '''

    cv2.imshow("imaj" , img)
    cv2.imwrite("OpenCV/Resimler/bgr_renkler.jpg",img)
    
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    bgr_renkler()
