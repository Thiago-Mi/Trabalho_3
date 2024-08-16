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
    n1 = m - l
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
            metricas.trocas +=1
            arr[k] = L[i]
            i += 1
        else:
            metricas.trocas +=1
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar os elementos restantes de L[], se houver
    while i < n1:
        metricas.trocas +=1
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar os elementos restantes de R[], se houver
    while j < n2:
        metricas.trocas +=1
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
    mergeSort(arr, 0, tamanho -1, metricas)
    fim = time.time()

    metricas.tempoExecucao = fim - inicio
    # Retornar métricas como dicionário
    return {
        "Comparacoes": metricas.comparacoes,
        "Trocas": metricas.trocas,
        "Tempo de execucao": metricas.tempoExecucao,
        "Memoria usada": metricas.memoriaUsada
    }


