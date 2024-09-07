import numpy as np

def TEU_method(f, a, b, n):
    # a e b são os limites do intervalo
    # n é o número de subintervalos para a transformação
    intervals = []
    x = np.linspace(a, b, n)
    
    for i in range(len(x) - 1):
        if f(x[i]) * f(x[i + 1]) <= 0:
            intervals.append((x[i], x[i + 1]))
    
    return intervals

# Recebe as entradas do usuário
func_str = input("Digite a função f(x): ")
a = float(input("Digite o valor (a): "))
b = float(input("Digite o valor (b): "))
n = int(input("Digite o número de subintervalos (n): "))

# Define a função baseada na entrada do usuário
f = lambda x: eval(func_str)

# Calcula os intervalos contendo raízes
intervals = TEU_method(f, a, b, n)

print("Os intervalos contendo raízes são:")
for interval in intervals:
    print(f"({interval[0]:.2f}, {interval[1]:.2f})")