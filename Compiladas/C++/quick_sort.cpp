#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <ctime>
#include <chrono>

struct Metricas {
    int comparacoes = 0;
    int trocas = 0;
    double tempoExecucao = 0.0; // Em segundos
    int memoriaUsada = 0;    // Em bytes
};

void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

// Função para escolher a mediana de três como pivot
int medianaDeTres(std::vector<int>& arr, int low, int high) {
    int mid = low + (high - low) / 2;
    if (arr[low] > arr[mid])
        std::swap(arr[low], arr[mid]);
    if (arr[low] > arr[high])
        std::swap(arr[low], arr[high]);
    if (arr[mid] > arr[high])
        std::swap(arr[mid], arr[high]);
    std::swap(arr[mid], arr[high]); // Coloca o pivot no final
    return arr[high];
}

int partition(std::vector<int>& arr, int low, int high, Metricas& metricas) {
    int pivot = medianaDeTres(arr, low, high);
    int i = low - 1;
    metricas.memoriaUsada += sizeof(int); // Considera o espaço ocupado pelo pivot

    for (int j = low; j <= high - 1; j++) {
        metricas.comparacoes++;
        if (arr[j] < pivot) {
            i++;
            metricas.trocas++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    metricas.trocas++;
    return (i + 1);
}

void quickSort(std::vector<int>& arr, int low, int high, Metricas& metricas) {
    metricas.comparacoes++;
    if (low < high) {
        int pi = partition(arr, low, high, metricas);
        quickSort(arr, low, pi - 1, metricas);
        quickSort(arr, pi + 1, high, metricas);
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
        std::cerr << "Uso: ./quick_sort <tamanho do vetor> <caso>\n";
        return 1;
    }
    int tamanho = std::stoi(argv[1]);
    std::string caso = argv[2];

    Metricas metricas;
    std::vector<int> arr = loadArray(tamanho, caso);

    auto inicio = std::chrono::high_resolution_clock::now();
    quickSort(arr, 0, tamanho - 1, metricas);
    auto fim = std::chrono::high_resolution_clock::now();
    metricas.tempoExecucao = std::chrono::duration<double>(fim - inicio).count();
    std::cout << "Comparacoes: " << metricas.comparacoes << std::endl;
    std::cout << "Trocas: " << metricas.trocas << std::endl;
    std::cout << "Tempo de execucao: " << metricas.tempoExecucao << std::endl;
    std::cout << "Memoria usada: " << metricas.memoriaUsada << std::endl;

    return 0;
}
