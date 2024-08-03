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

    # # Testando Shell Sort
    # metricas = Metricas()
    # arr_shell = gerarVetor(N, opcao, repeticao)
    # inicio = time.time()
    # shellSort(arr_shell, metricas)
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
    shellSort(arr, metricas)
    fim = time.time()
    metricas.tempoExecucao = fim - inicio

    print("\nMétricas Shell Sort: ")
    print(f"Comparações: {metricas.comparacoes}")
    print(f"Trocas: {metricas.trocas}")
    print(f"Tempo de execução: {metricas.tempoExecucao} segundos")
    print(f"Memória usada: {metricas.memoriaUsada} bytes")

if __name__ == "__main__":
    main()
