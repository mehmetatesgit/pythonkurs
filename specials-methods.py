myList = [1,2,3]

# print(len(myList))

class Movie():
    def __init__(self, title, director, duraction):
        self.title = title
        self.director = director
        self.duraction = duraction
        print('Movie objesi oluştu..')

    def __str__(self):
        return f"{self.title} by {self.director} "

    def __len__(self):
        return self.duraction

    def __del__(self):
        print('film objesi silindi...')


m = Movie('film adı', 'yönetmen adı', 120)

# print(str(myList))
print(str(m))
# print(len(myList))
# print(len(m))

