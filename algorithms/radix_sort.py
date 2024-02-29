def radix_sort(vetor):
  maximu = max(vetor)
  digitos = 0
  while maximu > 0:
    maximu //= 10
    digitos += 1
  for i in range(digitos):
    buckets = [[] for j in range(10)]
    for num in vetor:
      digito = (num // 10**i) % 10
      buckets[digito].append(num)
    vetor = [num for bucket in buckets for num in bucket] 
  return vetor