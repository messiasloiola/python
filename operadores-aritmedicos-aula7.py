"""
OPERADORES ARITMEDICOS

+ adicao                ** potência
- subtracao             // divisao inteira
* multiplicacao         % resto da divisao
/ divisao

5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
5 // 2 == 2
5 % 2 == 1

ORDEM DE PRECEDÊNCIA

1 ()
2 **
3 * / // %
4 + -
"""

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:^20}!'.format(nome))  ## :^20 alinhar o nome no centro com 20 caracteres
print('Prazer em te conhecer {:<20}!'.format(nome))  ## :^20 alinhar o nome a esquerda com 20 caracteres
print('Prazer em te conhecer {:>20}!'.format(nome))  ## :^20 alinhar o nome a direita com 20 caracteres
print('Prazer em te conhecer {:=^20}!'.format(nome))  ## :=^20 alinhar o nome no centro com iguais dos lados em 20 caracteres
