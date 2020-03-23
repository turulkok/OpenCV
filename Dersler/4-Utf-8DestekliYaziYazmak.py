# turkce.py

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import sys

# Türkçe karakterleri de yazabilmek icin pillow kutuphanesini kullaniyoruz
# pillow kutuphanesi bir goruntu isleme kutuphanesidir.Python da goruntu islemleri yapilabilmesi icin olusturulmustur.
def print_utf8_text(image, text, fontName='DejaVuSerif',
            color=(0,0,0), yer=(10,10), boy=48):
    font = ImageFont.truetype(fontName, boy)  # font adi ve boyutu
    pilImg = Image.fromarray(image)  # imajı pillow moduna çevir
    #Image opencv de BGR renk uzayini kullaniyor ancak PIL RGB uzayini kullandigi icin onun cevirimini yapiyoruz.
    draw = ImageDraw.Draw(pilImg)  # imajı hazırla
    #ImageDraw basit iki boyutlu grafik olusturulmasini saglar
    #burada yapilan pilimg'i cizmek

    draw.text((yer[0], yer[1]), text,
              fill=(color[0], color[1], color[2],0),font = font)


    image = np.array(pilImg)  # resmi tekrar opencv'nin kullanabilecegi moda (BGR) ceviriyoruz
    return image
'''

    PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None)
        Parameters:
            xy –metnin sol ust kosesi
            text – cizilecek metin
            fill – metin icin kullanilacak renk
            font – ImageFont ornegi
'''




if __name__ == "__main__":


    imaj = np.ones((400, 700, 3), dtype=np.uint8) * 255#beyaz bir zemin olusturak icin



    fontName='verdana.ttf'; renk = (0, 0, 0); yer = (10,10); boy = 64#sirayla deger atama islemleri.
    #ayni satirda yazdigimiz icin aralara ; koyduk
    imaj = print_utf8_text(imaj, "Ağaç ", fontName,
                               renk, yer, boy)
    #fonksiyonumuzun icerisine parametrelerimizi gonderiyoruz
    # ve ayni islemleri farkli yazilar yazmak icin tekrarliyoruz

    fontName = 'tahoma.ttf'
    renk = (0, 0, 255); yer = (100,120); boy = 36
    imaj = print_utf8_text(imaj, "Tuğrul Şahin Kök ", fontName,
                               renk, yer, boy)

    fontName = 'times.ttf'; renk = (128, 0, 0)
    yer = (30,200); boy = 48
    imaj = print_utf8_text(imaj,
        "LACİVERT ", fontName, renk, yer, boy)

    fontName = 'times.ttf'; renk = (0, 255, 0)
    yer = (10,300); boy = 42
    imaj = print_utf8_text(imaj, "Ömer ", fontName, renk, yer, boy)

    cv2.imshow('beyaz fon', imaj)
    cv2.moveWindow('beyaz fon', 10, 10)# pencerenin x,y duzleminde nerede acilacagini belirtir

    cv2.waitKey(0)
    cv2.destroyAllWindows()

