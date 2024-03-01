from algorithms.quick_sort import quick_sort

def bucket_sort(vetor):
  maximo, minimo = max(vetor), min(vetor)
  numBuckets = len(vetor)
  tamBucket = (maximo - minimo) / numBuckets
  buckets = [[] for _ in range(numBuckets)]
  for num in vetor:
    indBucket = min(int((num - minimo) / tamBucket), numBuckets - 1)
    buckets[indBucket].append(num)
  for i in range(numBuckets):
    buckets[i] = quick_sort(buckets[i])
  resultado = []
  for bucket in buckets:
    resultado.extend(bucket)
  return resultado