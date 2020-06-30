sayilar = [1,3,5,7,9,12,19,21]

#sayilar listesini while döngüsü ile ekrana yazdırın.

# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1

#Başlangıç ve bitiş değerlerini alıp aradaki tek sayıları yazdırın.

# deger1 = int(input('1.Deger: '))
# deger2 = int(input('2.Deger: '))

# x = deger1
# while (x <= deger2):
#     if (x % 2 == 1):
#         print(x)
#     x += 1

#1-100 arasındaki sayıları azalan şekilde yazdırın.

# x = 100

# while x > 1:
#     print(x)
#     x -= 1

#Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

# number = []

# i = 0

# while i < 5:
#     sayi = int(input('Sayı giriniz: '))
#     number.append(sayi)
#     i += 1
# number.sort()
# print(number)


urunler = []

adet = int(input('kaç ürün eklemek istersiniz: '))

i = 0

while (i < adet):
    name = input('ürün ismi: ')
    price = input('fiyat')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]}  fiyatı: {urun["price"]}')