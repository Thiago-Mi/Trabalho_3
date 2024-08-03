import subprocess
import matplotlib.pyplot as plt

# Função para rodar um algoritmo de ordenação Python
def run_sort_algorithm(executable, size, option, repetition):
    result = subprocess.run(["python3", executable, str(size), str(option), str(repetition)], capture_output=True, text=True)
    output = result.stdout
    metrics = parse_metrics(output)
    return metrics

# Função para rodar o algoritmo Merge Sort
def run_merge_sort(executable,size,option,repetition):
    return run_sort_algorithm(executable, size, option, repetition)

# Função para rodar o algoritmo Selection Sort
def run_selection_sort(executable, size, option, repetition):
    return run_sort_algorithm(executable, size, option, repetition)

# Função para rodar o algoritmo Counting Sort
def run_counting_sort(executable, size, option, repetition):
    return run_sort_algorithm(executable, size, option, repetition)

# Função para rodar o algoritmo Quick Sort
def run_quick_sort(executable, size, option, repetition):
    return run_sort_algorithm(executable, size, option, repetition)

# Função para rodar o algoritmo Heap Sort
def run_heap_sort(executable, size, option, repetition):
    return run_sort_algorithm(executable, size, option, repetition)

# Função para rodar o algoritmo Shell Sort
def run_shell_sort(executable, size, option, repetition):
    return run_sort_algorithm(executable, size, option, repetition)

# Função para rodar o algoritmo Bubble Sort
def run_bubble_sort(executable, size, option, repetition):
    return run_sort_algorithm(executable, size, option, repetition)

# Função para rodar o algoritmo Radix Sort
def run_radix_sort(executable, size, option, repetition):
    return run_sort_algorithm(executable, size, option, repetition)

# Função para parsear as métricas a partir da saída do script
def parse_metrics(output):
    lines = output.split('\n')
    metrics = {}
    for line in lines:
        if "Comparacoes" in line:
            metrics["Comparacoes"] = int(line.split(":")[1].strip())
        elif "Trocas" in line:
            metrics["Trocas"] = int(line.split(":")[1].strip())
        elif "Tempo de execucao" in line:
            metrics["Tempo de execucao"] = float((line.split(":")[1].strip().split()[0]).replace(",",".")) 
        elif "Memoria usada" in line:
            metrics["Memoria usada"] = int(line.split(":")[1].strip().split()[0])
    return metrics

# Função para plotar as métricas
def plot_metrics(metrics_list, algorithm_names):
    labels = [f"Run {i+1}" for i in range(len(metrics_list))]
    comparacoes = [metrics["Comparacoes"] for metrics in metrics_list]
    trocas = [metrics["Trocas"] for metrics in metrics_list]
    tempo_execucao = [metrics["Tempo de execucao"] for metrics in metrics_list]
    memoria_usada = [metrics["Memoria usada"] for metrics in metrics_list]

    x = range(len(metrics_list))

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.bar(x, comparacoes, tick_label=labels)
    plt.xlabel('Execucao')
    plt.ylabel('Comparacoes')
    plt.title(f'Comparacoes por Execucao - {algorithm_names}')

    plt.subplot(2, 2, 2)
    plt.bar(x, trocas, tick_label=labels)
    plt.xlabel('Execucao')
    plt.ylabel('Trocas')
    plt.title(f'Trocas por Execucao - {algorithm_names}')

    plt.subplot(2, 2, 3)
    plt.bar(x, tempo_execucao, tick_label=labels)
    plt.xlabel('Execucao')
    plt.ylabel('Tempo de Execucao (s)')
    plt.title(f'Tempo de Execucao por Execucao - {algorithm_names}')

    plt.subplot(2, 2, 4)
    plt.bar(x, memoria_usada, tick_label=labels)
    plt.xlabel('Execucao')
    plt.ylabel('Memoria Usada (bytes)')
    plt.title(f'Memoria Usada por Execucao - {algorithm_names}')

    plt.tight_layout()
    plt.show()

def exec_pythons_algorithms(algorithms_py, sizes, option, repetition):
    for algorithm_name, executable in algorithms_py.items():
        metrics_list = []
        print(f"Running {algorithm_name}...")

        for size in sizes:
            if algorithm_name == "Bubble Sort":
                metrics = run_bubble_sort(executable, size, option, repetition)
            elif algorithm_name == "Selection Sort":
                metrics = run_selection_sort(executable, size, option, repetition)
            elif algorithm_name == "Counting Sort":
                metrics = run_counting_sort(executable, size, option, repetition)
            elif algorithm_name == "Merge_sort":
                metrics = run_merge_sort(executable,size,option,repetition)
            elif algorithm_name == "Quick Sort":
                metrics = run_quick_sort(executable, size, option, repetition)
            elif algorithm_name == "Heap Sort":
                metrics = run_heap_sort(executable, size, option, repetition)
            elif algorithm_name == "Shell Sort":
                metrics = run_shell_sort(executable, size, option, repetition)
            elif algorithm_name == "Radix Sort":
                metrics = run_radix_sort(executable, size, option, repetition)

            metrics_list.append(metrics)

        plot_metrics(metrics_list, algorithm_name)

# Função principal
if __name__ == "__main__":
    algorithms_py = {
        "Counting Sort": "counting_sort.py",
        "Merge Sort": "merge_sort.py",
        "Bubble Sort": "bubble_sort.py",
        "Selection Sort": "selection_sort.py",
        "Quick Sort": "quick_sort.py",
        "Heap Sort": "heap_sort.py",
        "Shell Sort": "shell_sort.py",
        "Radix Sort": "radix_sort.py"
    }
    
    algorithms_c = {
        "Counting Sort": "counting_sort.c",
        "Merge Sort": "merge_sort.c",
        "Bubble Sort": "bubble_sort.c",
        "Selection Sort": "selection_sort.c",
        "Quick Sort": "quick_sort.c",
        "Heap Sort": "heap_sort.c",
        "Shell Sort": "shell_sort.c",
        "Radix Sort": "radix_sort.c"
    }
    
    algorithms_cpp = {
        "Counting Sort": "counting_sort.cpp",
        "Merge Sort": "merge_sort.cpp",
        "Bubble Sort": "bubble_sort.cpp",
        "Selection Sort": "selection_sort.cpp",
        "Quick Sort": "quick_sort.cpp",
        "Heap Sort": "heap_sort.cpp",
        "Shell Sort": "shell_sort.cpp",
        "Radix Sort": "radix_sort.cpp"
    }

    sizes = [1000, 10000, 100000, 200000, 400000, 800000, 1000000]  # Diferentes tamanhos de entrada para teste
    option = 0  # Opcao para tipo de vetor
    repetition = 1  # Repeticao

    for algorithm_name, executable in algorithms_py.items():
        metrics_list = []
        print(f"Running {algorithm_name}...")

        for size in sizes:
            if algorithm_name == "Bubble Sort":
                metrics = run_bubble_sort(executable, size, option, repetition)
            elif algorithm_name == "Selection Sort":
                metrics = run_selection_sort(executable, size, option, repetition)
            elif algorithm_name == "Counting Sort":
                metrics = run_counting_sort(executable, size, option, repetition)
            elif algorithm_name == "Merge_sort":
                metrics = run_merge_sort(executable,size,option,repetition)
            elif algorithm_name == "Quick Sort":
                metrics = run_quick_sort(executable, size, option, repetition)
            elif algorithm_name == "Heap Sort":
                metrics = run_heap_sort(executable, size, option, repetition)
            elif algorithm_name == "Shell Sort":
                metrics = run_shell_sort(executable, size, option, repetition)
            elif algorithm_name == "Radix Sort":
                metrics = run_radix_sort(executable, size, option, repetition)

            metrics_list.append(metrics)

        plot_metrics(metrics_list, algorithm_name)
