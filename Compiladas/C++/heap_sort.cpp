#include <iostream>
#include <vector>
#include <chrono>
#include <fstream>

struct Metricas {
    int comparacoes = 0;
    int trocas = 0;
    double tempoExecucao = 0.0;
    int memoriaUsada = 0;
};

void swap(int& a, int& b, Metricas& metricas) {
    int t = a;
    a = b;
    b = t;
    metricas.trocas++;
}

void heapify(std::vector<int>& arr, int n, int i, Metricas& metricas) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    metricas.memoriaUsada += largest*sizeof(int) + left * sizeof(int) + right*sizeof(int);
    metricas.comparacoes++;
    if (left < n && arr[left] > arr[largest])
        largest = left;

    metricas.comparacoes++;
    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(arr[i], arr[largest], metricas);
        heapify(arr, n, largest, metricas);
    }
}

void heapSort(std::vector<int>& arr, Metricas& metricas) {
    int n = arr.size();
    metricas.memoriaUsada += n*sizeof(int);
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i, metricas);

    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i], metricas);
        heapify(arr, i, 0, metricas);
    }

}

std::vector<int> loadArray(int size, const std::string& caseType) {
    std::ifstream file("D:/Documentos/cefet/AEDS/Trabalho_3/vetores/vetores_input.txt");
    std::vector<int> arr(size);
    std::string key = std::to_string(size) + " " + caseType + ":";
    std::string line;

    while (std::getline(file, line)) {
        if (line == key) {
            for (int i = 0; i < size; ++i)
                file >> arr[i];
            break;
        }
    }
    return arr;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Uso: ./merge_sort <tamanho do vetor> <caso>\n";
        return 1;
    }

    int tamanho = std::stoi(argv[1]);
    std::string caso = argv[2];

    Metricas metricas;
    std::vector<int> arr = loadArray(tamanho, caso);

    auto start = std::chrono::high_resolution_clock::now();
    heapSort(arr, metricas);
    auto end = std::chrono::high_resolution_clock::now();

    metricas.tempoExecucao = std::chrono::duration<double>(end - start).count();

    std::cout << "Comparacoes: " << metricas.comparacoes << std::endl;
    std::cout << "Trocas: " << metricas.trocas << std::endl;
    std::cout << "Tempo de execucao: " << metricas.tempoExecucao << std::endl;
    std::cout << "Memoria usada: " << metricas.memoriaUsada << std::endl;
    
    return 0;
}
