from algorithms.utils.helpers import plt
from graphys.generate_graphs import tamanhos, tempo

def main():
    plt.figure(figsize=(10, 10))
    plt.plot(tamanhos, tempo[0], label='Quick')
    plt.plot(tamanhos, tempo[1], label='Merge')
    plt.plot(tamanhos, tempo[2], label='Counting')
    plt.plot(tamanhos, tempo[3], label='Radix')
    plt.plot(tamanhos, tempo[4], label='Bucket')
    plt.plot(tamanhos, tempo[5], label='Heap')
    plt.legend(loc='upper left')
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Segundos')
    plt.show()

if __name__ == "__main__":
    main()
