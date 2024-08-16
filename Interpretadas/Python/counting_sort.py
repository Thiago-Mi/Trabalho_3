import sys
import time
import random
import locale

# Classe para armazenar as métricas
class Metricas:
    def __init__(self):
        self.comparacoes = 0  # Comparacoes não são feitas diretamente no Counting Sort
        self.trocas = 0  # Trocas não são feitas diretamente no Counting Sort
        self.tempoExecucao = 0.0  # Armazena o tempo de execução em segundos
        self.memoriaUsada = 0  # Armazena a quantidade de memória usada em bytes

# Implementação do Counting Sort
def countingSort(arr, metricas):
    max_val = max(arr)
    min_val = min(arr)
    metricas.comparacoes += len(arr)*2
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)
    metricas.memoriaUsada += (len(count) + len(output)) * 4  # Considerando 4 bytes por int

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


def carregarVetor(tamanho, caso, caminhoVetor):
    with open(caminhoVetor, 'r') as f:
        lines = f.readlines()
        key = f"{tamanho} {caso}:"
        for i in range(len(lines)):
            if lines[i].strip() == key:
                vetor = list(map(int, lines[i + 1].strip().split()))
                return vetor
    return []

def main(tamanho, caso, caminhoVetor):
    locale.setlocale(locale.LC_ALL, "Portuguese")

    metricas = Metricas()
    arr = carregarVetor(tamanho, caso, caminhoVetor)
    
    inicio = time.time()
    countingSort(arr, metricas)
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
