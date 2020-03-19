# -*- coding: utf-8 -*-
#%% Resim Acma,Resim Okuma,Resim Yazma

import cv2


resim = cv2.imread("../Resimler/seinfield.jpg")#resmi numpy dizisine donusturmeye yarar
#imread in ikinci parametresini 0 yaparsak resmi gri yapar yapmazsak normal bir sekilde acar 
#her piksel 3 rengin karisimindan olusur k,y,m kombinasyonlarindan eger bir resme rgb degeri atamazsak resim gri olur burada yapilan islemde bu 
cv2.imwrite("../Resimler/seinfield_gri.jpg",resim)#grilestirdigimiz resmi kaydetmemizi saglar 
#print(type(resim))#resim ne objesi 

cv2.imshow("Seinfield Resmi",resim)#ilk parametre pencere ismi , digeride resmimiz 

cv2.waitKey(0)#herhangi bir tusa basmamizi bekleyen fonksiyon,resmin ekranda kalma suresidir sifir degeri verilirse herhangi bir tusa basmadan calismaz 

cv2.destroyAllWindows()#open cvye bagli acik butun pencerelerin kapanmasini saglar
#

