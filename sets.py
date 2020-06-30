fruits = {'orange', 'apple', 'banana'}

print(fruits)

for x in fruits:
    print(x)


fruits.add('cherry')
fruits.update(['mango', 'grape'])

print(fruits)

fruits.remove('mango')
print(fruits)
fruits.discard('apple')
print(fruits)

fruits.pop()
print(fruits)
myList = [1,2,3,4,2,2,1,4]
print(set(myList))