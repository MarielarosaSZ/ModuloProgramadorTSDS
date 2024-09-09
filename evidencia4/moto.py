class Moto:
    def __init__(self):
        self.modelo=""
        self.color=""
        self.cilindradas=""
        self.velocidad = 0
        self.marcha = 1  # Se asume que la marcha inicial es 1

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad = max(0, self.velocidad - 10)  # Velocidad no puede ser negativa

    def cambiar_marcha(self, marcha):
        if marcha < 1 or marcha > 5:  # Supongamos que hay 5 marchas
            raise ValueError("La marcha debe estar entre 1 y 5.")
        self.marcha = marcha
