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


    cv2.imshow("imaj",img)
    cv2.imwrite("OpenCV/Resimler/bgr_renkler.jpg",img)
    
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    bgr_renkler()
