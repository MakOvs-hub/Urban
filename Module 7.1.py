class Product:
    def __init__(self, name, weight, category):
        self.name = name  # название продукта(строка)
        self.weight = weight  # общий вес товара(дробное число)
        self.category = category  # категория товара(строка)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        x = file.read()
        file.close()
        return x


    def add(self, *products):
        for product in products:
            if product.name in self.get_products():
                file = open(self.__file_name, 'r')
                print(f'Продукт {product.name} уже есть в магазине')
                file.close()
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n') 
                file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
