# def changeName(n):
#     n = 'ada'

# name = 'yiğit'

# changeName(name)
# print(name)

# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara', 'izmir']

# change(sehirler[:])

# print(sehirler)


# def add (*params):
#     sum = 0
#     for n in params:
#         sum = sum + n
#     return sum

# print(add(10, 20))
# print(add(10, 20, 30))

def displayUser(**params):
    print(type(params))
    for key,value in params.items():
        print('{} is {}'.format(key,value))

displayUser(name = 'Çınar', age = 2, city = 'İstanbul')
displayUser(name = 'Ates', age = 23, city = 'Ankara', phone = '123456')
displayUser(name = 'Yiğit', age = 35, city = 'Kocaeli', phone = '123456789', email = 'yigit@gmail.com' )

def myfunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10,20,30,40,50, key1 = 'value 1', key2 = 'value 2')