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

# Implementação do Bubble Sort
def bubbleSort(arr, metricas):
    n = len(arr)
    metricas.memoriaUsada += n * 4  # Considerando 4 bytes por int
    for i in range(n):
        for j in range(0, n-i-1):
            metricas.comparacoes += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                metricas.trocas += 1

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

    metricas = Metricas()
    arr = carregarVetor(tamanho, caso)
    inicio = time.time()
    bubbleSort(arr, metricas)
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
    main(1000,"aleatorios")
