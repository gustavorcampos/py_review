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

# Parei no minuto 40:11
