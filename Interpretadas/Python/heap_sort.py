import sys
import time
import random
import locale

# Classe para armazenar as métricas
class Metricas:
    def __init__(self):
        self.comparacoes = 0
        self.trocas = 0
        self.tempoExecucao = 0.0  # Armazena o tempo de execução em segundos
        self.memoriaUsada = 0  # Armazena a quantidade de memória usada em bytes

# Implementação do Heap Sort
def heapify(arr, n, i, metricas):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        metricas.comparacoes += 1
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        metricas.comparacoes += 1
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        metricas.trocas += 1
        heapify(arr, n, largest, metricas)

def heapSort(arr, metricas):
    n = len(arr)
    metricas.memoriaUsada += n * 4  # Considerando 4 bytes por int

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, metricas)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        metricas.trocas += 1
        heapify(arr, i, 0, metricas)


def carregarVetor(tamanho, caso, caminhoVetor):
    with open(caminhoVetor, 'r') as f:
        lines = f.readlines()
        key = f"{tamanho} {caso}:"
        for i in range(len(lines)):
            if lines[i].strip() == key:
                vetor = list(map(int, lines[i + 1].strip().split()))
                return vetor
    return []

# Função principal
def main(tamanho, caso, caminhoVetor):
    locale.setlocale(locale.LC_ALL, "Portuguese")

    metricas = Metricas()
    arr = carregarVetor(tamanho, caso, caminhoVetor)
    
    inicio = time.time()
    heapSort(arr, metricas)
    fim = time.time()
    metricas.tempoExecucao = fim - inicio

    # Retornar métricas como dicionário
    return {
        "Comparacoes": metricas.comparacoes,
        "Trocas": metricas.trocas,
        "Tempo de execucao": metricas.tempoExecucao,
        "Memoria usada": metricas.memoriaUsada
    }

if __name__ == "__main__":
    main()
