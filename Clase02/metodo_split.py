help(str.split)

#   Devuelve una lista de las subcadenas de la cadena, utilizando sep como cadena separadora.
#
#        sep
#          El separador utilizado para dividir la cadena.
#
#          Cuando se establece en Ninguno (el valor predeterminado), se dividirá en cualquier espacio en blanco.
#          carácter (incluyendo \\n \\r \\t \\f y espacios) y descartará
#          cadenas vacías del resultado.
#        división máxima
#          Número máximo de divisiones (comenzando por la izquierda).
#          -1 (el valor predeterminado) significa que no hay límite.
#
#      Tenga en cuenta que str.split() es útil principalmente para datos que han sido intencionalmente
#      delimitado. Con texto natural que incluye puntuación, considere usar
#      el módulo de expresión regular.

cursos = 'Java JavaScript Node Python Diseno'
lista_cursos = cursos.split()
print(f'Lista de cursos: {lista_cursos}')
print(type(lista_cursos))