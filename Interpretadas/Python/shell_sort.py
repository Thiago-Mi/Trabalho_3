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

# Implementação do Shell Sort
def shellSort(arr, metricas):
    n = len(arr)
    gap = n // 2
    metricas.memoriaUsada += n * 4  # Considerando 4 bytes por int

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                metricas.comparacoes += 1
                arr[j] = arr[j - gap]
                j -= gap
                metricas.trocas += 1
            arr[j] = temp
        gap //= 2


def carregarVetor(tamanho, caso):
    with open('vetores/vetores_input_2.txt', 'r') as f:
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

    # N = 100000  # Tamanho do vetor
    # opcao = 0  # 0 para aleatório, 1 para crescente, 2 para decrescente
    # repeticao = 1  # 0 para sem repetição, 1 para com repetição

    # # Testando Shell Sort
    # metricas = Metricas()
    # arr_shell = (N, opcao, repeticao)
    # inicio = time.time()
    # shellSort(arr_shell, metricas)
    # fim = time.time()
    # metricas.tempoExecucao = fim - inicio
    

    

    metricas = Metricas()
    arr = carregarVetor(tamanho, caso)
    
    inicio = time.time()
    shellSort(arr, metricas)
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
