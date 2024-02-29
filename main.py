from algorithms.utils.helpers import plt
from graphys.generate_graphs import tamanhos, tempo1, tempo2, tempo3, tempo4

def main():
    plt.figure(figsize=(10, 10))
    plt.plot(tamanhos, tempo1, label='Quick')
    plt.plot(tamanhos, tempo2, label='Merge')
    plt.plot(tamanhos, tempo3, label='Counting')
    plt.plot(tamanhos, tempo4, label='Radix')
    plt.legend(loc='upper left')
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Segundos')
    plt.show()

if __name__ == "__main__":
    main()
