import ambiente.ambiente as amb
import timeit

def checarPosicao(ambiente, posicao):
  if ambiente[posicao[0]][posicao[1]] == 0:
    return 0
  elif ambiente[posicao[0]][posicao[1]] == 1:
    return 1
  elif ambiente[posicao[0]][posicao[1]] == 2:
    return 2


def andar(ambiente, posicao):
  if posicao[0] % 2 == 0 and posicao[1] == 19:
    posicao[0] += 1
  elif posicao[0] % 2 != 0 and posicao[1] == 0:
    posicao[0] += 1
  elif ((posicao[0] % 2) == 0) or (posicao[0] == 0):
    posicao[1] += 1
  else:
    posicao[1] -= 1
  #print(posicao, end="")

  return posicao


def pegar(ambiente, posicao, anterior, pontuacao):
  pontuacao+=checarPosicao(ambiente, posicao)*10
  ambiente[posicao[0]][posicao[1]] = 0
  anterior[0], anterior[1] = posicao[0], posicao[1]
  return ambiente, anterior, pontuacao


def voltar(ambiente, posicao):
  for i in range(posicao[0], -1, -1):
    posicao[0] = i
    #print(posicao, end="")
  for i in range(posicao[1], -1, -1):
    posicao[1] = i
    #print(posicao, end="")
  #print(posicao)

  #amb.mostrarAmbiente(ambiente)
  #print("")
  return posicao


def voltarAnterior(ambiente, anterior, posicao):
  if anterior[0] != 0:
    for i in range(0, anterior[0] + 1, 1):
      posicao[0] = i

  if anterior[1] != 0:
    for i in range(0, anterior[1] + 1, 1):
      posicao[1] = i
  return posicao

def executar():
  inicio = timeit.default_timer()
  posicao = [0, 0]
  anterior = [0, 0]
  pontuacao = 0

  ambiente = amb.gerarAmbiente()
  print("2")
  flag = True
  deveVoltarAnterior = True
  while flag:
    '''
    if anterior[0] != 0 and anterior[1] != 0 and deveVoltarAnterior:
      posicao = voltarAnterior(ambiente, anterior, posicao)
      deveVoltarAnterior = False
    '''

    posicao = andar(ambiente, posicao)
    if posicao[0] == 20 and posicao[1] == 0:
      posicao = voltar(ambiente, posicao)
      flag = False
      break
    atual = checarPosicao(ambiente, posicao)

    if atual == 1 or atual == 2:
      ambiente, anterior, pontuacao = pegar(ambiente, posicao, anterior, pontuacao)
      posicao = voltar(ambiente, posicao)
      posicao = voltarAnterior(ambiente, anterior, posicao)
      #deveVoltarAnterior = True

      #andar(ambiente, posicao)
    
  fim = timeit.default_timer()
  print(pontuacao)
  print(fim - inicio)

