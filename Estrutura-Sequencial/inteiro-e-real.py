import math

i1 = int(input("Digite o primeiro número inteiro: "))
i2 = int(input("Digite o segundo número inteiro: "))
r1 = float(input("Digite o primeiro número real: "))

a = ((i1 * 2) * (i2 / 2))
b = ((i1 * 3) + r1)
c = (math.pow(3, r1))

print(f"O produto do dobro do primeiro com metade do segundo: {a}")
print(f"A soma do triplo do primeiro com o terceiro: {b}")
print(f"O terceiro elevado ao cubo: {c}")