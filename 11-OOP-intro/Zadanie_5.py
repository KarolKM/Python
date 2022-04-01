class Products():
    def __init__(self, name, size, cost):
        self.name = name
        self.size = size
        self.cost = cost

    def __repr__(self):
        return f'{self.name} || {self.size} - {self.cost} PLN'


class Shop():

    def __init__(self, articles):
        self.articles = articles

    def show(self):
        print(self.articles)

    def try_articles(self, index):
        print(f' Przynierzam: {self.articles[index]}')


p1 = Products('Spodnie', "L", 90)
p2 = Products('Bluza', "M", 100)
p3 = Products('Buty', 'S', 98)


shop_articles = Shop([p1, p2, p3])
shop_articles.show()
shop_articles.try_articles(2)


