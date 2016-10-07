# -*- coding: utf-8 -*
"""
Yazar: Ahmet Aksoy
Sürüm: Python 3.5.2 ile derlenmiştir.
Tarih: 07.10.2016
Rev. : 07.10.2016
Bu script, yedek_cfg.py dosyasında tanımlanan dizinlerdeki uzantısı verilen dosyaların
kopyalarını yedek dizin/dosya şeklinde saklayacak. Eski dosya isimlerine
yedeklenme tarih ve saatleri eklenecek.
"""

from yedek_cfg import *
import os
import time, datetime
import hashlib
import shutil

BUFFER = 65536

#def damgatar(): return datetime.datetime.now().strftime('%Y%m%d-%H:%M:%S.%f')
def damgatar():
    return datetime.datetime.now().strftime('%Y%m%d%H%M')

def get_hash(d):
    hashx = hashlib.sha1()
    with open(d, 'rb') as afile:
        buf = afile.read(BUFFER)
        while len(buf) > 0:
            hashx.update(buf)
            buf = afile.read(BUFFER)
    return hashx.hexdigest()

def txt_dosyabul(klasor):
    liste = []
    for dir, dirs, files in os.walk(klasor):
        for dosya in files:
            for uz in UZANTILAR:
                if dosya.endswith(uz):
                    liste.append(dosya)

    return klasor, liste

def main():
    dosyasay = 0
    for adizin in ALT_DIZINLER:
        klasor, dosyalar = txt_dosyabul(ANA_DIZIN+adizin)
        for d in dosyalar:
            dosyasay +=1
            s=klasor+d
            #print(dosyasay, s)
            print(s)
            hash1 = get_hash(s)
            s2 = YEDEK_DIZIN+adizin+d
            print(s2)
            h2=-1
            if os.path.exists(s2):
                hash2 = get_hash(s2)
            # Eğer her iki hash değeri aynıysa, son kopya ile orijinal de aynıdır
            if hash1 == hash2:
                print("Orijinal dosyada değişiklik yok")
                continue
            # yedek dosya yoksa hemen kaydet
            if os.path.exists(s2):
                print("Eski dosyanın adını değiştir")
                s3 =YEDEK_DIZIN+adizin+damgatar()+d
                shutil.move(s2,s3)
            # yedek varsa ama hashler tutmuyorsa
            # eski dosyanın adını değiştir, yenisini kaydet
            print("Yeni dosyayı kopyala")
            # dizin yoksa, oluştur
            if not os.path.exists(YEDEK_DIZIN+adizin):
                os.mkdir(YEDEK_DIZIN+adizin)
            shutil.copy(s,s2)
if __name__ == "__main__":
    main()
