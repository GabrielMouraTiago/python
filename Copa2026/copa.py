# Relatório Copa do Mundo 2026
# Autor: Gabriel Moura
# Dados: FIFA World Cup 2026 Player Data

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('teams.csv')
top10 = df[['team', 'goals', 'goals_against']].sort_values('goals', ascending=False).head(10)

x = range(len(top10))

plt.figure(figsize=(12, 6))
plt.bar(x, top10['goals'], width=0.4, label='Gols Feitos', color='green', align='center')
plt.bar([i + 0.4 for i in x], top10['goals_against'], width=0.4, label='Gols Sofridos', color='red', align='center')

plt.xticks([i + 0.2 for i in x], top10['team'], rotation=45, ha='right')
plt.title('Ataque x Defesa - Top 10 Seleções Copa 2026')
plt.legend()
plt.tight_layout()
plt.savefig('ataque_defesa_copa2026.png', dpi=150, bbox_inches='tight')
print('Gráfico salvo!')