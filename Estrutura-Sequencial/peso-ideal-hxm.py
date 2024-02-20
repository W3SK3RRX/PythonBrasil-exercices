altura = float(input("Digite a sua altura: "))
sexo = str(input("Digite o seu sexo - Masculino(m), Feminino(f): "))

if sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print(f"Seu peso ideal é {peso_ideal}")