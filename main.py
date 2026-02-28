from functions.addm import addm
from functions.subtractm import subtractm
from functions.transposem import transposem
from functions.multiplym import multiplym

import os
import sys

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

print("\n---------------------------------------- Bem vindo(a) ao CMatrixD ----------------------------------------\n")

# operação
while True:
    try:
        print("Primeiramente, informe o tipo de operação que quer performar, digitando apenas o número: ")
        print("1: Adição")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Transposição")
        op = input()

        if op not in ("1", "2", "3", "4"):
            print("Entrada inválida. A entrada deve ser um dos números listados.")
            continue
        break

    except (ValueError):
        print("Entrada inválida. Digite UM número INTEIRO correspondente aos 4 listados.")
    except (KeyboardInterrupt, EOFError):
        print("\nEntrada cancelada pelo usuário.")
        input("\nPrograma finalizado. Pressione ENTER para sair...")
        sys.exit()

if op != "4":
    # matriz 1
    while True:
        try:
            lines1, rows1 = input("Informe o número de linhas e colunas de sua primeira matriz respectivamente, separados por um espaço: ").split()
            lines1, rows1 = int(lines1), int(rows1)

            if lines1 <= 0 or rows1 <= 0:
                print("Entrada inválida. As entradas devem ser maiores que 0.")
                continue

            break

        except (ValueError):
            print("Entrada inválida. Digite DOIS números INTEIROS separados por um ESPAÇO.")
        except (KeyboardInterrupt, EOFError):
            print("\nEntrada cancelada pelo usuário.")
            input("\nPrograma finalizado. Pressione ENTER para sair...")
            sys.exit()
    m1 = []
    for i in range(lines1):
        vals = input(f"Digite os valores da linha {i+1} (separados por espaço): ")
        parts = vals.split()
        line = []
        for p in parts:
            line.append(float(p))
        m1.append(line)

    # matriz 2
    while True:
        try:
            lines2, rows2 = input("Informe o número de linhas e colunas de sua segunda matriz respectivamente, separados por um espaço: ").split()
            lines2, rows2 = int(lines2), int(rows2)

            if lines2 <= 0 or rows2 <= 0:
                print("Entrada inválida. As entradas devem ser maiores que 0.")
                continue

            break

        except (ValueError):
            print("Entrada inválida. Digite DOIS números INTEIROS separados por um ESPAÇO.")
        except (KeyboardInterrupt, EOFError):
            print("\nEntrada cancelada pelo usuário.")
            input("\nPrograma finalizado. Pressione ENTER para sair...")
            sys.exit()
    m2 = []
    for i in range(lines2):
        vals = input(f"Digite os valores da linha {i+1} (separados por espaço): ")
        parts = vals.split()
        line = []
        for p in parts:
            line.append(float(p))
        m2.append(line)
