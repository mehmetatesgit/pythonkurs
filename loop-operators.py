# list = [1,2,3]

# for item in list:
#     print(item)

# for item in range(10):

#     print(item)

#range

# for item in range(2,10):
#     print(item)

# for item in range(50,100,20):
#     print(item)

# print(list(range(50,100,20)))

#enumurate

# index = 0
# greeting = 'Hello'

# for letter in greeting:
#     print(f'İndex: {index} letter: {letter}')
#     index += 1


# for item in enumerate(greeting):
#     print(item)
#     # print(f'İndex: {index} letter: {letter}')


#zip

list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3)))


for item in zip(list1, list2, list3):
    print(item)



