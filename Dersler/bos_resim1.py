import numpy as np
import cv2

deneme = np.zeros((400,400,3),dtype=np.uint8)
#400x400 piksel boyutlarinda 3 renk kanalina sahip bir siyah pencere olusturur.
#bu resmi bir numpy matrisiyle olusturup icerisini sifir ile doldurduk.(np.zeros)
cv2.imshow('deneme',deneme)
cv2.waitKey(0)
cv2.destroyAllWindows()