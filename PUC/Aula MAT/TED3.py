# Exercício: Faça um programa na forma de MENU em que o usuário escolhe entre os seguintes itens:
# Opção 1: Função do primeiro grau
# Opção 2: Função do segundo grau
# Opção 3: Sair
# Opção 1 - Função do segundo grau:
# Solicitar dados necessários (a e b)
#     1)  Opção para determinar se a função é crescente ou decrescente
#     2) Opção para determinar o zero da função
#     3) **Desafio** Opção para gerar o gráfico da função
#     4) Voltar
# Opção 2 - Função do segundo grau:
# Solicitar dados necessários ( a, b   c)
#     1) Opção para determinar raízes (zeros)
#     2) Opção para determinar vértices
#     3)**Desafio** Opção para gerar o gráfico da função
#     4) Voltar

while True:
    opcao = int(input('[1] Função do primeiro grau\n[2] Função do segundo grau\n[3] Sair'))
    if opcao == 1:
        while True:
            a = int(input('Termo "a": '))
            b = int(input('Termo "b": '))
            perg = int(input(f'ƒ(x)={a}x+{b}\n [1] Saber se a função é crescente ou decrescente\n [2] Zero da função\n [3] Voltar'))
            if perg == 1:
                if a > 0:
                    print(f'A função ƒ(x)={a}x+{b} é crescente')
                elif a < 0:
                    print(f'A função ƒ(x)={a}x+{b} é decrescente')
                elif a == 0:
                    print(f'A função ƒ(x)={a}x+{b} é reta')
            elif perg == 2:
                print(f'O zero da função ƒ(x)={a}x+{b} é {b}')
            elif perg == 3:
                break 
    if opcao == 2:
        while True:
            a = int(input('Termo "a": '))
            b = int(input('Termo "d": '))
            c = int(input('Termo "c": '))
            delta = b**2 + 4*a*c
            perg = int(input(f'ƒ(x)={a}x^2+{b}x+{c}\n [1] Saber as raízes\n [2] Saber o vértice \n [3] Voltar'))
            while True:
                if perg == 1:
                    if delta > 0:
                        print(f'A função ƒ(x)={a}x^2+{b}x+{c} tem 2 raízes reais')
                        r1 = -b + 

            






