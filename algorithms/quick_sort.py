def quick_sort(vetor):
  if len(vetor) <= 1:
    return vetor
  else:
    pivo = vetor[len(vetor)//2]
    menores = [x for x in vetor[1:] if x < pivo]
    maiores = [x for x in vetor[1:] if x >= pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)