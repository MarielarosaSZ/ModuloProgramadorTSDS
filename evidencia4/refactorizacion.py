class Moto:
    def __init__(self):
        self.velocidad = 0
        self.marcha = 1  # Se asume que la marcha inicial es 1

    def acelerar(self):
        """Aumenta la velocidad de la moto en 10."""
        self.velocidad += 10

    def frenar(self):
        """Disminuye la velocidad de la moto en 10, sin permitir que sea negativa."""
        self.velocidad = max(0, self.velocidad - 10)

    def cambiar_marcha(self, marcha):
        """Cambia la marcha de la moto, debe estar entre 1 y 5."""
        if marcha < 1 or marcha > 5:
            raise ValueError("La marcha debe estar entre 1 y 5.")
        self.marcha = marcha

#python -m unittest test_moto.py
