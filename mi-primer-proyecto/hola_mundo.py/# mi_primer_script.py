# mi_primer_script.py 
print("¡Hola, Github!")

# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Calcular números primos entre 1 y 1000
primos = []

for n in range(1, 1001):
    if es_primo(n):
        primos.append(n)

# Mostrar resultados
print("Números primos entre 1 y 1000:")
print(primos)
