# tda-tp-2
Trabajo Práctico 2: Programación Dinámica

# Algoritmo
El algoritmo de solución recibe por parámetro la ubicación del archivo con los datos a resolver, con el formato propuesto por la cátedra, y al terminar imprime el valor de la ganancia obtenida, y el plan de entrenamiento

En el código fuente se cuenta con la lista de ejemplos provistos por la cátedra, así como otros propuestos por nosotros. 
Para ejecutar alguno:
```bash
python3 algoritmo.py ./data/10.txt 
```

Lo que dará por resutado
```bash
Ganancia maxima: 380
Plan de entrenamiento: Entreno, Descanso, Entreno, Descanso, Entreno, Entreno, Entreno, Entreno, Entreno, Entreno
```

# Sets de datos
##Formato propuesto por la cátedra
```bash
En la primera línea el valor de la cantidad de días a considerar (n)
En las siguientes n líneas, las ganancias de dichos días (nuestros e_i).
En las siguientes n líneas, la energía con la que se cuenta al día 1, 2, 3, ..., n de estar entrenando sin haber descansando previamente (nuestros s_i)
```

## Generador

Para generar un archivo de ejemplo, se ejecuta el script `generador.py` y se imprime el resultado por stdout

### Uso del script
```bash
python3 generador.py <cantidad de días> [seed]
```

Por ejemplo:

```bash
python3 generador.py 5 73
```

Imprime por consola:

```
5
20
51
72
14
91
97
88
61
54
19
```

Dónde, en la primer línea, el 5 corresponde a la cantidad de días.

Las siguientes 5 líneas las ganancias:

```
20
51
72
14
91
```

Y las últimas 5 líneas las energias correspondientes a cada día, si no se descansa:
```
97
88
61
54
19
```

Para generar un archivo que se pueda usar en el algoritmo principal, se pude redireccionar el stdout:

```bash
python3 generador.py 5 73 > ejemplo.dat
```