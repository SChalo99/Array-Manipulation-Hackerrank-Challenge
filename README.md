# Array-Manipulation-Hackerrank-Challenge
El objetivo es realizar una manipulación de un arreglo utilizando un conjunto de operaciones que actualizan valores en un rango de índices. La función arrayManipulation recibe un número de elementos en el arreglo (n) y una lista de consultas (queries), donde cada consulta especifica un rango [a, b] y un valor k para agregar a todos los elementos en ese rango.

El proceso consiste en aplicar cada consulta para sumar el valor k a todos los elementos entre los índices a y b, y finalmente devolver el valor máximo en el arreglo después de todas las actualizaciones.

## Ejemplo

n = 10
queries = [[1,5,3],[4,8,7],[6,9,1]]

```
a b k
1 5 3
4 8 7
6 9 1 
```
Luego se deben añadir los valores de k entre los índices a y b inclusive:
```
index->
  1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
```

## En resumen:
Inicializas un arreglo de ceros de tamaño n.
Por cada consulta, sumas un valor k en el rango de índices entre a y b.
Al final, devuelves el valor máximo del arreglo modificado.

El problema se optimizó con la técnica del "difference array". También se deja una solución utilizando recursividad.
