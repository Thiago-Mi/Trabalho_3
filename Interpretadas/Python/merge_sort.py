import time
import random
import locale
import sys

# Classe para armazenar as métricas
class Metricas:
    def __init__(self):
        self.comparacoes = 0
        self.trocas = 0
        self.tempoExecucao = 0.0  # Armazena o tempo de execução em segundos
        self.memoriaUsada = 0  # Armazena a quantidade de memória usada em bytes

# Função para mesclar duas metades do array
def merge(arr, l, m, r, metricas):
    n1 = m - l + 1
    n2 = r - m

    # Arrays temporários
    L = [0] * n1
    R = [0] * n2
    metricas.memoriaUsada += (n1 + n2) * 4  # Considerando 4 bytes por int

    # Copiar dados para arrays temporários L[] e R[]
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    # Mesclar os arrays temporários de volta em arr[l..r]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        metricas.comparacoes += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar os elementos restantes de L[], se houver
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar os elementos restantes de R[], se houver
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Função recursiva do Merge Sort
def mergeSort(arr, l, r, metricas):
    if l < r:
        m = l + (r - l) // 2

        # Ordenar a primeira e a segunda metade
        mergeSort(arr, l, m, metricas)
        mergeSort(arr, m + 1, r, metricas)

        # Mesclar as metades ordenadas
        merge(arr, l, m, r, metricas)

# Função para imprimir um array
def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print()


# Função para carregar o vetor a partir do arquivo
def carregarVetor(tamanho, caso):
    with open('vetores_input.txt', 'r') as f:
        lines = f.readlines()
        key = f"{tamanho} {caso}:"
        for i in range(len(lines)):
            if lines[i].strip() == key:
                vetor = list(map(int, lines[i + 1].strip().split()))
                return vetor
    return []

# Função principal
def main():
    locale.setlocale(locale.LC_ALL, "Portuguese")
    if len(sys.argv) != 3:
        print("Uso: python insertion_sort.py <tamanho do vetor> <caso>")
        return

    tamanho = int(sys.argv[1])
    caso = sys.argv[2]

    metricas = Metricas()
    arr = carregarVetor(tamanho, caso)


    print("Array inicial: ")
    # printArray(arr)

    # Capturar o tempo de início
    inicio = time.time()
    mergeSort(arr,0,tamanho -1,metricas)
    # Capturar o tempo de término
    fim = time.time()

    # Calcular o tempo de execução em segundos
    metricas.tempoExecucao = fim - inicio


    print("\nMétricas: ")
    print(f"Comparações: {metricas.comparacoes}")
    print(f"Trocas: {metricas.trocas}")
    print(f"Tempo de execução: {metricas.tempoExecucao:.6f} segundos")
    print(f"Memória usada: {metricas.memoriaUsada} bytes")

if __name__ == "__main__":
    main()
