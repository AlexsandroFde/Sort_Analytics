from algorithms.utils.helpers import np, time, threading
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort
from algorithms.counting_sort import counting_sort
from algorithms.radix_sort import radix_sort
from algorithms.bucket_sort import bucket_sort
from algorithms.heap_sort import heap_sort
from graphys.loading import loading, done_loading

tempo = [[] for _ in range(6)]
tamanhos = np.arange(10000, 100001, 5000)
funcoes = [quick_sort, merge_sort, counting_sort, radix_sort, bucket_sort, heap_sort]

loading_thread = threading.Thread(target=loading)
loading_thread.start()

for tam in tamanhos:
  for i in range(len(funcoes)):
    l = np.random.randint(0, 10*tam, tam)
    inicio = time.perf_counter()
    ls = funcoes[i](l)
    fim = time.perf_counter()
    tempo[i].append(fim-inicio)

done_loading.set()
loading_thread.join()