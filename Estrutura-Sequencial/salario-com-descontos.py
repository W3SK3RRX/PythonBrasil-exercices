valor_hora = float(input("Digite o valor ganho por hora: "))
qtd_horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

salario_bruto = qtd_horas_trabalhadas * valor_hora
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f"Salário bruto: R${salario_bruto}\n"
      f"Imposto de renda: R${ir}\n"
      f"INSS: R${inss}\n"
      f"Sindicato: R${sindicato}\n"
      f"Salário líquido: R${salario_liquido}")