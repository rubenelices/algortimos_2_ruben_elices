## Segundo examen de algortimos.
# Rubén Elices.

# 1) Ejercicio POO:
   En el archivo del ejercicio podemos encontrar dos scripts, el primero contiene la clase Genre y es un enum con los distintos generos musicales que pide el ejercicio. El
   segundo contiene la clase Song que importa direcamente desde la clase Genre el enum y además mediante getters y setters te da toda la informacion sobre la canción que pongas, en este caso
   la del ejemplo, Calorro de Estopa.

# 2) Ejercicio recursividad:
   En este ejercicio se implementa un algoritmo para calcular el factorial dde cualquier numero de manera recursiva.
   Precondición: El número dado tiene que ser un entero, no negativo.
   Salida: El programa devolvera un int que diga "El factorial de n es: n!" siendo n un numero cualquiera introducido por el usuario y ! el simbolo que equivale a factorial
   
# 3) Ejercicio ordenacion.
   El método bubble sort: El método bubble sort es un método de ordenación cuya principal caracteristica es su simpleza. EN este método se ordena una lista de números empezando por
   la izquierda del todo de la lista y comparando el primer término con el segundo, a continuacion se compara el segundo término con el tercero, después el tercero con el cuarto... y asi
   sucesivamente hasta que llegamos al final de la lista. Una vez en el final se vuelve a comenzar desde el principio pasando siempre el numero más grande a la derecha con el mismo
   algoritmo de antes. Este algoritmo se repite una y otra vez hasta que la lista queda completamente ordenada, el programa sabe que la lista esta competamente ordenada cuando al hacer
   toda una pasada por la lista no se realiza ningun intercambio. Cabe recalcar que este proceso se repite cada vez con menos elementos (ya que el elemento más grande de cada pasada ya está
   en su lugar correcto y no necesita ser considerado).
   
  # ¿En que casos es conveniente usar este método?.
   El método bubble sort es muy útil para listas pequeñas ya que su simpleza hace que para listas grandes no sea el más eficiente.ç
   También es muy eficiente para ordenar listas que estan ya casi ordenadas.

  # Ejemplo de uso.
   [34, 7, 23, 32, 5]
  Primera Pasada:
    Comparar 34 y 7: 34 es mayor que 7, por lo que se intercambian.
    Lista: [7, 34, 23, 32, 5]
    Comparar 34 y 23: 34 es mayor que 23, por lo que se intercambian.
    Lista: [7, 23, 34, 32, 5]
    Comparar 34 y 32: 34 es mayor que 32, por lo que se intercambian.
    Lista: [7, 23, 32, 34, 5]
    Comparar 34 y 5: 34 es mayor que 5, por lo que se intercambian.
    Lista: [7, 23, 32, 5, 34]
    Al final de esta primero pasada tenemos ya colocado en la ultima posicion al elemento más grande, sin embargo el resto de la lista todavía no esta colocado por lo que hay que hacer
    más "pasadas"
   Segunda Pasada:
    Comparar 7 y 23: 7 es menor que 23, no se intercambia.
    Lista: [7, 23, 32, 5, 34]
    Comparar 23 y 32: 23 es menor que 32, no se intercambia.
    Lista: [7, 23, 32, 5, 34]
    Comparar 32 y 5: 32 es mayor que 5, se intercambian.
    Lista: [7, 23, 5, 32, 34]
   Tercera Pasada:
    Comparar 7 y 23: 7 es menor que 23, no se intercambia.
    Lista: [7, 23, 5, 32, 34]
    Comparar 23 y 5: 23 es mayor que 5, se intercambian.
    Lista: [7, 5, 23, 32, 34]
   Cuarta Pasada:
    Comparar 7 y 5: 7 es mayor que 5, se intercambian.
    Lista: [5, 7, 23, 32, 34]
   Una vez realizada esta pasada, el program realizaria una ultima pasada en la que no cambiaria ningun numero de posición por lo que se daría por terminada la ordenacion.

# 4) Ejercicio functools
  En el archivo de este ejercicio podemos encontrar un script con el código de la clase "SimpleOperations" la cual contienete métodos para calcular descuentos sobre un precio así
  como añadir tasas de impuestos a ese mismo precio. El precio al que se le aplican estos métodos lo introduce el usuario mediante un input.
   
