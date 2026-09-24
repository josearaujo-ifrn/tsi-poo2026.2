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

print("\nInicio da Questão 14: \n")

for numeros in range(101):
    print(numeros)

print("\nFim da Questão 14")
print("-------------------------")

print("\nInicio da Questão 15: \n")

for numeros in range(100, 0, -1):
    print(numeros)

print("\nFim da Questão 15")
print("-------------------------")

print("\nInicio da Questão 16: \n")

inicio = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))
somatorio = 0

print(f"Os números do intervalo entre {inicio} e {final}:")
for numeros in range(inicio,final + 1):
    somatorio += numeros
    print(numeros)

print(f"O somatório dos números do intervalo é: {somatorio}")
print("\nFim da Questão 16")
print("-------------------------")

print("\nInicio da Questão 17: \n")
somatorio = 0

for numeros in range(10):
    numero = int(input("Digite o número: "))
    somatorio += numero

print(f"O somatório dos 10 números digitados: {somatorio}")

print("\nFim da Questão 17")
print("-------------------------")

print("\nInicio da Questão 18: \n")
somatorio = 0

for numeros in range(5):
    numero = int(input("Digite o número: "))
    if numero < 10:
        somatorio += numero

print(f"O somatório dos números menores que 10: {somatorio}")

print("\nFim da Questão 18")
print("-------------------------")

print("\nInicio da Questão 19: \n")
somatorio = 0

for numeros in range(5):
    numero = int(input("Digite o número: "))
    if numero >= 10 and numero < 20:
        somatorio += numero

print(f"O somatório dos números maiores ou iguais a 10 e menores que 20: {somatorio}")

print("\nFim da Questão 19")
print("-------------------------")

print("nInicio da Questão 20: \n")
somatorio = 0

for numeros in range(5):
    numero = int(input("Digite o número: "))
    if numero % 2 == 0:
        somatorio += numero

print(f"O somatório dos números pares: {somatorio}")

print("\nFim da Questão 20")
print("-------------------------")

print("\nInicio da Questão 21: \n")

qtd = int(input("Digite a quantidade de valores: "))
par = 0

for i in range(qtd):
    numero = int(input("Digite o número: "))
    if numero % 2 == 0:
        par += 1

print(f"A quantidade de números pares é: {par}")
print("\nFim da Questão 21")
print("-------------------------")

print("\nInicio da Questão 22: \n")

posicoes_pares = 0
posicoes_impares = 0

for i in range(10):
    numero = int(input("Digite o número: "))
    if i % 2 == 0:
        posicoes_impares += numero # quando coloquei par, estava somando ao contrario, tive que inverter a ordem
    else:
        posicoes_pares += numero

print(f"Soma das posições pares: {posicoes_pares}")
print(f"Soma das posições ímpares: {posicoes_impares}")

if posicoes_pares > posicoes_impares:
    print("A soma das posições pares é maior que das posições impares")
elif posicoes_impares > posicoes_pares:
    print("A soma das posições impares é maior que das posições pares")
else: 
    print("Ambos são iguais")

print("\nFim da Questão 22")
print("-------------------------")

print("\nInicio da Questão 23: \n")

numeros_pares = 0
numeros_impares = 0

for i in range(10):
    numero = int(input("Digite o número: "))
    if numero % 2 == 0:
        numeros_pares += numero 
    else:
        numeros_impares += numero

print(f"Soma dos números pares: {numeros_pares}")
print(f"Soma dos números ímpares: {numeros_impares}")

if numeros_pares > numeros_impares:
    print("A soma dos números pares é maior que dos números impares")
elif numeros_impares > numeros_pares:
    print("A soma dss números impares é maior que dos números pares")
else: 
    print("Ambos são iguais")

print("\nFim da Questão 23")
print("-------------------------")

print("\nInicio da Questão 24: \n")

total = int(input("Digite o total de números que vão ser somados: "))
soma = 0

for i in range(total):
    numero = int(input("Digite o número: "))
    soma += numero

print(f"o total dos números é {soma}")

print("\nFim da Questão 24")
print("-------------------------")

print("\nInicio da Questão 25: \n")

print(f"Os números divisiveis por 7 e não multiplos de 5 entre 1000 e 3000 são:")
for i in range(1000, 3000):
    if i % 7 == 0 and i % 5 != 0:
        print(i)

print("\nFim da Questão 25")
print("-------------------------")

print("\nInicio da Questão 26: \n")

quantidade_pares = 0
quantidade_impares = 0
while (True):
    numeros = int(input("Digite o número: "))
    if numeros < 0:
        break
    elif numeros % 2 == 0:
       quantidade_pares += 1
    elif numeros % 2 != 0:
        quantidade_impares += 1
print(f"A quantidade de pares é: {quantidade_pares}")
print(f"A quantidade de ímpares é: {quantidade_impares}")

print("\nFim da Questão 26")
print("-------------------------")

print("\nInicio da Questão 27: \n")

total_numeros = int(input("Digite um número: "))

for i in range(1, total_numeros + 1):
    if i % 3 == 0:
        print("PI")
    elif i % 7 == 0:
        print("PA")
    elif i % 3 and i % 7 == 0:
        print("POW")
    else:
        print(i)

print("\nFim da Questão 27")
print("-------------------------")