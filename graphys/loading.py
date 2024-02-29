from algorithms.utils.helpers import sys, time, threading

def loading():
  chars = "/—\\|"
  i = 0
  while not done_loading.is_set():
    sys.stdout.write('\r' + 'Processando ' + chars[i % len(chars)])
    sys.stdout.flush()
    time.sleep(0.1)
    i += 1

done_loading = threading.Event()