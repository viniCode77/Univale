import random

# Tabuleiro de jogo da velha 

tabuleiro = [
    ["x", "O", "x"],
    ["x", "O", "x"],
    ["O", "O", "x"]
]

# Acesso: [linha][coluna]
print(tabuleiro ) # X (linha 0, col 0)
print(tabuleiro ) # O (linha 1 col 1)
print(tabuleiro )


# Alterar uma posição 
tabuleiro[0][1] = "x"

