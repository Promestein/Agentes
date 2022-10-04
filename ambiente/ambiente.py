from random import randint

def vermelho():
  print("\033[1;31m", end=" ")


def azul():
  print("\033[1;34m", end=" ")


def amarelo():
  print("\033[1;30m", end=" ")


#Gerando ambiente
def gerarAmbiente():
  ambiente = []

  for i in range(0, 20):
    ambiente.append([])
    for j in range(0, 20):
      ambiente[i].append(0)

  ambiente, pontos = gerarPontos(ambiente, 1)
  ambiente, pontos = gerarPontos(ambiente, 2)

  #mostrarAmbiente(ambiente)
  return ambiente


def gerarAmbientePegandoPontos():
  ambiente = []

  for i in range(0, 20):
    ambiente.append([])
    for j in range(0, 20):
      ambiente[i].append(0)

  print(len(ambiente))

  ambiente, pontos1 = gerarPontos(ambiente, 1)
  ambiente, pontos2 = gerarPontos(ambiente, 2)
  pontos1.pop(0)
  pontos2.pop(0)
  pontos = pontos1 + pontos2
  print("\n")
  
  #mostrarAmbiente(ambiente)
  return ambiente, pontos


def gerarPontos(ambiente, valor):
  pontos = [[0, 0]]
  for i in range(0, 10, 1):
    diferente = True
    while diferente == True:
      x = randint(0, 19)
      y = randint(0, 19)

      for i in pontos:
        if i[0] != x and i[1] != y:
          diferente = False
        else:
          diferente = True
          break
      if diferente==False:
        ambiente[x][y] = valor
        pontos.append([x, y])
  return ambiente, pontos


def mostrarAmbiente(ambiente):
  for i in range(0, 100):
    for j in range(0, 100):
      if (ambiente[i][j] == 1):
        vermelho()
      elif (ambiente[i][j] == 2):
        azul()
      else:
        amarelo()

      print(ambiente[i][j], end="  ")
    print("")
  return ambiente

#ambiente = gerarAmbiente()
#print(pontos)
