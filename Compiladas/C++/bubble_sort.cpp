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

void bubbleSort(std::vector<int>& arr, Metricas& metricas) {
    int n = arr.size();
    metricas.memoriaUsada += n * sizeof(int);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                metricas.comparacoes++;
                std::swap(arr[j], arr[j + 1]);
                metricas.trocas++;
            }
        }
    }
}

std::vector<int> loadArray(int size, const std::string& caseType) {
    std::ifstream file("D:/Documentos/cefet/AEDS/Trabalho_3/vetores/vetores_input_2.txt");
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
        std::cerr << "Uso: ./bubble_sort <tamanho do vetor> <caso>\n";
        return 1;
    }
    int tamanho = std::stoi(argv[1]);
    std::string caso = argv[2];

    Metricas metricas;
    std::vector<int> arr = loadArray(tamanho, caso);

    auto inicio = std::chrono::high_resolution_clock::now();
    bubbleSort(arr, metricas);
    auto fim = std::chrono::high_resolution_clock::now();
    metricas.tempoExecucao = std::chrono::duration<double>(fim - inicio).count();
    std::cout << "Comparacoes: " << metricas.comparacoes << std::endl;
    std::cout << "Trocas: " << metricas.trocas << std::endl;
    std::cout << "Tempo de execucao: " << metricas.tempoExecucao << std::endl;
    std::cout << "Memoria usada: " << metricas.memoriaUsada << std::endl;

    return 0;
}
