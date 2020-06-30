#global scope
x = 'global x'

def function():
    #local scope
    # x = 'local x'
    print(x)

function()
print(x)

############################

name = 'ates'

def changeName(new_name):
    name = new_name
    print(name)

changeName('İstanbul')
print(name)

############################

name = 'global str'

def greeting():
    # name = 'Kıymet'
    
    def hello():
        # name = 'Ada'
        print('hello'+ name)
    
    hello()


greeting()

############################

x = 50

def test():
    global x
    print(f'x {x} ')

    x = 100
    print(f'change x to {x} ')

test()
print(x)

