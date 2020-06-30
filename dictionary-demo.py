ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    },
}

ogrenciler = {}

number = input("Öğrenci no: ")
name = input("İsim: ")
surName = input("Soyad: ")
phone = input("Telefon no: ")

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surName,
#     'telefon': phone
# }

# ogrenciler.update({
#     number: {
#         'ad': name,
#         'soyad': surName,
#         'telefon': phone
#     }
# })

print(ogrenciler)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)