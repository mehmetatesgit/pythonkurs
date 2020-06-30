# Bankamatik uygulaması

AtesHesap = {
    'ad': 'Ates Ozer',
    'hesapNo': '123456',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Ozer',
    'hesapNo': '123',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']} ")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz..')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        
        if(toplam >= miktar):
            ekHesapKullanımı = input('Ek hesap kullanılsın mı (e/h): ')

            if (ekHesapKullanımı == 'e'):
                ekHesapKullanilcakMiktar = miktar - hesap['bakiye'] 
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilcakMiktar
                print('Paranızı alabilirsiniz...')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır. ")
        else:
            print('Bakiye yetersiz.')

def bakiyeSorgulama(hesap):
    print(f" {hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL dir ")


def paraYatır(hesap):
    paraYatırma = input('Hangi hesabınıza para yatırmak istersiniz ? (bakiye / ekhesap)')
    yatırılanMiktar = int(input('Yatırmak istediğiniz tutar: '))
    if (paraYatırma == 'bakiye'):
        hesap['bakiye'] += yatırılanMiktar
    else:
        hesap['ekHesap'] += yatırılanMiktar

bakiyeSorgulama(AtesHesap)
paraYatır(AtesHesap)
bakiyeSorgulama(AtesHesap)
paraCek(AtesHesap, 6000)
bakiyeSorgulama(AtesHesap)