#Girilen bir sayının 0 ile 100 arasında olduğunu kontrol ediniz.

# x = int(input('Bir sayı giriniz: '))

# result = ((x > 0 and x < 100))

#Girilen sayının pozitif çift sayı olduğunu kontrol ediniz.

# x = int(input('Bir sayı giriniz: '))

# result = ((x > 0) and (x % 2 == 0))

#email ve parola bilgilerini kontrol ediniz.

# email = 'ates@gmail.com'
# password = '123456'

# girilenEmail = input('Email: ')
# girilenPass = input('Parola: ')

# result = ((girilenEmail == email) and (girilenPass == password))

#Girilen 3 sayıyı karşılaştırınız.

# a = int(input('1. sayı: '))
# b = int(input('2. sayı: '))
# c = int(input('3. sayı: '))

# result = (a > b) and (a > c)

# print(f'a en büyük sayıdır. {result}')

# result1 = (b > a) and (b > c)

# print(f'b en büyük sayıdır. {result1}')

# result2 = (c > b) and (c > a)

# print(f'c en büyük sayıdır. {result}')

#Kullanıcıdan 2 vize %60 ve final %40 notu alın ortalamasını hesaplayın
#       Eğer kullanıcı 50 ve üstündeyse geçti değilse kaldı yazdırın.

vize1 =  float(input('1. vize: '))
vize2 =  float(input('2. vize: '))
final =  float(input('final: '))

ortalama = (((vize1 + vize2) / 2 ) * 0.6) + (final * 0.4)

result = (ortalama >= 50) and (final >= 50)

print(f'Öğrencinin ortaması: {ortalama} ve geçme durumu: {result} ')

#       a) Ortalama 50 olsa bile final notu en az 50 olmalıdır
#       b) Finalden 70 alındığında ortalamanın bir önemi olmasın

#Kişinin ad. kilo ve boy bilgilerini alıp indekslerini hesaplayın
#   0-18,4 = zayıf   18,5 - 24,9 normal  25 - 29,9 = fazla kilolu 30 - 34,9 = şişman



# print(result)