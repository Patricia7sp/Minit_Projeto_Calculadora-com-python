print('--------------------------- Calculadora em python ---------------------------', '\n')

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mult(a, b):
  return a * b

def div(a, b):
  return a / b

def porct(a, b):
   div = a / 100
   multi = div * b
   return multi

print ("Seleciona a opcao desejada:" '\n')
print("1 = Soma")
print("2 = Subtracao")
print("3 = Multiplicacao")
print("4 = Divisao")
print("5 = Porcentagem")

calc = input("Digite sua opcao (1/2/3/4/5): \n")

n1 = int(input("Digite o numero para operacao: \n"))

n2 = int(input("Digite o segundo numero para operacao: \n"))

if calc == '1' :
  print('\n')
  print("Resultado", "=", add(n1, n2))
  print('\n')
  
elif calc == '2':
  print('\n')
  print("Resultado", "=", sub(n1, n2))
  print('\n')

elif calc == '3':
  print('\n')
  print("Resultado", "=", mult(n1, n2))
  print('\n')

elif calc == '4':
  print('\n')
  print("Resultado", "=", div(n1, n2))
  print('\n')

elif calc == '5':
  print('\n')
  print("Resultado", "=", porct(n1,n2))
  print('\n')

else:
  print("Esta Opcao nao existe, :(")
