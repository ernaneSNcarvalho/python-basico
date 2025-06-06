class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def set_name(self, new_name):
        self._name = new_name

    def set_price(self, new_price):
        self._price = new_price

    def exibir_dados(self):
        return f"Produto = {self.get_name()} | Preco = R$ {self.get_price()}"


name = input("Digite o nome do produto: ")
price = float(input("Digite o preço do produto: "))

p1 = Product(name, price)
print(p1.exibir_dados())
