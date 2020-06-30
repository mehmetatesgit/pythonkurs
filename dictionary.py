# sehirler = ['kocaeli', 'istanbul']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('kocaeli')])
# print(plakalar[sehirler.index('istanbul')])

# plakalar = {'kocaeli' : 41, 'istanbul' : 34}

# print(plakalar['kocaeli'])

# plakalar['ankara'] = 6
# plakalar['kocaeli'] = 'new value'

# print(plakalar)

users = {
    'ates özer' : {
        'age' : 36,
        'roles' : ['user'],
        'mail' : 'gmail.com',
        'address' : 'kocaeli',
        'phone' : '123456'
    },
    'kıymet' : {
        'age' : 14,
        'roles' : ['admin', 'user'],
        'mail' : 'hotmail.com',
        'address' : 'izmit',
        'phone' : '654321'
    }
}

print(users['kıymet']['roles'])

