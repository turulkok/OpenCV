import cv2

cember = True
#resmi okumak
kare = cv2.imread('../Resimler/paralar04.jpg')
#ayrintilari kaybetmek (resmi yumusatmak)
blur = cv2.GaussianBlur(kare,(3,3),0)
#kenarlari bulmak icin
canny = cv2.Canny(blur,30,250)
#cv2.imshow("Canny",canny)
#cv2.waitKey(0)
#cekirdik boyutu getStructuringElement yapilandirma elemanin olusmasini saglar
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
#morphologyEx islemi hem resme hem erosion hem dilation islemi uygular
morf = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)
#cv2.imshow('morf',morf)
#cv2.waitKey(0)
#sinirlarin bulunmasi
konturlar = cv2.findContours(morf.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) [-2]
#bulunan nesneler baslangicta 0
say = 0
#konturlar bir liste elemani
for kontur in konturlar:
    #alanlarin bulunmasi
    alan = cv2.contourArea(kontur)
    #alan degeri belirli bir boyuttan fazlaysa sayma islemini gerceklestir
    if alan > 10000:
        print(alan)
        say+=1
        #seklin sag ust sinirlayici dortgenini tutar
        (x,y,w,h) = cv2.boundingRect(kontur)
        #dikdortgen cizme islemi
        cv2.rectangle(kare,(x,y),(x+w,y+w),(0,255,0),2)
        #cember ifademiz true idi yani dikdortgen varsa o bizim icin paranin oldugu alandir
        if cember:
            #cember sinirlarinin bulunmasi islemi
            (x,y), ycap = cv2.minEnclosingCircle(kontur)
            merkez = (int(x),int(y))
            ycap = int(ycap)
            #dairenin cizilmesi islemi
            img = cv2.circle(kare,merkez,ycap,(255,0,0),2)
#bozukluklari sayma islemi
if say > 0:
    cv2.putText(kare,f"{say} bozukluk bulundu",(10,80),cv2.FONT_HERSHEY_SIMPLEX,1,1)

cv2.imshow('kare',kare)
cv2.waitKey(0)