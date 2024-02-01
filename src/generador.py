import sys
import random 

def params_invalidos():
  print('Uso: python generador.py <cantidad de dias> [seed]')
  exit(1)

def parsear_params():
  if (len(sys.argv) < 2):
    params_invalidos()

  dias = int(sys.argv[1])

  if (dias < 1):
    params_invalidos()

  if (len(sys.argv) > 2):
    seed = sys.argv[2]
  else:
    seed = None

  return dias, seed

def generar_entrenamiento():
  return random.randint(10, 100)

def generar_energias(dias):
  energias = []
  for i in range(0, dias):
    energias.append(random.randint(1, 100))
  energias.sort(reverse=True)
  return energias

def main():
  dias, seed = parsear_params()

  if (seed):
    random.seed(seed)

  # Header
  print(dias)
  # Entrenamientos
  for i in range(0, dias):
    print(generar_entrenamiento())
  # Energia
  energias = generar_energias(dias)
  for energia in energias:
    print(energia)

main()