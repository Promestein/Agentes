import timeit
import ambiente.ambiente as amb

def checarPosicao(ambiente, posicao):
  if ambiente[posicao[0]][posicao[1]] == 0:
    return 0
  elif ambiente[posicao[0]][posicao[1]] == 1:
    return 1
  elif ambiente[posicao[0]][posicao[1]] == 2:
    return 2


def irAtePonto(posicao, ponto):
  if ponto[0] != 0:
    for i in range(0, ponto[0] + 1, 1):
      posicao[0] = i
      #print(posicao, end="")

  if ponto[1] != 0:
    for i in range(0, ponto[1] + 1, 1):
      posicao[1] = i
      #print(posicao, end="")
  return posicao


def pegar(ambiente, posicao, pontuacao):
  pontuacao+=checarPosicao(ambiente, posicao)*10
  ambiente[posicao[0]][posicao[1]] = 0
  return ambiente, pontuacao


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

def executar():
  inicio = timeit.default_timer()
  posicao = [0, 0]
  pontuacao=0

  ambiente, pontos = amb.gerarAmbientePegandoPontos()
  #pontos.sort()
  #print(pontos)

  flag = True
  deveVoltarAnterior = True
  for i in pontos:
    posicao = irAtePonto(posicao, i)
    ambiente, pontuacao = pegar(ambiente, posicao, pontuacao)
    posicao = voltar(ambiente, posicao)
  print(posicao)
  fim = timeit.default_timer()
  print(pontuacao)
  print(fim - inicio)
