def heap(vetor, n, i):
  pai = i
  esq = 2 * i + 1
  dir = 2 * i + 2  
  if esq < n and vetor[esq] > vetor[pai]:
    pai = esq
  if dir < n and vetor[dir] > vetor[pai]:
    pai = dir 
  if pai != i:
    vetor[i], vetor[pai] = vetor[pai], vetor[i]
    heap(vetor, n, pai)

def heap_sort(vetor):
  n = len(vetor)
  for i in range(n // 2 - 1, -1, -1):
    heap(vetor, n, i)
  for i in range(n - 1, 0, -1):
    vetor[0], vetor[i] = vetor[i], vetor[0]
    heap(vetor, i, 0)  
  return vetor