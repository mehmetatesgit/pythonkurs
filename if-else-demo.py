# name = input('İsminiz: ')
# year = int(input('Yaşınız: '))
# education = input('Öğrenim durumu: ')

# if ((year > 18) and (education == ('lise' or 'üni'))):
#     print(f'Sayın {name} ehliyet alabilirsiniz')
# else:
#     print('Malesef')

yazili1 = int(input('1.Sınav: '))
yazili2 = int(input('2.Sınav: '))
sozlu = int(input('Sözlü: '))

result = ((yazili1 + yazili2 + sozlu) / 3)

if ( 0 < result < 24):
    print('Notunuz sıfır')
elif ( 25 < result < 44):
    print('Notunuz bir')
elif ( 45 < result < 54):
    print('Notunuz iki')
elif ( 55 < result < 69):
    print('Notunuz üç')
elif ( 70 < result < 84):
    print('Notunuz dört')
else:
    print('Notunuz beş')