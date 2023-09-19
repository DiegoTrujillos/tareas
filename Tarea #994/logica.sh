#!/bin/bash
## operaciones lógicas
booleano=true
# Si la variable booleano es true veremos por pantalla "OK"
$booleano && echo "OK" || echo "no es true"
test ${otrobool} || echo "Ahora es falso"
# Mediante && podemos encadenar comandos
valor=6
test $valor -le 6 && echo "Se cumple"
nuevo=${valor}
test ${nuevo} -eq ${valor} && echo "Son los mismo"
echo "Ahora ${nuevo} es lo mismo que ${valor}"
