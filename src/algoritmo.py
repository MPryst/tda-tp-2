import sys 
import csv

def entrena_to_str(entrena):
    r = []
    for e in entrena:
        if e:
            r.append('Entreno')
        else:
            r.append('Descanso')
    return ', '.join(r)

def max_ganancia(M, D, DIAS):
    return max(M[DIAS-1] + [D[DIAS-1]])

def pos_energia_ganancia(M, dia, ganancia):
    for i, g in enumerate(M[dia]):
        if ganancia == g:
            return i
    return None

def reconstruccion(DIAS, M, D):
    entrena = [None]*DIAS
    max_gan = max_ganancia(M, D, DIAS)
    j = pos_energia_ganancia(M, DIAS-1, max_gan)

    for i in range(DIAS-1, -1, -1):
        if j is None:
            entrena[i] = False
            j = pos_energia_ganancia(M, i-1, D[i])
        else:
            entrena[i] = True
            if j == 0:
                j = None
            else:
                j -= 1
    return entrena

def gan(e, s):
    return min(e, s)

def algoritmo(DIAS, E, S):
    M = [[0]*DIAS for _ in range(DIAS)]
    D = [0]*DIAS

    for i in range(DIAS):
        for j in range(i+1):    
            g = gan(E[i], S[j])
            if j == 0:
                M[i][j] = g + D[i-1]
            else:
                M[i][j] = g + M[i-1][j-1]

        if i > 0:
            D[i] = max(M[i-1] + [D[i-1]])          
        
    return M, D

def write(filename, data):
    with open(filename, 'w+') as f:
        writer = csv.writer(f, delimiter=';')
        for e in data:
            writer.writerow(e)

def load(filename):
    with open(filename) as f:
        lines = f.readlines()

    data = []
    for e in lines:
        data.append(int(e.rstrip()))

    DIAS = data[0]
    E = data[1:DIAS+1]
    S = data[DIAS+1:]
    return DIAS, E, S


def main():
    filename = sys.argv[1]
    DIAS, E, S = load(filename)
    M, D = algoritmo(DIAS, E, S)
    entrena = reconstruccion(DIAS, M, D)
    #print('M: ', M, ' --- D: ', D)
    print('Ganancia maxima:', max_ganancia(M, D, DIAS))
    print('Plan de entrenamiento:', entrena_to_str(entrena))


if __name__ == '__main__':
    main()