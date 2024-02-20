import math

cobertura_por_litro = 3
litros_por_lata = 18
valor_lata = 80.0

area = float(input("Digite o tamanho em m²: "))

litros_necessarios = area/cobertura_por_litro

latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)

valor_total = valor_lata * latas_necessarias

print(f"A quantidade de latas necessárias é {latas_necessarias} e o valor total é R${valor_total}")