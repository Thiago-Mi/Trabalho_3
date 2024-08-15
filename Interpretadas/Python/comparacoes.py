import subprocess
import matplotlib.pyplot as plt
import importlib.util
import seaborn as sns
import os.path
import execjs

# Função para rodar um algoritmo de ordenação Python
def run_sort_algorithm_py(module_name, size, option):
    result = subprocess.run(["python3", module_name, str(size), str(option)], capture_output=True, text=True)
    metrics = result.stdout
    return metrics

def run_merge_sort_cpp(executable, size, option ):
    result = subprocess.run([executable, str(size), str(option)], capture_output=True, text=True)
    output = result.stdout
    metrics = parse_metrics(output)
    return metrics

# Função para rodar o algoritmo Merge Sort
def run_merge_sort_py(size, option):
    import merge_sort
    return merge_sort.main(size, option)

# Função para rodar o algoritmo Selection Sort
def run_selection_sort_py(size, option ):
    import selection_sort
    return selection_sort.main(size, option )

# Função para rodar o algoritmo Counting Sort
def run_counting_sort_py(size, option ):
    import counting_sort
    return counting_sort.main(size, option )

# Função para rodar o algoritmo Quick Sort
def run_quick_sort_py(size, option ):
    import quick_sort
    return quick_sort.main(size, option )

# Função para rodar o algoritmo Heap Sort
def run_heap_sort_py(size, option ):
    import heap_sort
    return heap_sort.main(size, option )

# Função para rodar o algoritmo Shell Sort
def run_shell_sort_py(size, option ):
    import shell_sort
    return shell_sort.main(size, option )

# Função para rodar o algoritmo Bubble Sort
def run_bubble_sort_py(size, option ):
    import bubble_sort
    return bubble_sort.main(size, option)

# Função para rodar o algoritmo Radix Sort
def run_radix_sort_py(size, option):
    import radix_sort
    return radix_sort.main(size,option)

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
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns

def plot_metrics(metrics_dict):
    metrics = ["Comparacoes", "Trocas", "Tempo de execucao", "Memoria usada"]
    vector_types = ['aleatorios', 'crescente', 'decrescente']  # Replace with actual vector type names
    
    plt.figure(figsize=(20, 45))
    
    plot_number = 1
    
    for option in vector_types:
        for metric_name in metrics:
            plt.subplot(len(vector_types), len(metrics), plot_number)
            
            for algorithm_name, options_metrics in metrics_dict.items():
                if option in options_metrics:
                    metrics_list = options_metrics[option]
                    metric_values = [metrics[metric_name] for metrics in metrics_list]
                    sns.lineplot(x=range(len(metrics_list)), y=metric_values, label=f"{algorithm_name} - {option}")
            
            plt.xlabel('Execução')
            plt.ylabel(metric_name)
            plt.title(f'{metric_name} por Execução ({option})')
            plt.legend()
            plt.grid(True)
            
            plot_number += 1
    
    plt.tight_layout()
    plt.show()




def exec_pythons_algorithms(algorithm_name, size, option):
    metrics = {}
    print(f"Running {algorithm_name}, with size: {size}")
    if algorithm_name == "Bubble Sort":
        metrics = run_bubble_sort_py(size, option )
    elif algorithm_name == "Selection Sort":
        metrics = run_selection_sort_py(size, option )
    elif algorithm_name == "Counting Sort":
        metrics = run_counting_sort_py(size, option )
    elif algorithm_name == "Merge Sort":
        print(size, option)
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

def run_python_comparison(algorithms_py):
    metrics_dict = {}
    for algorithm_name, executable in algorithms_py.items():
        metrics_dict[algorithm_name] = {}
        for option in options:
            metrics_list = []
            for size in sizes:
                print(f"Running {algorithm_name}, with size: {size}")
                metrics_list.append(exec_pythons_algorithms(algorithm_name, size, option))
            metrics_dict[algorithm_name][option] = metrics_list
    plot_metrics(metrics_dict)
    
def run_cpp_comparison(algorithms_cpp, sizes, options):
    metrics_dict = {}
    for algorithm_name, executable in algorithms_cpp.items():
        metrics_dict[algorithm_name] = {}
        for option in options:
            metrics_list = []
            for size in sizes:
                print(f"Running {algorithm_name}, with size: {size}")
                result = subprocess.run([executable, str(size), str(option)], capture_output=True, text=True)
                output = result.stdout
                metrics = parse_metrics(output)
                metrics_list.append(metrics)
            metrics_dict[algorithm_name][option] = metrics_list
    plot_metrics(metrics_dict)
    
def run_c_comparison(algorithms_c, sizes, options):
    metrics_dict = {}
    for algorithm_name, executable in algorithms_c.items():
        metrics_dict[algorithm_name] = {}
        for option in options:
            metrics_list = []
            for size in sizes:
                print(f"Running {algorithm_name}, with size: {size}")
                result = subprocess.run([executable, str(size), str(option)], capture_output=True, text=True)
                output = result.stdout
                metrics = parse_metrics(output)
                metrics_list.append(metrics)
            metrics_dict[algorithm_name][option] = metrics_list
    plot_metrics(metrics_dict)

def run_js_comparison(algorithms_js, sizes, options):
    metrics_dict = {}
    myjs = execjs.get()
    for algorithm_name, executable in algorithms_js.items():
        metrics_dict[algorithm_name] = {}
        for option in options:
            metrics_list = []
            for size in sizes:
                print(f"Running {algorithm_name}, with size: {size}")
                dir = os.path.dirname(executable)
                with open(os.path.join(dir, "merge_sort.js")) as f:
                    jscode = f.read()
                result = myjs.compile(jscode)
                output = result.call("main",size,option)
                metrics = output
                metrics_list.append(metrics)
            metrics_dict[algorithm_name][option] = metrics_list
    plot_metrics(metrics_dict)
                
        

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

    # sizes = [1000, 10000, 100000, 200000, 400000, 800000, 1000000]  # Diferentes tamanhos de entrada para teste
    sizes = [1000,10000,100000,200000]
    # sizes = [1000,10000]
    options = ["aleatorios","crescente", "decrescente"]

    run_js_comparison(algorithms_js,sizes,options)
    run_cpp_comparison(algorithms_cpp,sizes,options)
    run_python_comparison(algorithms_py)