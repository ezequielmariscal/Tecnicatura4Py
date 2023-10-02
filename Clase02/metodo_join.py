# help(str.join)

#  Concatena cualquier número de cadenas.
#
#  La cadena cuyo método se llama se inserta entre cada cadena dada.
#  El resultado se devuelve como una nueva cadena.
#
# Ejemplo: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

tupla_str = ('Hola', 'alumnos', 'Tecnicatura', 'Universitaria')
mensaje = ' '.join(tupla_str)
print(f'Mensaje: {mensaje}')

