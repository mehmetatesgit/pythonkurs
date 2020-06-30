# file = open("newfile.txt", "w")
# file = open("C:/Users/new/Desktop/newfile.txt", "w")

# file.close()

# file = open("newfile.txt", "w", encoding = "utf-8")
# file.write("Mehmet Ateş Özer")
# file.close()
#
# file = open("newfile.txt", "a", encoding = "utf-8")
# # file.write('\nSema Özer')
# file.write('Sema Özer\n')
# file.close()


# file = open("newfile2.txt", "x", encoding = "utf-8")

# file = open("newfile.txt", "r")

# print(file)

# try:
#     file = open("newfile2.txt", "r")
# except FileNotFoundError:
#     print('Dosya okuma hatası')

# file = open("newfile.txt", "r", encoding="utf-8")

#*******************for döngüsü
'''
for i in file:
    print(i, end="")

file.close()
'''
#*****************read() fonksiyonu
'''
content1 = file.read()
print('içerik 1: ')
print(content1)

file = open("newfile.txt", "r", encoding="utf-8")


content2 = file.read()
print('içerik 2: ')
print(content2)

file.close()


content = file.read(5)
content = file.read(3)
content = file.read(5)

print(content)

file.close()
'''

#*****************readline() fonksiyonu
'''
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
'''

#*****************readlines() fonksiyonu
'''
liste = file.readlines()
print(liste[2], end="")

'''

'''
with open("newfile.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(0)
    print(file.tell())
    content2 = file.read()
    print(content2)
'''
# close() gerek yok.


# Dosyada update yapma
'''
with open("newfile.txt", "r+", encoding="utf-8") as file:
    file.seek(15)
    file.write('deneme')

with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())
'''
#Sayfa sonunda güncelleme

'''
with open("newfile.txt", "a", encoding="utf-8") as file:
    file.write("\nMurat Özer")

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())
'''
#Sayfa başında güncelleme

'''
with open("newfile.txt", "r+", encoding="utf-8") as file:
    content = file.read()
    content = "Fatih Özer\n" + content
    file.seek(0)
    file.write(content)

with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())

'''

#Sayfa ortasında güncelleme

with open("newfile.txt", "r+", encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(1, "Osman Özer\n")
    file.seek(0)
    file.writelines(liste)

with open("newfile.txt", "r+", encoding="utf-8") as file:
    print(file.read())
