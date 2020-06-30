# a = int(input('1. sayı: '))

# b = int(input('2. sayı: '))

# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür {result}')

vize1 = float(input('1. vize: '))
vize2 = float(input('2. vize: '))
final = float(input('final: '))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

print(f'not ortamanız: {ortalama} ve derster geçme durumunuz: {ortalama >= 50}')