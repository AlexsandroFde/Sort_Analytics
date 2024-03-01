from algorithms.utils.helpers import plt
from graphys.generate_graphs import tamanhos, tempo

def main():
    plt.figure(figsize=(10, 10))

    cores = ['blue', 'orange', 'green', 'red', 'purple', 'brown']
    marcadores = ['o', 's', '^', 'D', 'P', 'X']

    for _, (t, l, c, m) in enumerate(zip(tempo, ['Quick', 'Merge', 'Counting', 'Radix', 'Bucket', 'Heap'], cores, marcadores)):
        plt.plot(tamanhos, t, label=l, color=c, marker=m)

    plt.legend(loc='upper left')
    plt.xlabel('Tamanho da lista')
    plt.ylabel('Segundos')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
