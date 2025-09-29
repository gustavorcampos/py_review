# Inicio da Revisão em 26/09/2025

# Data Types
varInt = 123
varFloat = 2727.0
varStr = 'GRC'
varBool = True

# Print
print(f"Nome: {varStr}")
print(varInt, varBool)  # Exemplo de uso da vírgula gerando espaço entre os valores
print("Exemplo refente ao END criando uma nova linha de log", end='\n\n')
print("Continuando para o exemplo acima (pulou uma linha")
print("Exemplo refente ao END juntando informação", end=' | ')
print("Continuando para o exemplo acima (juntou informação)")

# Variables
# Manter o formato de _ entre os nomes
var_nome_correto = ""
# Evitar números

# Input
# nome_digitado = input('Digite seu nome: ')
# print(f'Nome digitado: {nome_digitado}')

# Arithmetic Operator
x = 10
y = 3
result = x // y  # A divisão com uma barra só, ou seja x / y daria 3.3333333333333335.
print(result)
result = x % 3  # Resto da divisão
print(result)

# String Methods
var_str = 'Gustavo Rocha Campos'
print(var_str.split(' '))
print(var_str.upper())
print(var_str.capitalize())
print(var_str.casefold())
print(var_str.count('a'))
x = 'hello'
y = 3
print(x * y)

# Conditional Operators
# == Equal
# != Not Equal
x = 'hello'
y = 'hello'
print(x == y)
print(x != y)
# É possível fazer comparação entre letras, pois em PY existe uma ordem numérica
print(ord('a'))
print(ord('z'))
print('a' > 'z')

# If
x = 3
y = 5
if x > y:
    print(f'If: {True}')
elif x * 2 > y:
    print(f'If * 2: {True}')
else:
    print(f'If: {False}')

# List & Tuples
lista_x = ['Gustavo', True, 123]  # Posso armazenar diferente tipos de var's
print(f'Lista: {len(lista_x)}')
lista_x.append('Append')  # Inserir elemento no final da lista
print(f'Lista: {lista_x}')
lista_x.extend([1, 2, 3, 4, 5])  # Inserir outro conjunto na lista
print(f'Lista extend: {lista_x}')
lista_x.pop()  # Remove o último elemento da lista ou pode passar o index
print(f'Lista pop: {lista_x}')
lista_x.pop(lista_x.index(123))
print(f'Lista remove index {lista_x}')  # Valor 123 removido
lista_x.insert(0, 'GRC Index')
print(f'Lista insert index {lista_x}')
lista_x[1] = 'Gustavo X'
print(f'Lista alterando elemento {lista_x}')
# Tuples são imutáveis - Sem alterações
var_tupla = (0, 2, 3)
print(var_tupla)

# For loops
x = [1, 5, 9, 10]
for i, element in enumerate(x):
    print(i, element)
for i in range(10):
    print(i)

# While
x = [1, 2, 3, 4, 45]
i = 0
while i < 10:
    print('run')
    i += 1

# Slice Operator
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = 'hello'
# sliced = [start:stop:step]
print(x[-1:])

# Dictionaries
x = {'keyex': 'valuex'}
print(x['keyex'])
print('keyex' in x)
for key in x:
    print(x[key])

# Comprehensions
x = [x for x in range(5)]
print(x)
x = [['Teste' for i in range(5)] for x in range(5)]
print(x)


# Functions
def func_teste(x_in, y_in, f_in=None):
    print(f'Run function with value x {x_in} and y {y_in}')
    z = x_in + y_in
    print(f_in)
    return z, x_in * 5  # Retorno de mais de uma valor retorna Tupla


var_z = func_teste(1, 2)
print(f'Var Z: {var_z}')
r1, r2 = func_teste(1, 2)  # Exemplo para retornar var's especificas vs Tupla acima
print(r1)
print(r2)
x = [1, 2, 3, 4, 5]
print(*x)
# *x retorna cada valor da lista separado por espaço (unpacking)
# * para listas e duplas e ** para dicionários

# Exceptions
# Raise Exception('Bad')

# Try Cacth
try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print('Continue')

# Lambda
# result = lambda x: x + 5
# print(result(5))

# Map & Filter
x = [1, 2, 3, 4, 5, 6, 7, 8]
mp = map(lambda t: t + 2, x)
print(list(mp))
# Filter retorna bool
mp = filter(lambda t: t > 3, x)
print(list(mp))

# Parei no minuto 57:52
