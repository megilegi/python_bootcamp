class Product():

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f'Produkt "{self.name}", id: {self.id}, cena: {self.price} PLN')


class Basket():
    def __init__(self):
        self.koszyk = dict()

    def add_product(self, product, quantity):

        self.product = product
        self.quantity = quantity
        if self.product in self.koszyk:
            return self.koszyk
        else:

            self.koszyk.update({product: quantity})
            return self.koszyk

    def count_total_price(self):
        suma_zakupow = 0

        for product in self.koszyk.keys():
            suma_zakupow += product.price * self.koszyk[product]

        return suma_zakupow

    def generate_report(self):
        for self.product in self.basket:
            print(f'Produkty w koszyku :\n -{self.product.name} ({self.product.id}), cena: {self.product.price} x {self.quantity} \n W sumie: {self.count_total_price()}')


def test_basket_product():
    basket = Basket()
    product = Product(1, "Woda", 10.00)
    assert product.id == 1
    assert product.name == 'Woda'
    assert product.price == 10.00

def test_add_product(capsys):
    basket = Basket()
    product = Product(1, "Woda", 10.00)
    basket.add_product(product, 5)
    # product = Product(1, "Mydlo", 1.00)git check out
    # product = Product(1, "Mydlo", 1.00)
    # basket.add_product(product, 5)
    # assert basket.count_total_price() == 55.0
    out, _ = capsys.readouterr()
    assert out == 'Produkty w koszyku :\n -Woda (1), cena: 10.00 x 5 \n W sumie: 50.00'