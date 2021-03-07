from random import randint

class CriaTabuleiro:
    def __init__(self, num_linhas, num_colunas):
        self.tabuleiro = []
        for i in range(num_linhas):         # Construir a matriz por cada elemento
            self.linha = []
            for j in range(num_colunas):
                self.elemento = randint(0, 10)
                self.linha.append(self.elemento)
            self.tabuleiro.append(self.linha)
        
        for l in range(num_linhas-1):       # Imprimir em formato de matriz
            for c in range(num_colunas-1):
                print(f'[{self.tabuleiro[l][c]:^5}]', end=" ")
            print()

CriaTabuleiro(16, 16)