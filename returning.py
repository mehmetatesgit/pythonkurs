'''
def usalma(number):

    def inner(power):

        return number ** power
    return inner

two = usalma(2)
print(two(3))

three = usalma(3)
print(three(4))
'''
'''
def yetki_sorgula(page):

    def inner(role):
        if role == 'Admin':
            return '{0} rolü {1} sayfasına ulaşabilir'.format(role, page)
        else:
            return '{0} rolü {1} sayfasına ulaşamaz'.format(role, page)
    return inner

user1 = yetki_sorgula('Product edit')
print(user1('Admin'))
print(user1('User'))
'''

def islem_adi(islem):

    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+= i
        return toplam
    
    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem == 'toplama':
        return toplam
    else:
        return carpim

hesap = islem_adi('carpma')
print(hesap(1,3,5,7,9))