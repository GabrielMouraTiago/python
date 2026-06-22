# 🎮 Pokémon Battle — Orientação a Objetos em Python

Jogo de batalha Pokémon desenvolvido do zero em Python, com foco em Programação Orientada a Objetos. O projeto explora herança, polimorfismo e encapsulamento através de um sistema de batalha completo em terminal.

---

## ⚔️ O que o projeto faz

- Batalha em turnos entre jogador e inimigo
- Sistema de tipos com multiplicadores de dano (Fogo, Água, Planta, Elétrico, etc.)
- Cada Pokémon tem HP, força e energia gerenciados por turno
- Golpes especiais com custo de energia
- Nível aleatório que escala força e HP
- Inimigo escolhe golpes aleatoriamente

---

## 🧱 Arquitetura do projeto

O projeto foi estruturado em três camadas:

```
pokemon/
├── pokedex.py    # Classes base — Pokemon, Eletrico, Agua, Fogo, Planta...
├── pokemon.py    # Pokémons específicos — Pikaxu, Squirtle, Charmander, Bulbasaur
└── jogo.py       # Loop principal da batalha
```

---

## 🛠️ Conceitos de POO aplicados

| Conceito | Aplicação |
|---|---|
| `Herança` | Cada tipo herda de `Pokemon`; cada Pokémon herda do seu tipo |
| `Herança múltipla` | Pikaxu é Elétrico mas tem golpe de Lutador |
| `Polimorfismo` | Cada golpe tem comportamento diferente por tipo de alvo |
| `Encapsulamento` | HP e energia gerenciados dentro de cada instância |
| `getattr` | Golpes chamados dinamicamente pelo nome do método |

---
> Não precisa instalar nenhuma dependência — só Python puro.

---

## 🔥 Exemplo de batalha

```
Escolha seu Pokemon:
1 - Pikaxu
2 - Squirtle
3 - Bulbasaur
4 - Charmander

Você escolheu um Pikaxu! Digite um nome para ele: Raiden
Raiden - Nível 7 - Força: 350 - HP: 700

1 - Choque do Trovão
2 - Raio Bola
3 - Super Soco

Escolha um golpe: 1
Raiden usou Choque do Trovão causando 700 de dano!
```

---

## 👨‍💻 Autor

**Gabriel Tiago** — Python Developer
