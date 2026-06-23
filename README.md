# 🐍 Projetos Python — Gabriel Tiago

Repositório com projetos desenvolvidos em Python, cada um focado em um conjunto de conceitos fundamentais: análise de dados, orientação a objetos e desenvolvimento de jogos.

---

## 📁 Projetos

### ⚽ Copa do Mundo 2026 — Análise de Dados
> `pandas` • `matplotlib` • análise de dados • gráficos

Análise estatística das 48 seleções da Copa do Mundo 2026 com geração de gráficos profissionais. Projeto sem API — dados reais processados diretamente do dataset oficial da FIFA.

**O que faz:**
- Processa dataset com 48 seleções e 136 variáveis cada
- Gera ranking das seleções que mais fizeram gols
- Compara ataque x defesa das top 10 seleções visualmente
- Exporta gráficos em PNG prontos para apresentação

**Como rodar:**
```bash
cd Copa2026
pip install pandas matplotlib
python copa.py
```

**Resultado:**
| Seleção | Gols |
|---|---|
| Germany | 7 |
| Canada | 6 |
| Sweden | 5 |
| Switzerland | 5 |
| Brazil | 4 |

---

### 🎮 Pokémon Battle — Orientação a Objetos
> `POO` • `herança` • `polimorfismo` • `encapsulamento`

Jogo de batalha Pokémon em terminal desenvolvido do zero, com foco em Programação Orientada a Objetos. Arquitetura em três camadas com sistema de tipos, energia e dano escalável por nível.

**Conceitos aplicados:**
| Conceito | Aplicação |
|---|---|
| Herança | Cada tipo herda de `Pokemon`; cada Pokémon herda do seu tipo |
| Herança múltipla | Pikaxu é Elétrico mas possui golpe de Lutador |
| Polimorfismo | Cada golpe tem multiplicador diferente por tipo de alvo |
| Encapsulamento | HP e energia gerenciados dentro de cada instância |
| `getattr` | Golpes chamados dinamicamente pelo nome do método |

**Como rodar:**
```bash
cd pokemon
python jogo.py
```

---

### 🔢 NumberMatch — Funções e Matrizes
> `pygame` • `matrizes` • `funções` • `algoritmos`

Jogo de raciocínio lógico com interface gráfica completa, inspirado no clássico NumberMatch. Cada comportamento do jogo é isolado em funções independentes, e a grade é representada como uma matriz de tuplas.

**Conceitos aplicados:**
| Conceito | Aplicação |
|---|---|
| Matrizes | Grade 9x10 representada como lista de listas |
| Funções | Cada comportamento isolado — criar grade, verificar adjacência, adicionar números |
| Algoritmo de adjacência | Verifica horizontal, vertical, diagonal e wrap entre células |
| Pygame | Renderização, eventos, scroll suave e input do usuário |
| Tuplas | Cada célula armazena `(número, rodada)` |

**Como rodar:**
```bash
cd rachacuca
pip install pygame
python numbermatch.py
```

---

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat)
![Pygame](https://img.shields.io/badge/Pygame-darkgreen?style=flat)

---

## 👨‍💻 Autor

**Gabriel Moura** — Python Developer

Motoboy em transição de carreira para programação. Estudando Python com foco em análise de dados, automação e desenvolvimento de jogos.
