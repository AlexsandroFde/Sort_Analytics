def merge_sort(vetor):
  if len(vetor) <= 1:
    return vetor
  meio = len(vetor) // 2
  esquerda = merge_sort(vetor[:meio])
  direita = merge_sort(vetor[meio:])
  resultado = []
  i, j = 0, 0
  while i <= len(esquerda) - 1 and j <= len(direita) - 1:
    if esquerda[i] <= direita[j]:
      resultado.append(esquerda[i])
      i += 1
    else:
      resultado.append(direita[j])
      j += 1
  resultado.extend(esquerda[i:])
  resultado.extend(direita[j:])  
  return resultado