nome = input("Digite seu Nome:")
peso = float(input("Coloque seu peso: "))
altura = float(input("Coloque sua altura: "))

imc = peso / (altura ** 2)

print(f"{nome} Seu IMC é: {imc:.2f}")
if imc >= 30:
    print ("⚠️ Cuidado com a Saúde\n")
else:
    print ("✅ Tudo ok\n")

if imc >= 40:
    print ("Classificado como:\n Obesidade Grau III(mórbida)")
elif imc == 39:
    print ("Classificado como:\n Obesidade Grau II")
elif imc >= 34:
    print ("Classificado como:\n Obesidade Grau I")
elif imc >= 29:
    print ("Classificado como:\n Sobrepeso")
elif imc >= 24:
    print ("Classificado como:\n Peso Normal")
elif imc >= 18:
    print ("Classificado como:\n Abaixo do Peso")

Tabela = (input("Ver Tabela?"))
if Tabela == ("Ver"):
    print ("TABELA ABAIXO:\n Abaixo de 18.5: Abaixo do peso\n Abaixo de 24.9: Peso normal\n Abaixo de 29.9: Sobrepeso\n Abaixo de 34.9: Obesidade Grau I\n Abaixo de 39.9: Obesidade Grau II\n 40.0 ou mais: Obesidade Grau III (mórbida)")
elif Tabela == ("Não"):
    print ("Obrigado por usar o site!")