import matplotlib.pyplot as plt
import seaborn as sns
import subprocess
import os.path
import execjs
import numpy as np

CAMINHO_VETOR = 'D:/Documentos/cefet/AEDS/Trabalho_3/vetores/vetores_input_3.txt'
CAMINHO_GRAFICOS = 'D:/Documentos/cefet/AEDS/Trabalho_3/Graficos'
# Função para rodar um algoritmo de ordenação Python
def run_sort_algorithm_js(module_name, size, option):
    result = subprocess.run(["node", module_name, str(size), str(option), CAMINHO_VETOR], capture_output=True, text=True)
    metrics = result.stdout
    return metrics

# Função para rodar o algoritmo Merge Sort
def run_merge_sort_py(size, option):
    import merge_sort
    return merge_sort.main(size,option, CAMINHO_VETOR)

# Função para rodar o algoritmo Selection Sort
def run_selection_sort_py(size, option ):
    import selection_sort
    return selection_sort.main(size,option, CAMINHO_VETOR)

# Função para rodar o algoritmo Counting Sort
def run_counting_sort_py(size, option ):
    import counting_sort
    return counting_sort.main(size,option, CAMINHO_VETOR)

# Função para rodar o algoritmo Quick Sort
def run_quick_sort_py(size, option ):
    import quick_sort
    return quick_sort.main(size,option, CAMINHO_VETOR)

# Função para rodar o algoritmo Heap Sort
def run_heap_sort_py(size, option ):
    import heap_sort
    return heap_sort.main(size,option, CAMINHO_VETOR)

# Função para rodar o algoritmo Shell Sort
def run_shell_sort_py(size, option ):
    import shell_sort
    return shell_sort.main(size,option, CAMINHO_VETOR)

# Função para rodar o algoritmo Bubble Sort
def run_bubble_sort_py(size, option ):
    import bubble_sort
    return bubble_sort.main(size,option, CAMINHO_VETOR)

# Função para rodar o algoritmo Radix Sort
def run_radix_sort_py(size, option):
    import radix_sort
    return radix_sort.main(size,option, CAMINHO_VETOR)

# Função para parsear as métricas a partir da saída do script
def parse_metrics(output):
    lines = output.split('\n')
    metrics = {}
    for line in lines:
        if "Comparacoes" in line:
            metrics["Comparacoes"] = int((line.split(":")[1].strip()).replace(",",""))
        elif "Trocas" in line:
            metrics["Trocas"] = int(line.split(":")[1].strip().replace(",",""))
        elif "Tempo de execucao" in line:
            metrics["Tempo de execucao"] = float((line.split(":")[1].strip().split()[0]).replace(",","")) 
        elif "Memoria usada" in line:
            metrics["Memoria usada"] = int(line.split(":")[1].strip().split()[0])
    return metrics


# Função para plotar as métricas

    # discutir o grafico de linha em cada linguagem diferente o coiso

def plot_metrics(metrics_dict, linguagem, sizes):
    vector_types = ['aleatorios', 'crescente', 'decrescente']
    algorithms = list(metrics_dict.keys())
    sizes_to_plot = [100, 500, 1000, 1500, 10000]
    metrics_names = ['Comparacoes', 'Trocas', 'Tempo de execucao']
    
    if not os.path.exists(CAMINHO_GRAFICOS+"_metricas"):
        os.makedirs(CAMINHO_GRAFICOS)
    
    for metric in metrics_names:
        for size in sizes_to_plot:
            plt.figure(figsize=(15, 10))
            plt.suptitle(f'Métrica: {metric.capitalize()} para Tamanho de Vetor {size} - {linguagem}', fontsize=16)
            
            # Dados para plotagem
            data = []
            for vector_type in vector_types:
                for algorithm_name in algorithms:
                    valor = metrics_dict[algorithm_name][vector_type][sizes_to_plot.index(size)][metric.capitalize()]
                    data.append((algorithm_name, vector_type, valor))
            
            # Converter para numpy array para facilitar o plot
            data_np = np.array(data, dtype=object)
            algorithm_names = data_np[:, 0]
            vector_labels = data_np[:, 1]
            values = data_np[:, 2].astype(float)
            
            # Ordena os algoritmos pela métrica
            sorted_indices = np.argsort(algorithm_names)
            algorithm_names = algorithm_names[sorted_indices]
            vector_labels = vector_labels[sorted_indices]
            values = values[sorted_indices]
            
            # Cria o gráfico de barras
            for vector_type in vector_types:
                indices = np.where(vector_labels == vector_type)[0]
                plt.bar(algorithm_names[indices], values[indices], label=vector_type.capitalize())
            
            plt.xlabel('Algoritmo de Ordenação')
            plt.ylabel(metric.capitalize())
            plt.title(f'{metric.capitalize()} para Vetores de Tamanho {size}')
            plt.xticks(rotation=45)
            plt.legend(title="Tipo de Vetor")
            plt.grid(True, axis='y', linestyle='--', alpha=0.7)
            
            # Salvar o gráfico
            # output_file = os.path.join(CAMINHO_GRAFICOS+"_metricas", f'{metric.capitalize()}_para_Vetores_de_Tamanho_{size}')
            # plt.savefig(output_file)
        
        # Fechar a figura para liberar memória
        plt.close()

def plot_asymptotic_behavior(metrics_dict, linguagem, sizes):
    vector_types = ['aleatorios', 'crescente', 'decrescente']
    algorithms = list(metrics_dict.keys())

    # Criar o diretório de saída se ele não existir
    if not os.path.exists(CAMINHO_GRAFICOS):
        os.makedirs(CAMINHO_GRAFICOS)
    
    for algorithm_name in algorithms:
        plt.figure(figsize=(10, 6))
        plt.title(f'Curva de Tempo de Execução do Algoritmo {algorithm_name} ({linguagem})', fontsize=16)
        
        for vector_type in vector_types:
            times = []
            for size in sizes:
                tempo_execucao = metrics_dict[algorithm_name][vector_type][sizes.index(size)]['Tempo de execucao']
                
                # Tratamento dos dados para tempos pequenos ou inexistentes
                if tempo_execucao is None or tempo_execucao < 1e-6:
                    tempo_execucao = 0.0
                
                times.append(tempo_execucao)
            
            # Plotando a curva de tempo de execução
            plt.plot(sizes, times, marker='o', label=vector_type.capitalize())
        
        plt.xlabel('Tamanho do Vetor')
        plt.ylabel('Tempo de Execução (s)')
        plt.yscale('log')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend(title="Tipo de Vetor")
        plt.tight_layout()
        plt.show()
        # Salvar o gráfico
        # output_file = os.path.join(CAMINHO_GRAFICOS, f'{algorithm_name}_{linguagem}.png')
        # plt.savefig(output_file)
        
        # Fechar a figura para liberar memória
        plt.close()

def exec_pythons_algorithms(algorithm_name, size, option):
    metrics = {}
    if algorithm_name == "Bubble Sort":
        metrics = run_bubble_sort_py(size, option )
    elif algorithm_name == "Selection Sort":
        metrics = run_selection_sort_py(size, option )
    elif algorithm_name == "Counting Sort":
        metrics = run_counting_sort_py(size, option )
    elif algorithm_name == "Merge Sort":
        metrics = run_merge_sort_py(size,option)
    elif algorithm_name == "Quick Sort":
        metrics = run_quick_sort_py(size, option )
    elif algorithm_name == "Heap Sort":
        metrics = run_heap_sort_py(size, option )
    elif algorithm_name == "Shell Sort":
        metrics = run_shell_sort_py(size, option )
    elif algorithm_name == "Radix Sort":
        metrics = run_radix_sort_py(size, option )
    return metrics

def run_python_comparison(algorithms_py, sizes, options):
    metrics_dict = {}
    for algorithm_name, executable in algorithms_py.items():
        metrics_dict[algorithm_name] = {}
        for option in options:
            metrics_list = []
            for size in sizes:
                print(f"Running {algorithm_name}, with size: {size}")
                metrics_list.append(exec_pythons_algorithms(algorithm_name, size, option))
            metrics_dict[algorithm_name][option] = metrics_list
    # plot_metrics(metrics_dict, "Python", sizes)
    plot_asymptotic_behavior(metrics_dict, "Python", sizes)
    
def run_cpp_comparison(algorithms_cpp, sizes, options):
    metrics_dict = {}
    for algorithm_name, executable in algorithms_cpp.items():
        metrics_dict[algorithm_name] = {}
        for option in options:
            metrics_list = []
            for size in sizes:
                print(f"Running {algorithm_name}, with size: {size}")
                result = subprocess.run([executable, str(size), str(option), str(CAMINHO_VETOR)], capture_output=True, text=True)
                output = result.stdout
                metrics = parse_metrics(output)
                metrics_list.append(metrics)
            metrics_dict[algorithm_name][option] = metrics_list
    # plot_metrics(metrics_dict, "C++", sizes)
    plot_asymptotic_behavior(metrics_dict, "C++", sizes)
    
def run_c_comparison(algorithms_c, sizes, options):
    metrics_dict = {}
    for algorithm_name, executable in algorithms_c.items():
        metrics_dict[algorithm_name] = {}
        for option in options:
            metrics_list = []
            for size in sizes:
                print(f"Running {algorithm_name}, with size: {size}")
                result = subprocess.run([executable, str(size), str(option), str(CAMINHO_VETOR)], capture_output=True, text=True)
                output = result.stdout
                metrics = parse_metrics(output)
                metrics_list.append(metrics)
            metrics_dict[algorithm_name][option] = metrics_list
    # plot_metrics(metrics_dict, "C", sizes)
    plot_asymptotic_behavior(metrics_dict, "C", sizes)

def run_js_comparison(algorithms_js, sizes, options):
    metrics_dict = {}
    myjs = execjs.get()
    for algorithm_name, executable in algorithms_js.items():
        metrics_dict[algorithm_name] = {}
        for option in options:
            metrics_list = []
            for size in sizes:
                print(f"Running {algorithm_name}, with size: {size}")
                metrics = run_sort_algorithm_js(executable,size,option)
                metrics = parse_metrics(metrics)
                metrics_list.append(metrics)
            metrics_dict[algorithm_name][option] = metrics_list
    # plot_metrics(metrics_dict, "Js", sizes)
    plot_asymptotic_behavior(metrics_dict, "Js", sizes)
       
        

# Função principal
if __name__ == "__main__":
    algorithms_py = {
        "Merge Sort": "Interpretadas/Python/merge_sort.py",
        "Counting Sort": "Interpretadas/Python/counting_sort.py",
        "Radix Sort": "Interpretadas/Python/radix_sort.py",
        "Heap Sort": "Interpretadas/Python/heap_sort.py",
        "Shell Sort": "Interpretadas/Python/shell_sort.py",
        "Quick Sort": "Interpretadas/Python/quick_sort.py",
        "Selection Sort": "Interpretadas/Python/selection_sort.py",
        "Bubble Sort": "Interpretadas/Python/bubble_sort.py"
    }
    
    algorithms_c = {
        "Merge Sort": "Compiladas/C/output/merge_sort.exe",
        "Counting Sort": "Compiladas/C/output/counting_sort.exe",
        "Radix Sort": "Compiladas/C/output/radix_sort.exe",
        "Heap Sort": "Compiladas/C/output/heap_sort.exe",
        "Shell Sort": "Compiladas/C/output/shell_sort.exe",
        "Quick Sort": "Compiladas/C/output/quick_sort.exe",
        "Selection Sort": "Compiladas/C/output/selection_sort.exe",
        "Bubble Sort": "Compiladas/C/output/bubble_sort.exe"
    }
    
    algorithms_cpp = {
        "Merge Sort": "Compiladas/C++/output/merge_sort.exe",
        "Counting Sort": "Compiladas/C++/output/counting_sort.exe",
        "Radix Sort": "Compiladas/C++/output/radix_sort.exe",
        "Heap Sort": "Compiladas/C++/output/heap_sort.exe",
        "Shell Sort": "Compiladas/C++/output/shell_sort.exe",
        "Quick Sort": "Compiladas/C++/output/quick_sort.exe",
        "Selection Sort": "Compiladas/C++/output/selection_sort.exe",
        "Bubble Sort": "Compiladas/C++/output/bubble_sort.exe",
    }
    
    algorithms_js = {
        "Merge Sort": "Interpretadas/Javascript/merge_sort.js",
        "Counting Sort": "Interpretadas/Javascript/counting_sort.js",
        "Radix Sort": "Interpretadas/Javascript/radix_sort.js",
        "Heap Sort": "Interpretadas/Javascript/heap_sort.js",
        "Shell Sort": "Interpretadas/Javascript/shell_sort.js",
        "Quick Sort": "Interpretadas/Javascript/quick_sort.js",
        "Selection Sort": "Interpretadas/Javascript/selection_sort.js",
        "Bubble Sort": "Interpretadas/Javascript/bubble_sort.js",
    }


    sizes = range(100, 10000,100)

    options = ["aleatorios","crescente", "decrescente"]

    run_python_comparison(algorithms_py, sizes, options)
    run_js_comparison(algorithms_js,sizes,options)
    run_cpp_comparison(algorithms_cpp,sizes,options)
    run_c_comparison(algorithms_c,sizes,options)