import numpy as np

def numerical_derivative(f, x):
    h=1e-8
    """Calcula a derivada numérica de uma função f em x usando diferenças finitas."""
    return (f(x + h) - f(x - h)) / (2 * h)

def newton_raphson_method(f, x0, tol):
    max_iter = 1000
    x_value = x0
    iter_count = 0
    
    while abs(f(x_value)) > tol and iter_count < max_iter:
        try:
            df = numerical_derivative(f, x_value)
            x_value = x_value - f(x_value) / df
        except ZeroDivisionError:
            print("Derivada zero! Não é possível continuar.")
            return None
        iter_count += 1

    if abs(f(x_value)) <= tol:
        return x_value
    else:
        print("Número máximo de iterações atingido. O método não convergiu.")
        return None

# Recebe as entradas do usuário
func_str = input("Digite a função f(x): ")
x0 = float(input("Digite o valor inicial (x0): "))
tol = float(input("Digite a tolerância para o erro: "))

# Define a função baseada na entrada do usuário
f = lambda x: eval(func_str)

# Executa o método de Newton-Raphson
root = newton_raphson_method(f, x0, tol)

if root is not None:
    print(f"A raiz encontrada é: {root:.7f}")
else:
    print("Não foi possível encontrar uma raiz com o método Newton-Raphson.")
