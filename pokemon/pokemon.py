from pokedex import *

class Charmander(Fogo):
    forca_base = 50
    hp_base = 100

    def __init__(self, nome, energia = 100, nivel = 1):
        super().__init__(nome, self.forca_base, self.hp_base, energia, nivel)

    garraDragao = Dragao.garraDragao

class Pikaxu(Eletrico):
    forca_base = 50
    hp_base = 100
    def __init__(self, nome, energia = 100, nivel = 1):
        super().__init__(nome, self.forca_base, self.hp_base, energia, nivel)

    superSoco = Lutador.superSoco

class Squirtle(Agua):
    forca_base = 50
    hp_base = 100
    def __init__(self, nome, energia = 100, nivel = 1):
        super().__init__(nome, self.forca_base, self.hp_base, energia, nivel)

    pedrada = Terra.pedrada

class Bulbasaur(Planta):
    forca_base = 50
    hp_base = 100
    def __init__(self, nome, energia = 100, nivel = 1):
        super().__init__(nome, self.forca_base, self.hp_base, energia, nivel)

    superSoco = Lutador.cabecada

astolfo = Charmander("Astolfo", nivel=6)
rodolfo = Pikaxu("Rodolfo", nivel=2)
gabriel = Squirtle("Gabriel", nivel=3)
NaoSei = Bulbasaur("NaoSei", nivel=8)