renda_anual_salario = float(input("Renda anual com salário: "))
renda_anual_prestacao_servico = float(input("Renda anual com prestação de servico: "))
renda_anual_ganho_capital = float(input("Renda anual com ganho de capital: "))
gastos_medicos = float(input("Gastos médicos: "))
gastos_educacionais = float(input("Gastos educacionais: "))

imposto_sobre_salario = 0.0
imposto_sobre_servico = 0.0
imposto_sobre_ganho = 0.0
imposto_total = 0.0
deducao_total = 0.0
maximo_dedutivel = 0.0
imposto_devido = 0.0

if (renda_anual_salario / 12) < 3000.0:
    imposto_sobre_salario = 0.0
elif (renda_anual_salario / 12) < 5000 and renda_anual_salario >= 3000:
    imposto_sobre_salario = renda_anual_salario * 0.10
elif (renda_anual_salario / 12) > 5000:
    imposto_sobre_salario = renda_anual_salario * 0.20
else:
    print("Salario incorreto.")

if renda_anual_prestacao_servico > 0:
    imposto_sobre_servico += renda_anual_prestacao_servico * 0.15

if renda_anual_ganho_capital > 0:
    imposto_sobre_ganho += renda_anual_ganho_capital * 0.20

imposto_total = imposto_sobre_ganho + imposto_sobre_salario + imposto_sobre_servico
deducao_total += gastos_educacionais + gastos_medicos

print()
print("RELATORIO DE IMPOSTO DE RENDA: ")
print()
print("CONSOLIDADO DE RENDA: ")

print(f"Imposto sobre salário: {imposto_sobre_salario:.2f}")
print(f"Imposto sobre serviços: {imposto_sobre_servico:.2f}")
print(f"Imposto sobre ganho de capital: {imposto_sobre_ganho:.2f}")

print()
print("DEDUÇÕES: ")
if imposto_total * 0.30 < deducao_total * 0.30:
    deducao_total = imposto_total * 0.30
else:
    deducao_total = deducao_total * 0.30
print(f"Máximo dedutível: {deducao_total:.2f}")
print(f"Gastos dedutíveis: {deducao_total:.2f}")

imposto_devido = imposto_total - deducao_total

print()
print("RESUMO: ")
print(f"Imposto bruto total: {imposto_total:.2f}")
print(f"Abatimento: {deducao_total:.2f}")
print(f"Imposto devido: {imposto_devido:.2f}")
