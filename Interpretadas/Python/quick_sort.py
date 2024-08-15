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

def mediana_de_tres(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    # Coloca o pivot (mediana) no final
    arr[mid], arr[high] = arr[high], arr[mid]
    return arr[high]

# Implementação do Quick Sort com mediana de três
def partition(arr, low, high, metricas):
    pivot = mediana_de_tres(arr, low, high)
    metricas.memoriaUsada += 4  # Considerando 4 bytes por int para o pivot
    i = low - 1

    for j in range(low, high):
        metricas.comparacoes += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            metricas.trocas += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    metricas.trocas += 1
    return i + 1

def quickSort(arr, low, high, metricas):
    if low < high:
        pi = partition(arr, low, high, metricas)
        quickSort(arr, low, pi - 1, metricas)
        quickSort(arr, pi + 1, high, metricas)


def carregarVetor(tamanho, caso):
    with open('vetores/vetores_input.txt', 'r') as f:
        lines = f.readlines()
        key = f"{tamanho} {caso}:"
        for i in range(len(lines)):
            if lines[i].strip() == key:
                vetor = list(map(int, lines[i + 1].strip().split()))
                return vetor
    return []

# Função principal
def main(tamanho, caso):
    locale.setlocale(locale.LC_ALL, "Portuguese")

    metricas = Metricas()
    arr = carregarVetor(tamanho, caso)
    
    inicio = time.time()
    quickSort(arr,0,tamanho-1, metricas)
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
