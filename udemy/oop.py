class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def total_estoque(self):
        return self.preco * self.quantidade

    def exibir_dados(self):
        print(
            f"Produto = {self.nome} | Quantidade = {self.quantidade} | Total em estoque = {self.total_estoque()}"
        )


quantos = int(input("Quantos produtos serão instanciados: "))
produtos = []

for i in range(quantos):
    print(f"Produto {i + 1}º : ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    produto = Produto(nome, preco, quantidade)
    produtos.append(produto)

print("Produtos Cadastrados: ")
print()
for item in produtos:
    item.exibir_dados()
