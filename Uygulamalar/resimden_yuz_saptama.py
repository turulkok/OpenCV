import cv2

foto = cv2.imread('../Resimler/millitakim.jpg')
gri = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

#siniflandirici yuklenmesi
yuz_belirleme = cv2.CascadeClassifier(
    '../Cascades/haarcascade_frontalface_default.xml')

yuzler = yuz_belirleme.detectMultiScale(gri,1.5,5)

for (x,y,w,h) in yuzler:
    cv2.rectangle(foto,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow('foto',foto)
cv2.waitKey(0)
cv2.destroyAllWindows()
