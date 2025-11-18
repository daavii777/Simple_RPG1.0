class Dragon:
    def __init__(self, nome, tipo, ataque, defesa):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.defesa = defesa
        self.vida = 10000  # opcional: pra deixar mais RPG

    def atacar(self):
        print(f"{self.nome} ({self.tipo}) atacou com {self.ataque} de poder!")
        