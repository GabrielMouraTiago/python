class Pokemon:
    def __init__(self, nome, tipo, forca, hp, energia = 100, nivel = 1):
        self.nome = nome
        self.tipo = tipo
        self.forca_base = forca
        self.hp_base = hp
        self.energia = energia
        self.nivel = nivel
        self.forca = forca * nivel
        self.hp = hp * nivel


class Eletrico(Pokemon):
    def __init__(self, nome, forca, hp, energia = 100, nivel = 1):
        super().__init__(nome, "Eletrico", forca, hp, energia, nivel)

    def choqueTrovao(self, pokemon):
        if self.energia < 20:
            print(f"{self.nome} não tem energia suficiente para usar Choque do Trovão!")
            return
        
        self.energia -= 20

        match pokemon.tipo:
            case "Agua":
                dano = self.forca * 2
            case "Planta":
                dano = self.forca * 0.5
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque elétrico em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")

    def raioBola(self, pokemon):
        if self.energia < 15:
            print(f"{self.nome} não tem energia suficiente para usar Raio Bola!")
            return
        self.energia -= 15

        match pokemon.tipo:
            case "Agua":
                dano = self.forca * 1.3
            case "Planta":
                dano = self.forca * 0.8
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque elétrico em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")

class Agua(Pokemon):
    def __init__(self, nome, forca, hp, energia = 100, nivel = 1):
        super().__init__(nome, "Agua", forca, hp, energia, nivel)

    def toraDagua(self, pokemon):
        if self.energia < 20:
            print(f"{self.nome} não tem energia suficiente para usar Tora d'água!")
            return
        self.energia -= 20

        match pokemon.tipo:
            case "Fogo":
                dano = self.forca * 2
            case "Eletrico":
                dano = self.forca * 0.5
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque de água em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")

    def jatoDagua(self, pokemon):
        if self.energia < 15:
            print(f"{self.nome} não tem energia suficiente para usar Jato d'água!")
            return
        self.energia -= 15

        match pokemon.tipo:
            case "Fogo":
                dano = self.forca * 1.3
            case "Eletrico":
                dano = self.forca * 0.8
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque de água em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")

class Fogo(Pokemon):
    def __init__(self, nome, forca, hp, energia = 100, nivel = 1):
        super().__init__(nome, "Fogo", forca, hp, energia, nivel)

    def superFogo(self, pokemon):
        if self.energia < 20:
            print(f"{self.nome} não tem energia suficiente para usar Super Fogo!")
            return
        self.energia -= 20

        match pokemon.tipo:
            case "Planta":
                dano = self.forca * 2
            case "Agua":
                dano = self.forca * 0.5
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque de fogo em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")

    def bolaDeFogo(self, pokemon):
        if self.energia < 15:
            print(f"{self.nome} não tem energia suficiente para usar Bola de Fogo!")
            return
        self.energia -= 15

        match pokemon.tipo:
            case "Planta":
                dano = self.forca * 1.6
            case "Agua":
                dano = self.forca * 0.8
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque de fogo em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")
        
class Planta(Pokemon):
    def __init__(self, nome, forca, hp, energia = 100, nivel = 1):
        super().__init__(nome, "Planta", forca, hp, energia, nivel)

    def raioSolar(self, pokemon):
        if self.energia < 30:
            print(f"{self.nome} não tem energia suficiente para usar Raio Solar!")
            return
        self.energia -= 30

        match pokemon.tipo:
            case "Agua":
                dano = self.forca * 2.5
            case "Fogo":
                dano = self.forca * 0.9
            case _:
                dano = self.forca * 1.3
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque de planta em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")

    def folhaNavalha(self, pokemon):
        if self.energia < 20:
            print(f"{self.nome} não tem energia suficiente para usar Folha Navalha!")
            return
        self.energia -= 20

        match pokemon.tipo:
            case "Agua":
                dano = self.forca * 1.8
            case "Fogo":
                dano = self.forca * 0.7
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque de planta em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")


class Lutador(Pokemon):
    def __init__(self, nome, forca, hp, energia = 100, nivel = 1):
        super().__init__(nome, "Lutador", forca, hp, energia, nivel)

    def superSoco(self, pokemon):
        if self.energia < 20:
            print(f"{self.nome} não tem energia suficiente para usar Super Soco!")
            return  
        self.energia -= 20

        match pokemon.tipo:
            case "Normal":
                dano = self.forca * 2
            case "Psíquico":
                dano = self.forca * 0.5
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque de luta em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")

    def cabecada(self, pokemon):
        if self.energia < 15:
            print(f"{self.nome} não tem energia suficiente para usar Cabeçada!")
            return
        self.energia -= 15
        
        match pokemon.tipo:
            case "Normal":
                dano = self.forca * 1.5
            case "Psíquico":
                dano = self.forca * 0.8
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque de luta em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")

class Dragao(Pokemon):
    def __init__(self, nome, forca, hp, energia = 100, nivel = 1):
        super().__init__(nome, "Dragao", forca, hp, energia, nivel)

    def soproDragao(self, pokemon):
        if self.energia < 20:
            print(f"{self.nome} não tem energia suficiente para usar Sopro de Dragão!")
            return
        self.energia -= 20

        match pokemon.tipo:
            case "Dragao":
                dano = self.forca * 2
            case "Fada":
                dano = self.forca * 0.5
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque de dragão em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")

    def garraDragao(self, pokemon):
        if self.energia < 15:
            print(f"{self.nome} não tem energia suficiente para usar Garra de Dragão!")
            return
        self.energia -= 15

        match pokemon.tipo:
            case "Dragao":
                dano = self.forca * 1.5
            case "Fada":
                dano = self.forca * 0.8
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque de dragão em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")

class Terra(Pokemon):
    def __init__(self, nome, forca, hp, energia = 100, nivel = 1):
        super().__init__(nome, "Terra", forca, hp, energia, nivel)

    def pedrada(self, pokemon):
        if self.energia < 20:
            print(f"{self.nome} não tem energia suficiente para usar Pedrada!")
            return
        self.energia -= 20

        match pokemon.tipo:
            case "Eletrico":
                dano = self.forca * 2
            case "Voador":
                dano = self.forca * 0.5
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque terrestre em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")

    def terremoto(self, pokemon):
        if self.energia < 15:
            print(f"{self.nome} não tem energia suficiente para usar Terremoto!")
            return
        self.energia -= 15

        match pokemon.tipo:
            case "Eletrico":
                dano = self.forca * 1.5
            case "Voador":
                dano = self.forca * 0.8
            case _:
                dano = self.forca
        pokemon.hp -= dano
        print(f"{self.nome} usou um ataque terrestre em {pokemon.nome} causando {dano} de dano! {pokemon.nome} agora tem {pokemon.hp} HP.")
        