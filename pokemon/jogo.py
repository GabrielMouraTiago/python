from pokemon import *
import random

golpes_dic = { "choqueTrovao" : "Choque do Trovão", 
          "raioBola" : "Raio Bola", 
         "toraDagua" : "Tora d'água", 
         "jatoDaAgua" : "Jato d'água", 
          "garraDragao" : "Garra do Dragão", 
          "superSoco" : "Super Soco", 
          "pedrada" : "Pedrada", 
          "cabecada" : "Cabeçada" }

def listar_golpes(pokemon):
    atributos_base = ["nome", "tipo", "forca", "hp", "energia"]
    golpes = [m for m in dir(pokemon)
              if not m.startswith("__")
              and m not in atributos_base
              and callable(getattr(pokemon, m))]
    
    golpes_bonitos = []
    for g in golpes:
        nome_bonito = golpes_dic.get(g, g) 
        golpes_bonitos.append(nome_bonito)
    
    return golpes_bonitos, golpes

def listar_metodos(pokemon):
    atributos_base = ["nome", "tipo", "forca", "hp", "energia"]
    metodos = [m for m in dir(pokemon)
              if not m.startswith("__")
              and m not in atributos_base
              and callable(getattr(pokemon, m))]
    return metodos

opcao = {
    1: Pikaxu,
    2: Squirtle,
    3: Bulbasaur,
    4: Charmander
}

total_pokemons = len(opcao)

#Escolha do Pokemon: Player
print("Escolha seu Pokemon:")
for numero, pokemon in opcao.items():
    print(f"{numero} - {pokemon.__name__}")

escolha = int(input("Digite o número:"))
pokemon_escolhido = opcao.get(escolha)
nome = input(f"Você escolheu um {pokemon_escolhido.__name__}! Digite um nome para ele:")
nivel_aleatorio = random.randint(1, 10)
primeiro_pokemon = pokemon_escolhido(nome, nivel=nivel_aleatorio)
golpes, metodo = listar_golpes(primeiro_pokemon)
print(f"{primeiro_pokemon.nome} - Nível {primeiro_pokemon.nivel} - Força: {primeiro_pokemon.forca} - HP: {primeiro_pokemon.hp}")
print("Os seus golpes são: " + ", ".join(golpes))
input("Pressione Enter para continuar...")

#Escolha do Pokemon: Inimigo
inimigo_escolhido = opcao.get(random.randint(1, total_pokemons))
nome_inimigo =  "Dark" + inimigo_escolhido.__name__
input("O inimigo escolheu: " + inimigo_escolhido.__name__ + "! Pressione Enter para continuar...")
nivel_inimigo = random.randint(1, 10)
dark_pokemon = inimigo_escolhido(nome_inimigo, nivel=nivel_inimigo)
print(f"{dark_pokemon.nome} - Nível {dark_pokemon.nivel} - Força: {dark_pokemon.forca} - HP: {dark_pokemon.hp}")
input("Agora o pau vai tora! Pressione Enter para continuar...")
golpes_dark, metodo_dark = listar_golpes(dark_pokemon)

#Começar a batalha
while primeiro_pokemon.hp > 0 and dark_pokemon.hp > 0:

    for i, golpe in enumerate(golpes, start=1):
        print(f"{i} - {golpe}")
    golpe_escolhido = int(input("Escolha um golpe para usar: ")) - 1
    print(f"{primeiro_pokemon.nome} usou {golpes[golpe_escolhido]}!")
    getattr(primeiro_pokemon, metodo[golpe_escolhido])(dark_pokemon)
    
    if dark_pokemon.hp <= 0:
        break
    metodo_inimigo = random.choice(metodo_dark)
    getattr(dark_pokemon, metodo_inimigo)(primeiro_pokemon)

if primeiro_pokemon.hp > 0:
    print(f"{primeiro_pokemon.nome} venceu!")
else:
    print(f"{dark_pokemon.nome} venceu!")
