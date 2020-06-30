sayilar = [1,3,5,7,9,12,19,21]

#Sayılar listesindeki hangi sayılar 3ün katıdır.

# for number in sayilar:
#     if (number % 3 == 0):
#         print(f'{number} 3ün katıdır. ')
#     else:
#         print(f'{number} 3ün katı değildir. ')

#Sayılar listesindeki sayıların toplamı kaçtır.

# toplam = 0   

# for number in sayilar:
#     toplam += number
# print(f'Toplam: {toplam}')

#Sayılar listesindeki tek sayıların karesini alınız.

# for number in sayilar:
#     if (number % 2 == 1):
#         print('karesi', number ** 2)


sehirler = ['kocaeli', 'ankara', 'istanbul', 'izmir', 'rize']

#Hangileri en fazla 5 karakterlidir.

# for city in sehirler:
#     if (len(city) <= 5):
#         print(city)


urunler = [
    {'name': 'samsung s6', 'price': '3000'},
    {'name': 'samsung s7', 'price': '4000'},
    {'name': 'samsung s8', 'price': '5000'},
    {'name': 'samsung s9', 'price': '6000'},
    {'name': 'samsung s10', 'price': '7000'}
]

#Ürünlerin fiyatları toplamı nedir.
# toplam = 0

# for urun in urunler:
#     fiyat = int((urun['price']))
#     toplam += fiyat
# print(toplam)

for urun in urunler:
    fiyat = int((urun['price']))
    if(fiyat <= 5000):
        print(fiyat)
