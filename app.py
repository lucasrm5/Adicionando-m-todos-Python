class Carro:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    def ligar(self):
        print("O carro ligou!")

# Mudando propriedades

    def mudar_preco(self, novo_preco):
        self.preco = novo_preco

    def desligar(self):
        print("O carro desligou!")

nivus = Carro("VW", 70000)
print(nivus.marca)
nivus.ligar()

nivus.mudar_preco(80000)
print(nivus.preco)
nivus.desligar()