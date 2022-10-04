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


  return posicao

def pegar(ambiente, posicao, pontuacao):
  pontuacao+=checarPosicao(ambiente, posicao)*10
  ambiente[posicao[0]][posicao[1]] = 0
  print(pontuacao)
  return ambiente, pontuacao

def voltar(ambiente, posicao):
  for i in range(posicao[0], 0, -1):
    posicao[0] = i
  
  for i in range(posicao[1], 0, -1):
    posicao[1] = i
  

  #amb.mostrarAmbiente(ambiente)
  #print("")
  return posicao

def executar():
  inicio = timeit.default_timer()
  posicao = [0, 0]
  pontuacao = 0

  ambiente = amb.gerarAmbiente()
  print("1")
  flag = True
  while flag:
    posicao = andar(ambiente, posicao)
    if posicao[0] == 20 and posicao[1] == 0:
      posicao = voltar(ambiente, posicao)
      flag = False
      break
    atual = checarPosicao(ambiente, posicao)

    if atual == 1 or atual == 2:
      ambiente, pontuacao = pegar(ambiente, posicao, pontuacao)
      posicao = voltar(ambiente, posicao)

  fim = timeit.default_timer()
  print(pontuacao)
  print(fim - inicio)
