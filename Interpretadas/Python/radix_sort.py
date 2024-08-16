import sys
import time
import random
import locale

# Classe para armazenar as métricas
class Metricas:
    def __init__(self):
        self.comparacoes = 0  # Comparacoes não são feitas diretamente no Radix Sort
        self.trocas = 0  # Trocas não são feitas diretamente no Radix Sort
        self.tempoExecucao = 0.0  # Armazena o tempo de execução em segundos
        self.memoriaUsada = 0  # Armazena a quantidade de memória usada em bytes

# Implementação do Counting Sort usado pelo Radix Sort
def countingSortForRadix(arr, exp, metricas):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    metricas.memoriaUsada += (len(count) + len(output)) * 4  # Considerando 4 bytes por int

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(n):
        arr[i] = output[i]

# Implementação do Radix Sort
def radixSort(arr, metricas):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        countingSortForRadix(arr, exp, metricas)
        exp *= 10


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

    # # Testando Radix Sort
    # metricas = Metricas()
    # arr_radix = (N, opcao, repeticao)
    # inicio = time.time()
    # radixSort(arr_radix, metricas)
    # fim = time.time()
    # metricas.tempoExecucao = fim - inicio
    


    

    metricas = Metricas()
    arr = carregarVetor(tamanho, caso)
    
    inicio = time.time()
    radixSort(arr, metricas)
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
