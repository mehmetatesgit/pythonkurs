'''
    1-100 rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
    buldurmaya çalışın. (hak = 5)

    ** "random modülü" 
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
    üzerinden hesaplansın.
'''

import random

sayi = random.randint(1,10)
can = int(input('Kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    tahmin = int(input('Tahmin: '))
    sayac += 1
    if sayi == tahmin:
        print(f'Tebrikler {sayac}. seferde bildiniz. Toplam puanınız: {100 - (100 / can) * (sayac - 1)} ')
        break
    elif sayi > tahmin:
        print('Yukarı')
    else:
        print('Aşağı')
    
    if hak == 0:
        print(f'Hakkınız bitti. Tutulan sayı : {sayi}')
