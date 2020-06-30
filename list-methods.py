numbers = [1, 10, 5, 16, 20, 3, 9, 10]
letters = ['a', 'r', 'h', 'b', 'c', 'e']

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

val = numbers[3:6]

numbers[4] = 40

numbers.append(49)
numbers.append(59)
numbers.append(69)
numbers.insert(3, 78)
numbers.insert(-1, 52)
# numbers.pop()
# numbers.pop(0)
# numbers.pop(-1)
# numbers.remove(40)
numbers.sort()
letters.sort()
numbers.reverse()
letters.reverse()
elemanSayisi = len(numbers)
elemanSayisi1 = len(letters)
numbers.clear()



print(elemanSayisi1)
print(letters)
print(numbers)
print(elemanSayisi)
print(numbers)