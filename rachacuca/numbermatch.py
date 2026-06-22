import pygame
import random

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("NumberMatch")

rodando = True
fonte = pygame.font.SysFont("monospace", 48, bold=True)

COLUNAS = 9
LINHAS = 10
linhas_visiveis = 8
TAMANHO_CELULA = 55
MARGEM_X = (800 - COLUNAS * TAMANHO_CELULA) // 2
MARGEM_Y = (600 - LINHAS * TAMANHO_CELULA) // 2
vezes_adicionado = 0
scroll_y = 0
ALTURA_JANELA_GRADE = 8 * TAMANHO_CELULA

CORES_RODADA = [
    (235, 228, 215),  # branco bege
    (150, 200, 255),  # azul claro
    (180, 255, 180),  # verde claroo
]

BOTAO_X = 350
BOTAO_Y = 540
BOTAO_W = 100
BOTAO_H = 40
fonte_botao = pygame.font.SysFont("monospace", 24, bold=True)

pontos = 0
fonte_pontos = pygame.font.SysFont("monospace", 28, bold=True)

def criar_grade():
    total_celulas = COLUNAS * 4
    total_pares = total_celulas // 2
    pares_por_numero = total_pares // 9
    resto = total_pares % 9
    
    numeros = []
    for n in range(1, 10):
        quantidade = pares_por_numero + (1 if n <= resto else 0)
        numeros.extend([n, n] * quantidade)
    
    random.shuffle(numeros)
    linhas = [numeros[i:i+COLUNAS] for i in range(0, len(numeros), COLUNAS)]
    return [[(n, 0) for n in linha] for linha in linhas]

def celulas_entre_wrap(grade, l1, c1, l2, c2):
    idx1 = l1 * COLUNAS + c1
    idx2 = l2 * COLUNAS + c2
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    for idx in range(idx1 + 1, idx2):
        l = idx // COLUNAS
        c = idx % COLUNAS
        if grade[l][c][0] != 0:
            return False
    return True

def celulas_entre_diagonal(grade, l1, c1, l2, c2):
    dl = 1 if l2 > l1 else -1
    dc = 1 if c2 > c1 else -1
    l, c = l1 + dl, c1 + dc
    while (l, c) != (l2, c2):
        if grade[l][c][0] != 0:
            return False
        l += dl
        c += dc
    return True

def sao_adjacentes(grade, l1, c1, l2, c2):
    if abs(l1 - l2) <= 1 and abs(c1 - c2) <= 1:
        return True
    if abs(l1 - l2) == abs(c1 - c2):
        if celulas_entre_diagonal(grade, l1, c1, l2, c2):
            return True
    if l1 == l2:
        min_c, max_c = min(c1, c2), max(c1, c2)
        return all(grade[l1][c][0] == 0 for c in range(min_c + 1, max_c))
    if c1 == c2:
        min_l, max_l = min(l1, l2), max(l1, l2)
        return all(grade[l][c1][0] == 0 for l in range(min_l + 1, max_l))
    if l1 != l2 or c1 != c2:
        if celulas_entre_wrap(grade, l1, c1, l2, c2):
            return True
    return False

def adicionar_numeros(grade, linhas_visiveis, vezes_adicionado):
    if vezes_adicionado >= 3:
        return linhas_visiveis, vezes_adicionado
    
    nova_rodada = vezes_adicionado + 1
    numeros_atuais = []
    for linha in range(len(grade)):
        for col in range(COLUNAS):
            if grade[linha][col][0] != 0:
                numeros_atuais.append((grade[linha][col][0], nova_rodada))
    
    pos = 0

    for l in range(len(grade)):
        for c in range(COLUNAS):
            if grade[l][c][0] != 0:
                pos = l * COLUNAS + c + 1
    
    for tupla in numeros_atuais:
        l = pos // COLUNAS
        c = pos % COLUNAS
        if l >= len(grade):
            grade.append([(0, 0)] * COLUNAS)
        grade[l][c] = tupla
        pos += 1
    
    novas_linhas = max(linhas_visiveis, (pos - 1) // COLUNAS + 1)
    return novas_linhas, nova_rodada


def remover_linhas_vazias(grade, linhas_visiveis):
    novas = [linha for linha in grade[:linhas_visiveis] if any(n[0] != 0 for n in linha)]
    linhas_removidas = linhas_visiveis - len(novas)
    if linhas_removidas > 0:
        grade[:linhas_visiveis] = novas
    return linhas_visiveis

def scroll_max(linhas_visiveis):
    altura_total = linhas_visiveis * TAMANHO_CELULA
    return max(0, altura_total - ALTURA_JANELA_GRADE)

grade = criar_grade()
selecionado = None

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEWHEEL:
            scroll_y -= evento.y * TAMANHO_CELULA
            scroll_y = max(0, min(scroll_y, scroll_max(linhas_visiveis)))

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_DOWN:
                scroll_y = min(scroll_y + TAMANHO_CELULA, scroll_max(linhas_visiveis))
            if evento.key == pygame.K_UP:
                scroll_y = max(0, scroll_y - TAMANHO_CELULA)

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if BOTAO_X <= mx <= BOTAO_X + BOTAO_W and BOTAO_Y <= my <= BOTAO_Y + BOTAO_H:
                linhas_visiveis, vezes_adicionado = adicionar_numeros(grade, linhas_visiveis, vezes_adicionado)

            col = (mx - MARGEM_X) // TAMANHO_CELULA
            linha = (my - MARGEM_Y) // TAMANHO_CELULA
            if 0 <= col < COLUNAS and 0 <= linha < len(grade):
                numero, rodada = grade[linha][col]
                if numero == 0:
                    pass
                elif selecionado is None:
                    selecionado = (linha, col)
                else:
                    l1, c1 = selecionado
                    l2, c2 = linha, col
                    if (l1, c1) == (l2, c2):
                        selecionado = None
                    else:
                        n1 = grade[l1][c1][0]
                        n2 = grade[l2][c2][0]
                        if n1 == n2 or n1 + n2 == 10:
                            if sao_adjacentes(grade, l1, c1, l2, c2):
                                grade[l1][c1] = (0, 0)
                                grade[l2][c2] = (0, 0)
                                pontos += 10
                                linhas_visiveis = remover_linhas_vazias(grade, linhas_visiveis)
                        selecionado = None

    tela.fill((18, 18, 24))

    texto_pontos = fonte_pontos.render(f"Pontos: {pontos}", True, (235, 228, 215))
    tela.blit(texto_pontos, (20, 20))

    for linha in range(linhas_visiveis):
        for col in range(COLUNAS):

            x = MARGEM_X + col * TAMANHO_CELULA
            y = MARGEM_Y + linha * TAMANHO_CELULA - scroll_y

            if y < MARGEM_Y or y > MARGEM_Y + ALTURA_JANELA_GRADE:
                continue

            pygame.draw.rect(tela, (60, 60, 70), (x, y, TAMANHO_CELULA, TAMANHO_CELULA), 1)

            if linha >= len(grade):
                continue

            numero, rodada = grade[linha][col]

            if numero == 0:
                continue

            if selecionado == (linha, col):
                pygame.draw.rect(tela, (210, 180, 80), (x, y, TAMANHO_CELULA, TAMANHO_CELULA))
                cor_texto = (18, 18, 24)
            else:
                cor_texto = CORES_RODADA[rodada % len(CORES_RODADA)]

            texto = fonte.render(str(numero), True, cor_texto)
            texto_w = texto.get_width()
            texto_h = texto.get_height()
            tela.blit(texto, (x + (TAMANHO_CELULA - texto_w) // 2, y + (TAMANHO_CELULA - texto_h) // 2))

    superficie_degrade = pygame.Surface((COLUNAS * TAMANHO_CELULA, 80), pygame.SRCALPHA)
    for i in range(80):
        alpha = int((i / 80) * 255)
        pygame.draw.line(superficie_degrade, (18, 18, 24, alpha), (0, i), (COLUNAS * TAMANHO_CELULA, i))
    tela.blit(superficie_degrade, (MARGEM_X, MARGEM_Y + ALTURA_JANELA_GRADE - 80))
    pygame.draw.rect(tela, (18, 18, 24), (MARGEM_X, MARGEM_Y + ALTURA_JANELA_GRADE, COLUNAS * TAMANHO_CELULA, 60))

    cor_botao = (60, 60, 70) if vezes_adicionado < 3 else (40, 40, 45)
    pygame.draw.rect(tela, cor_botao, (BOTAO_X, BOTAO_Y, BOTAO_W, BOTAO_H), border_radius=8)
    texto_botao = fonte_botao.render(f"+ ({3 - vezes_adicionado})", True, (235, 228, 215))
    tela.blit(texto_botao, (BOTAO_X + 15, BOTAO_Y + 8))

    pygame.display.flip()

pygame.quit()