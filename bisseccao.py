import numpy as np

def bisection_method(f, a, b, tol):
    max_iter = 1000
    if f(a) * f(b) >= 0:
        print("O intervalo não contém uma raiz.")
        return None
    
    iter_count = 0
    while (b - a) / 2.0 > tol and iter_count < max_iter:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2.0

# Recebe as entradas do usuário
func_str = input("Digite a função f(x): ")
a = float(input("Digite o valor (a): "))
b = float(input("Digite o valor (b): "))
tol = float(input("Digite a tolerância para o erro: "))

# Define a função baseada na entrada do usuário
f = lambda x: eval(func_str)

# Executa o método da bissecção
root = bisection_method(f, a, b, tol)

if root is not None:
    print(f"A raiz encontrada é: {root:.7f}")
else:
    print("Não foi possível encontrar uma raiz no intervalo dado.")
