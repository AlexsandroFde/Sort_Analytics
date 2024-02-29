def counting_sort(vetor):
  maximo = max(vetor)
  aux = [0] * (maximo + 1)
  for num in vetor:
    aux[num] += 1
  resultado = []
  for i in range(len(aux)):
    while aux[i] > 0:
      resultado.append(i)
      aux[i] -= 1
  return resultado