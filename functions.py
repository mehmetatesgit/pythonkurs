# def sayHello(name = 'user'):
#     print('Hello '+ name)

# sayHello('Ates')
# sayHello('Hakan')
# sayHello()

def sayHello(name = 'user'):
    return 'Hello '+ name

msg = sayHello('Ates')

print(msg)


def total(num1, num2):
    return num1 + num2

result = total(10,20)

print(result)


def yasHesapla(dogumYili):
    return 2020 - dogumYili

ageCinar = yasHesapla(2010)

print(ageCinar)

def EmekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı ') 
    else:
        print('Zaten emekli oldunuz...')

EmekliligeKacYilKaldi(1983, 'Ali' )
EmekliligeKacYilKaldi(1950, 'Ahmet' )