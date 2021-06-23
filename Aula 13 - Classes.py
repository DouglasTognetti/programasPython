class Carro:

    def __init__(self, fabricante, modelo, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.leitura_hodometro = 0
        self.tanque = 0

    def buscar_nome_descricao(self):
        nome_extenso = str(self.ano) + ' ' + self.fabricante + ' ' + self.modelo
        return nome_extenso.title()

    def ler_hodometro(self):
         print("Esse carro tem " + str(self.leitura_hodometro) + " km.")    

    def atualizar_hodometro(self, km):
        if km >= self.leitura_hodometro:
            self.leitura_hodometro = km 
        else:
            print('Você está tentando reduzir o valor do km rodado.')

    def incrementar_hodometro(self, km):
        if km > 0:
            self.leitura_hodometro += km
        else:
            print('Você está tentando reduzir o valor do km rodado.')

    def abastecer_tanque(self, tanque):
        self.tanque += tanque
        print("Tanque atualizado para " + str(self.tanque) + " litros.")        


class CarroEletrico(Carro):

    def __init__(self, fabricante, modelo, ano):
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()

    def abastecer_tanque(self):
        print("Esse modelo de carro não possui tanque!")


class Bateria:

    def __init__(self, tamanho_bateria=70):
        self.tamanho_bateria = tamanho_bateria

    def descricao_bateria(self):
        print("Esse carro tem " + str(self.bateria) + "-kWh de bateria.")   

    def buscar_faixa(self):
        if self.tamanho_bateria == 70:
            range = 240
        elif self.tamanho_bateria == 85:
            range = 270
        message = "Esse carro pode percorrer aproximadamente " + str(range)
        message += " km com a bateria cheia."
        print(message)

    def __init__(self, fabricante, modelo, ano):
        super().__init__(fabricante, modelo, ano)
        self.bateria = 70

    def descricao_bateria(self):
        print("Esse carro tem " + str(self.bateria) + "-kWh de bateria.")   

    def abastecer_tanque(self):
        print("Esse modelo de carro não possui tanque!")
