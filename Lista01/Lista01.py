print("---Estruturas Sequenciais---")
print("Inicio da Questão 01: \n")

nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))
nota4 = int(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"\nAs notas digitadas foram: {nota1}, {nota2}, {nota3}, {nota4}")
print(f"A média aritmética foi: {media}")
print("\nFim da Questão 01")
print("-------------------------")

print("\nInicio da Questão 02: \n")

anos = int(input("Digite os anos: "))
meses = int(input("Digite os meses: "))
dias = int(input("Digite os dias: "))

anos_em_dias = anos * 365
meses_em_dias = meses * 30
total_dias = anos_em_dias + meses_em_dias + dias

print(f"A idade em dias é: {total_dias}")
print("\nFim da Questão 02")
print("-------------------------")

print("\nInicio da Questão 03: \n")

horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))

horas_em_minutos = horas * 60

total_minutos = horas_em_minutos + minutos

print(f"O tempo em minutos que passou foi: {total_minutos}")
print("\nFim da Questão 03")
print("-------------------------")

print("\nInicio da Questão 04: \n")

nome_completo = input("Digite o nome completo: ")
horas_trabalhadas = int(input("Digite as horas trabalhadas por mês: "))
valor_hora_trabalhada = int(input("Digite o valor que recebe por hora trabalhada: "))
numero_filhos = int(input("Digite o número de filhos: "))

salario_inicial = horas_trabalhadas * valor_hora_trabalhada
salario_final = salario_inicial + (salario_inicial * (0.03 * numero_filhos))

print(f"\nO salário bruto de {nome_completo} é: {salario_inicial}")
print(f"O salário de {nome_completo} com bônus é: {salario_final}")
print("\nFim da Questão 04")
print("-------------------------")

print("\nInicio da Questão 05: \n")

largura = int(input("Digite a largura da sala: "))
profundidade = int(input("Digite a profundidade da sala: "))

area = largura * profundidade

total_lampadas = area * 18 / 60

print(f"O total de lâmpadas necessárias é: {total_lampadas} lâmpadas")

print("\nFim da Questão 05")
print("-------------------------")

print("\nInicio da Questão 06: \n")

votos_brancos = int(input("Digite o total de votos brancos: "))
votos_nulos = int(input("Digite o total de votos nulos: "))
votos_validos = int(input("Digite o total de votos válidos: "))

total_votos = votos_brancos + votos_nulos + votos_validos

porcentagem_brancos = (votos_brancos / total_votos) * 100
porcentagem_nulos = (votos_nulos / total_votos) * 100
porcentagem_validos = (votos_validos / total_votos) * 100

print(f"\nA porcentagem dos votos brancos foi: {porcentagem_brancos}%")
print(f"A porcentagem dos votos nulos foi: {porcentagem_nulos}%")
print(f"A porcentagem dos votos válidos foi: {porcentagem_validos}%")
print("\nFim da Questão 06")
print("-------------------------")

print("\nInicio da Questão 07: \n")

graus_fahrenheit = float(input("Digite a quantidade de graus fahrenheit: "))

celsius = (graus_fahrenheit - 32) / 9 * 5

print(f"\n{graus_fahrenheit}°F em Celsius é {celsius}°C")
print("\nFim da Questão 07")
print("-------------------------")

print("Inicio da Questão 08: \n")

preco_carro = int(input("Digite o preço do carro: "))

percentual_distribuidor = preco_carro * 0.28
impostos = preco_carro * 0.45
preco_total = preco_carro + percentual_distribuidor + impostos

print(f"\nO preço de fábrica do carro é: R${preco_carro}")
print(f"O preço final do carro é: R${preco_total}")
print("\nFim da Questão 08")
print("-------------------------")

print("\n---Estruturas Condicionais---")

print("Inicio da Questão 09: \n")

numero_09 = int(input("Digite um número de 1 a 10: "))

if numero_09 >= 1 and numero_09 <= 10:
    print("O número digitado está DENTRO da faixa solicitada.")
else:
    print("O número digitado está FORA da faixa solicitada.")

print("\nFim da Questão 09")
print("-------------------------")

print("Inicio da Questão 10: \n")

numero_10_01 = int(input("Digite o primeiro número: "))
numero_10_02 = int(input("Digite o segundo número: "))

if numero_10_01 > numero_10_02:
    print(f"O primeiro número ({numero_10_01}) é maior que o segundo número ({numero_10_02})")
elif numero_10_02 > numero_10_01:
    print(f"O segundo número ({numero_10_02}) é maior que o primeiro número ({numero_10_01})")
else:
    print(f"O primeiro número ({numero_10_01}) é igual ao segundo número ({numero_10_02})")

print("\nFim da Questão 10")
print("-------------------------")

print("Inicio da Questão 11: \n")

numero_11_01 = int(input("Digite o primeiro número: "))
numero_11_02 = int(input("Digite o segundo número: "))

if numero_11_01 > numero_11_02:
    print(f"O maior número é {numero_11_01} e o menor número é {numero_11_02}")
    print(f"A diferença entre {numero_11_01} e {numero_11_02} é: ",numero_11_01 - numero_11_02)
else:
    print(f"O maior número é {numero_11_02} e o menor número é {numero_11_01}")
    print(f"A diferença entre {numero_11_02} e {numero_11_01} é: ",numero_11_02 - numero_11_01)

print("\nFim da Questão 11")
print("-------------------------")

print("Inicio da Questão 12: \n")

numero_12_01 = int(input("Digite o primeiro número: "))
numero_12_02 = int(input("Digite o segundo número: "))
numero_12_03 = int(input("Digite o terceiro número: "))

numeros = (numero_12_01, numero_12_02, numero_12_03)
ordem_crescente = sorted(numeros)
print(f"A ordem crescente é: {ordem_crescente}")

print("\nFim da Questão 12")
print("-------------------------")

print("Inicio da Questão 13: \n")

numero_13_01 = int(input("Digite o primeiro número: "))
numero_13_02 = int(input("Digite o segundo número: "))
numero_13_03 = int(input("Digite o terceiro número: "))
ordem = input("Qual ordem? (crescente / decrescente): ").lower()

numeros = (numero_13_01, numero_13_02, numero_13_03)
ordem_crescente = sorted(numeros)
ordem_decrescente = sorted(numeros, reverse= True)

if ordem == "crescente":
    print(f"A ordem crescente é: {ordem_crescente}")
else:
    print(f"A ordem decrescente é: {ordem_decrescente}")

print("\nFim da Questão 13")
print("-------------------------")

print("\n---Estruturas de Repetição---")