import cv2

deltax = 0
deltay = 0

sthrs = ['cv2.THRESH_BINARY','cv2.THRESH_BINARY_INV',
         'cv2.THRESH_TRUNC', 'cv2.THRESH_TOZERO',
         'cv2.THRESH_TOZERO_INV', 'cv2.THRESH_MASK',
         'cv2.THRESH_OTSU','cv2.THRESH_TRIANGLE']
thrs = [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC,
        cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV, cv2.THRESH_MASK,
        cv2.THRESH_OTSU, cv2.THRESH_TRIANGLE]
print(thrs)
gri = cv2.imread('../Resimler/gradient.jpg',cv2.IMREAD_GRAYSCALE)
gri = cv2.resize(gri,(int(gri.shape[1]/gri.shape[0]*400),400))

#
x = 10; y = 10
cv2.imshow('gri',gri)
cv2.moveWindow('gri',x,y)
x = 45;
for j in range(len(thrs)):
    #burada yapilan islem acilan pencereler ekran boyutuna ulastiginda alt satira gecmesini saglamak
    x += gri.shape[1] + deltax
    if x>1600: #1600 ekran genisligi
        x = 45;y += gri.shape[0] + deltay
    ret,esik = cv2.threshold(gri,128, 255,thrs[j])
    #(gri_imaj, esik_degeri, max_degeri, esik_tipi)
    #esik_degeri : 0 - 255
    #max_deger : 0 - 255
    #geriye iki deger dondurur birincisi esik degeri ikinicisi yeni olusan esik goruntusudur.
    #ret : cv2.THRESH_OTSU kullanilirsa hesaplanan esik degeri, yoksa verilen esik degeri
    '''

    Parameters
        src	: giriş dizisi (çok kanallı, 8 bit veya 32 bit kayma noktasi).
        thresh : esik degeri.
        maxval : THRESH_BINARY ve THRESH_BINARY_INV ile kullanilacak esikleme degeri.
        type : esik turu.
    '''
    print('ret = ',ret)
    cv2.imshow(sthrs[j],esik)
    cv2.moveWindow(sthrs[j],x,y)

cv2.waitKey(0)
cv2.destroyAllWindows()