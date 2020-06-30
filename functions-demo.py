# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonsiyonu yazın.
'''
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir('merhaba\n', 10)

'''

# 2- Kendine gönderilen sınırsız sayıda parametreyi bir listeye ceviren fonksiyonu yazın.

def listeyeCevir(*args):
    liste = []
    for param in args:
        liste.append(param)
    
    return liste

result = listeyeCevir(10,20,30,'Merhaba')
print(result)

# 3- Gönderilen 2 sayı arasındaki asal sayıları bulun.
'''
def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                   break
            else:
                print(sayi)

sayi1 = int(input('sayı 1 : '))
sayi2 = int(input('sayı 2 : '))

asalSayilariBul(sayi1, sayi2)

'''

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste seklinde döndürün.

def bolenBul(sayi):
    liste = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            liste.append(i)
    return liste
    

print(bolenBul(20))

