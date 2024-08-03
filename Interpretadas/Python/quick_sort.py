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

# Implementação do Quick Sort
def partition(arr, low, high, metricas):
    i = low - 1
    pivot = arr[high]
    metricas.memoriaUsada += 4  # Considerando 4 bytes por int para o pivot

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

# Função para gerar um vetor de acordo com a opção fornecida
def gerarVetor(N, opcao, repeticao):
    locale.setlocale(locale.LC_ALL, "Portuguese")
    vetor = [0] * N

    if opcao == 0:  # Vetor aleatório
        if repeticao == 1:
            for i in range(N):
                vetor[i] = random.randint(0, N - 1)  # Valores aleatórios entre 0 e N-1
        else:
            temp = list(range(N))
            for i in range(N):
                j = random.randint(0, N - i - 1)
                vetor[i] = temp[j]
                temp[j] = temp[N - i - 1]
    elif opcao == 1:  # Vetor crescente
        for i in range(N):
            vetor[i] = i
    elif opcao == 2:  # Vetor decrescente
        for i in range(N):
            vetor[i] = N - i
    else:
        print("Opção inválida")
        exit(1)

    return vetor

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

    # N = 100000  # Tamanho do vetor
    # opcao = 0  # 0 para aleatório, 1 para crescente, 2 para decrescente
    # repeticao = 1  # 0 para sem repetição, 1 para com repetição

    # # Testando Quick Sort
    # metricas = Metricas()
    # arr_quick = gerarVetor(N, opcao, repeticao)
    # inicio = time.time()
    # quickSort(arr_quick, 0, N - 1, metricas)
    # fim = time.time()
    # metricas.tempoExecucao = fim - inicio
    
    if len(sys.argv) != 3:
        print("Uso: python insertion_sort.py <tamanho do vetor> <caso>")
        return

    tamanho = int(sys.argv[1])
    caso = sys.argv[2]

    metricas = Metricas()
    arr = carregarVetor(tamanho, caso)
    
    inicio = time.time()
    quickSort(arr,0,tamanho -1, metricas)
    fim = time.time()
    metricas.tempoExecucao = fim - inicio

    print("\nMétricas Quick Sort: ")
    print(f"Comparações: {metricas.comparacoes}")
    print(f"Trocas: {metricas.trocas}")
    print(f"Tempo de execução: {metricas.tempoExecucao} segundos")
    print(f"Memória usada: {metricas.memoriaUsada} bytes")

if __name__ == "__main__":
    main()
