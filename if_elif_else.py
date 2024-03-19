# -*- coding: utf-8 -*-
"""if/elif/else.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HkpQGBbpWf7Vu5MzRs5ChrIsF8Xds5lY

**Exercício 1**
"""

#Leia dois números, faça a soma e apresente caso seja maior que 15.

nota1 = float(input("Coloque o primeiro número"))
nota2 = float(input("Coloque o segundo número"))
result = nota1 + nota2

if result > 15:
  print("Aprovado")
else:
  print("Reprovado")

"""**Exercício** **2**"""

#Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.

numero = int(input("Coloque o número"))

if numero > 0:
  print("positivo")

elif numero == 0:
  print("neutro")

else:
  print("negativo")

"""**Exercício 3**

"""

#Leia a idade e informe se a pessoa é maior ou menor de idade

numero = int(input("Coloque sua idade"))

if numero>= 18:
  print("maior de idade")

else:
  print("menor de idade")

"""**Exercício 4**"""

#Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na tela dizendo se está “quente”, “frio” ou “agradável”.

temperatura = float(input("Coloque sua temperatura"))

if temperatura > 20:
  print("Quente")

elif temperatura == 20:
  print("Agradável")

else:
  print("frio")

"""**Exercício 5**"""

# Faça um programa em linguagem Python que leia dois números inteiros e informe se estes são iguais ou diferentes.

numero1 = float(input("Coloque o primeiro número"))
numero2 = float(input("Coloque o segundo número"))

if numero1 == numero2:
  print("iguais")

else:
  print("diferentes")

"""**Exercício 6**"""

#. Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes
#mensagens:  ACESSO PERMITIDO caso a senha seja válida.  ACESSO NEGADO caso a senha seja inválida.

numeros = float(input("Coloque o primeiro número"))

if numeros == 1234:
  print("ACESSO PERMITIDO")

else:
  print("ACESSO NEGADO")

"""**Exercício 7**"""

#. Ler duas notas de um aluno, efetuar a média aritmética e, se a média for maior ou igual a 7, informar que o aluno foi aprovado; se a média for maior ou igual a 5 mas
#menor do que 7, informar que o aluno está de exame; se a média for menor do que 5 informar que o aluno foi reprovado.

nota1 = float(input("Coloque a primeira nota"))
nota2 = float(input("Coloque a segunda nota"))

if (nota1 + nota2) / 2 >= 7:
  print("Aprovado")

elif 5 <= (nota1 + nota2) / 2 >= 5:
  print("Exame")

else:
  print("Reprovado")

"""**Exercício 8**"""

#Desenvolva um programa que recebe do usuário o placar de um jogo de futebol (os gols de cada time) e informe se o resultado foi um empate, se a vitória foi do
#primeiro time ou do segundo time.

time1 = int(input("gols do primeiro time"))
time2 = int(input("gols do segundo time"))

if time1 > time2:
  print("O primeiro time ganhou")

elif time1 == time2:
  print("Empate")

else:
  print("O segundo time ganhou")

"""**Exercício 9**"""

#Faça um Programa que pergunte em que turno você estuda. Peça para digitar Mmatutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa
#Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = (input("Em qual turno você estuda?(M-matutino, V-vespertino, N-noturno)"))

if "m-matutino":
  print("Bom-dia!")

elif "v-vespertino":
  print("Boa tarde!")

elif "n-noturno":
  print("Boa noite!")

else:
  print("Valor inválido")

"""**Exercício 10**"""

#Faça um programa que solicite ao usuário sua idade, depois disso, exiba a classificação etária de acordo com as faixas de valores:
# Criança para 0 até 11 anos;
# Adolescente para 12 até 18 anos;
# Jovem para 19 até 24 anos;
# Adulto para 25 até 40 anos;
# Meia Idade para 41 até 60 anos;
# Idoso acima de 60 anos.

idade = int(input("Coloque sua idade:"))

if idade <= 11:
  print("Criança")

elif idade >=12 and idade <= 18:
  print("Adolescente")

elif idade >= 19 and idade <= 24:
  print("Jovem")

elif idade >= 25 and idade <= 40:
  print("Adulto")

elif idade >= 41 and idade <= 60:
  print("Meia Idade")

else:
  print("Idoso")

"""**Exercício 11**"""

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os
#reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input("Coloque seu salário"))

if salario < 280:
  porcentagem_aplicada = (20/100) * salario
  salario_final = salario + porcentagem_aplicada

  print(f"O saario antes do reajuste é {salario}")
  print("O percentual de aumento será 20%")
  print(f"O valor de aumento será {porcentagem_aplicada}")
  print(f"O novo salario sera {salario_final}")

elif  salario > 280 and salario < 700:
  porcentagem_aplicada = (15/100) * salario
  salario_final = salario + porcentagem_aplicada

  print(f"O saario antes do reajuste é {salario}")
  print("O percentual de aumento será 15%")
  print(f"O valor de aumento será {porcentagem_aplicada}")
  print(f"O novo salario sera {salario_final}")

elif  salario > 700 and salario < 1500:
  porcentagem_aplicada = (10/100) * salario
  salario_final = salario + porcentagem_aplicada

  print(f"O saario antes do reajuste é {salario}")
  print("O percentual de aumento será 10%")
  print(f"O valor de aumento será {porcentagem_aplicada}")
  print(f"O novo salario sera {salario_final}")

elif  salario > 1500:
  porcentagem_aplicada = (5/100) * salario
  salario_final = salario + porcentagem_aplicada

  print(f"O saario antes do reajuste é {salario}")
  print("O percentual de aumento será 5%")
  print(f"O valor de aumento será {porcentagem_aplicada}")
  print(f"O novo salario sera {salario_final}")

"""**Exercício 12**"""

#Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("Coloque um número de 1 a 7"))

if numero == 1:
  print("Domingo")

elif numero == 2:
  print("Segunda")

elif numero == 3:
  print("Terça")

elif numero == 4:
  print("Quarta")

elif numero == 5:
  print("Quinta")

elif numero == 6:
  print("Sexta")

elif numero == 7:
  print("Sábado")

else:
  print("Erro")

"""**Exercício 13**"""

#Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta
#do usuário, faça a devida conversão.

pergunta1 = (input("Quer passar fahrenheit para celsius?"))
pergunta2 = (input("Quer passar celsius para fahrenheit?"))
temperatura = float(input("Insira a temperatura"))

if pergunta2 == "sim":
   fahrenheit_para_celsius = ((temperatura-32)/1.8)
   print(f"O resultado é", {fahrenheit_para_celsius})

else:
     celsius_para_fahrenheit = (1.8*temperatura-32)
     print (f"o resultado é {celsius_para_fahrenheit}")

"""**Exercício 14**"""

#Faça um programa que receba a idade de uma pessoa e imprima sua condição (obrigatória, optativa ou proibida), em relação ao ato de votar, conforme
#apresentado abaixo:
#Pessoas com idade menor que 16 anos são proibidas de votar (proibido);
# Pessoas com idade igual a 16 e menor que 18 anos não são obrigadas a votar (optativo);
# Pessoas com idade igual a 18 e menor que 65 anos são obrigadas a votar (obrigatório);
# Pessoas com idade igual ou maior a 65 anos não são obrigadas a votar (optativo).

idade = int(input("Coloque sua idade"))

if idade < 16:
  print("Proibido")

elif idade >= 16 and idade <= 18:
  print("Optativo")

elif idade >= 18 and idade >= 65:
  print("Obrigatório")

else:
  print("Optativo")

"""**Exercício 15**"""

#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# “Telefonou para a vítima? “
# “Esteve no local do crime?”
# “Mora perto da vítima? “
# “Devia para a vítima? “
# “Já trabalhou com a vítima? “
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
#classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino“. Caso contrário, ele será classificado como “Inocente“.

print("Responda as seguintes perguntas com sim ou não")
psergunta1 = input("Telefonou para a vítima?").lower() #se a pessoa colocar maiusculo ele vai alterar para minusculo
pergunta2 = input("Esteve no local do crime?").lower()
pergunta3 = input("Mora perto da vítima?").lower()
pergunta4 = input("Devia para a vítima?").lower()
pergunta5 = input("Já trabalhou com a vítima?").lower()

positivas = 0

if pergunta1 == "sim":
  positivas += 1
if pergunta2 == "sim":
  positivas += 1
if pergunta3 == "sim":
  positivas += 1
if pergunta4 == "sim":
  positivas += 1
if pergunta5 == "sim":
  positivas += 1

if positivas == 2:
  print("Suspeita")
#elif 3 <+ positivas <= 4: ou
elif positivas >=3 and positivas <=4:
  print("Cumplice")
elif positivas == 5:
  print("bandido")
else:
  print("inocente")

"""**Exercício 16**"""

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Coloque o preço do primeiro produto"))
produto2 =  float(input("Coloque o preço do segundo produto"))
produto3 =  float(input("Coloque o preço do terceiro produto"))

if produto1 < produto2 and produto1 < produto3:
  print("O primeiro produto é mais barato")

elif produto2 < produto1 and produto2 < produto3:
  print("O segundo produto é mais barato")

elif produto3 < produto1 and produto3 < produto2:
  print("O terceiro produto é o mais barato")