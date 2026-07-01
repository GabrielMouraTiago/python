# Relatório Copa do Mundo 2026
# Autor: Gabriel Moura
# Dados: FIFA World Cup 2026 Player Data

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

# ── 1. CARREGAR DADOS ─────────────────────────────────────
df = pd.read_csv('teams.csv')

# ── 2. PREPARAR DADOS ────────────────────────────────────
df = df.copy()
df['total_cartoes'] = df['cards_yellow'] + df['cards_red']
df['eficiencia'] = (df['goals'] / df['shots']).fillna(0).round(2)

# ── 3. ANÁLISES ──────────────────────────────────────────
gols = df['goals'].values
posse = df['possession'].values

top10_gols    = df[['team', 'goals', 'goals_against']].sort_values('goals', ascending=False).head(10)
top10_cartoes = df[['team', 'cards_yellow', 'cards_red', 'total_cartoes']].sort_values('total_cartoes', ascending=False).head(10)
top10_efic    = df[['team', 'shots', 'goals', 'eficiencia']].sort_values('eficiencia', ascending=False).head(10)
top10_chutes  = df[['team', 'shots', 'shots_on_target', 'goals']].sort_values('shots', ascending=False).head(10)

media      = np.mean(gols)
mediana    = np.median(gols)
moda       = np.argmax(np.bincount(gols))
correlacao = np.corrcoef(posse, gols)[0, 1]

# ── 4. GRÁFICOS ──────────────────────────────────────────
# Gráfico 1 — Cartões
plt.figure(figsize=(12, 6))
plt.barh(top10_cartoes['team'], top10_cartoes['cards_yellow'], label='Amarelos', color='gold')
plt.barh(top10_cartoes['team'], top10_cartoes['cards_red'], left=top10_cartoes['cards_yellow'], label='Vermelhos', color='red')
plt.title('Top 10 Seleções com Mais Cartões')
plt.xlabel('Cartões')
plt.legend()
plt.tight_layout()
plt.savefig('cartoes.png', dpi=150, bbox_inches='tight')
plt.close()
print('Gráfico cartões salvo!')

# Gráfico 2 — Ataque x Defesa
x = range(len(top10_gols))

plt.figure(figsize=(12, 6))
plt.bar(x, top10_gols['goals'], width=0.4, label='Gols Feitos', color='green', align='center')
plt.bar([i + 0.4 for i in x], top10_gols['goals_against'], width=0.4, label='Gols Sofridos', color='red', align='center')
plt.xticks([i + 0.2 for i in x], top10_gols['team'], rotation=45, ha='right')
plt.title('Ataque x Defesa - Top 10 Seleções Copa 2026')
plt.legend()
plt.tight_layout()
plt.savefig('ataque_defesa.png', dpi=150, bbox_inches='tight')
plt.close()
print('Gráfico ataque x defesa salvo!')

# Gráfico 3 — Eficiência
plt.figure(figsize=(12, 6))
plt.barh(top10_efic['team'], top10_efic['eficiencia'], color='steelblue')
plt.title('Top 10 Seleções Mais Eficientes (Gols por Chute)')
plt.xlabel('Eficiência')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('eficiencia.png', dpi=150, bbox_inches='tight')
plt.close()
print('Gráfico eficiência salvo!')

# Gráfico 4 — Dispersão posse x gols
plt.figure(figsize=(12, 6))
plt.scatter(df['possession'], df['goals'], color='purple', alpha=0.6)

for i, row in df.iterrows():
    plt.annotate(row['team'], (row['possession'], row['goals']), fontsize=7)

plt.title(f'Posse de Bola x Gols (correlação: {correlacao:.2f})')
plt.xlabel('Posse de Bola (%)')
plt.ylabel('Gols')
plt.tight_layout()
plt.savefig('dispersao.png', dpi=150, bbox_inches='tight')
plt.close()
print('Gráfico dispersão salvo!')

# Análise 5 — Posse x Pontos por jogo
plt.figure(figsize=(12, 6))
plt.scatter(df['possession'], df['points_per_game'], color='darkorange', alpha=0.6)

for i, row in df.iterrows():
    plt.annotate(row['team'], (row['possession'], row['points_per_game']), fontsize=7)

corr_posse_pontos = np.corrcoef(df['possession'], df['points_per_game'])[0, 1]

plt.title(f'Posse de Bola x Desempenho (correlação: {corr_posse_pontos:.2f})')
plt.xlabel('Posse de Bola (%)')
plt.ylabel('Pontos por Jogo')
plt.tight_layout()
plt.savefig('posse_vs_pontos.png', dpi=150, bbox_inches='tight')
plt.close()
print('Gráfico posse x pontos salvo!')

# Análise 6 — Cartões x Desempenho
plt.figure(figsize=(12, 6))
plt.scatter(df['total_cartoes'], df['points_per_game'], color='crimson', alpha=0.6)

for i, row in df.iterrows():
    plt.annotate(row['team'], (row['total_cartoes'], row['points_per_game']), 
                fontsize=7, xytext=(4, 4), textcoords='offset points')

corr_cartoes_pontos = np.corrcoef(df['total_cartoes'], df['points_per_game'])[0, 1]

plt.title(f'Cartões x Desempenho (correlação: {corr_cartoes_pontos:.2f})')
plt.xlabel('Total de Cartões')
plt.ylabel('Pontos por Jogo')
plt.tight_layout()
plt.savefig('cartoes_vs_pontos.png', dpi=150, bbox_inches='tight')
plt.close()
print('Gráfico cartões x pontos salvo!')

# ── 5. PDF ───────────────────────────────────────────────
pdf = FPDF()

# Página 1 — Capa
pdf.add_page()
pdf.set_font('Helvetica', 'B', 24)
pdf.cell(0, 20, 'Relatorio Copa do Mundo 2026', ln=True, align='C')
pdf.set_font('Helvetica', '', 12)
pdf.cell(0, 10, 'Analise estatistica das 48 selecoes', ln=True, align='C')
pdf.cell(0, 10, 'Por Gabriel Tiago', ln=True, align='C')
pdf.ln(15)
pdf.multi_cell(0, 8, 'Este relatorio apresenta uma analise estatistica completa das 48 selecoes que disputaram a Copa do Mundo 2026. Os dados incluem gols, cartoes, eficiencia ofensiva e a relacao entre posse de bola e desempenho em campo.')

# Página 2 — Gráfico Ataque x Defesa
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 15, 'Ataque x Defesa', ln=True)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 8, 'O grafico abaixo compara gols feitos e gols sofridos pelas 10 selecoes que mais marcaram na competicao.')
pdf.ln(5)
pdf.image('ataque_defesa.png', x=10, w=190)

# Página 3 — Gráfico Cartões
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 15, 'Cartoes', ln=True)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 8, 'As selecoes mais indisciplinadas do torneio, somando cartoes amarelos e vermelhos.')
pdf.image('cartoes.png', x=10, w=190)
pdf.ln(5)

# Página 4 — Gráfico Eficiência
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 15, 'Eficiencia', ln=True)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 8, 'Quem converteu mais gols a cada chute,  nem sempre quem chuta mais e quem marca mais.')
pdf.image('eficiencia.png', x=10, w=190)

# Página 5 — Posse de bola X Pontos
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 15, 'Posse de bola vs Pontos', ln=True)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 8, f'Relacao entre posse de bola e gols feitos. Correlacao de {correlacao:.2f}, fraca, ou seja, posse nao garante gol.')
pdf.image('posse_vs_pontos.png', x=10, w=190)

# Página 6 — Posse de bola X Pontos
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 15, 'Posse de bola vs Gols', ln=True)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 8, f'Relacao entre posse de bola e gols feitos.')
pdf.image('dispersao.png', x=10, w=190)

# Página 7 — Cartões  X Pontos
pdf.add_page()
pdf.set_font('Helvetica', 'B', 16)
pdf.cell(0, 15, 'Cartões vs Pontos', ln=True)
pdf.set_font('Helvetica', '', 11)
pdf.multi_cell(0, 8, f'Relacao entre indisciplina e pontuacao na competicao. Correlacao de {corr_cartoes_pontos:.2f}.')
pdf.image('cartoes_vs_pontos.png', x=10, w=190)

pdf.output('relatorio_copa2026.pdf')
print('PDF gerado!')
