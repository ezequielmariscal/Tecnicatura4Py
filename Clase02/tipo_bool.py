
# Bool contiene los valores True y False
# Los tipos numericos, es false para el 0 (cero), true para los demas valores
valor = 0.0
resultado = bool(valor)
print(f'valor {valor}, resultado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'valor {valor}, resultado: {resultado}')

# Tipo string -> False '', True demas valores
valor = ''
resultado = bool(valor)
print(f'valor {valor}, resultado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'valor {valor}, resultado: {resultado}')

# Tipo colecciones -> False para colecciones vacias, True las demas

# Lista (Array)
valor = []
resultado = bool(valor)
print(f'valor de una lista vacia {valor}, resultado: {resultado}')

valor = [2, 3, 4]
resultado = bool(valor)
print(f'valor lista con elementos{valor}, resultado: {resultado}')

# Tuplas
valor = ()
resultado = bool(valor)
print(f'valor de una tupla vacia {valor}, resultado: {resultado}')

valor = (7,)
resultado = bool(valor)
print(f'valor de una tupla con elementos {valor}, resultado: {resultado}')

# Diccionario
valor = {}
resultado = bool(valor)
print(f'valor de un diccionario vacio {valor}, resultado: {resultado}')

valor = {'Nombre': 'Pepe', 'Apellido': 'Argento'}
resultado = bool(valor)
print(f'valor de un diccionario con elementos {valor}, resultado: {resultado}')

# Sentencias de control bool
if '':
    print('Regresa verdadero')
else:
    print('Regresa falso')

# Ciclos
variable = 3
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')