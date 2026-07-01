# 🐍 Projetos Python — Gabriel Moura

Repositório com projetos desenvolvidos em Python, cada um focado em um conjunto de conceitos fundamentais: análise de dados, orientação a objetos e desenvolvimento de jogos.

---

## 📁 Projetos

### ⚽ Copa do Mundo 2026 — Análise de Dados
> `pandas` • `numpy` • `matplotlib` • `fpdf2`

Análise estatística completa das 48 seleções da Copa do Mundo 2026. Gera 6 gráficos e um relatório em PDF automaticamente, sem nenhuma intervenção manual.

**O que faz:**
- Processa dataset com 48 seleções e 136 variáveis
- Calcula média, mediana, moda e correlações com numpy
- Gera 6 gráficos: ataque x defesa, cartões, eficiência, dispersão e correlações
- Exporta relatório completo em PDF com capa, gráficos e textos explicativos

**Como rodar:**
```bash
cd Copa2026
pip install pandas numpy matplotlib fpdf2
python copa.py
```

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
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat)
![Pygame](https://img.shields.io/badge/Pygame-darkgreen?style=flat)

---

## 👨‍💻 Autor

**Gabriel Tiago** — Python Developer

Motoboy em transição de carreira para programação. Estudando Python com foco em análise de dados, automação e desenvolvimento de jogos.
