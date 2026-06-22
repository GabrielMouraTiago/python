# 🔢 NumberMatch — Jogo de Raciocínio com Pygame

Jogo de raciocínio lógico desenvolvido com Pygame, inspirado no clássico NumberMatch. O projeto explora funções, matrizes e lógica de jogo com interface gráfica completa.

---

## 🎯 Como jogar

- Encontre pares de números iguais **ou** que somem 10
- Os números precisam ser adjacentes — na mesma linha, coluna ou diagonal, sem outros números no caminho
- Elimine todos os pares para vencer
- Use o botão **+** para adicionar os números restantes ao final (até 3 vezes)

---

## ✨ Funcionalidades

- Grade 9x10 gerada aleatoriamente com pares balanceados
- Seleção visual com destaque em amarelo
- Scroll suave pelo mouse ou teclado
- Cores diferentes por rodada de adição
- Degradê na borda inferior da grade
- Sistema de pontuação em tempo real
- Remoção automática de linhas vazias

---

## 🧠 Conceitos técnicos aplicados

| Conceito | Aplicação |
|---|---|
| `Matrizes` | Grade representada como lista de listas |
| `Funções` | Cada comportamento isolado em função própria |
| `Algoritmo de adjacência` | Verifica horizontal, vertical, diagonal e wrap |
| `Pygame` | Renderização, eventos, scroll e input do usuário |
| `Tuplas` | Cada célula armazena `(número, rodada)` |


## 👨‍💻 Autor

**Gabriel Moura** — Python Developer
