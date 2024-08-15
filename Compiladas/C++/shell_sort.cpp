#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <chrono>

struct Metricas {
    int comparacoes = 0;
    int trocas = 0;
    double tempoExecucao = 0.0;
    int memoriaUsada = 0;
};

void shellSort(std::vector<int>& arr, Metricas& metricas) {
    int n = arr.size();
    metricas.memoriaUsada += n * sizeof(int);
    for (int gap = n/2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                metricas.comparacoes++;
                arr[j] = arr[j - gap];
                metricas.trocas++;
            }
            arr[j] = temp;
            metricas.trocas++;
        }
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
    shellSort(arr, metricas);
    auto end = std::chrono::high_resolution_clock::now();

    metricas.tempoExecucao = std::chrono::duration<double>(end - start).count();

    std::cout << "Comparacoes: " << metricas.comparacoes << std::endl;
    std::cout << "Trocas: " << metricas.trocas << std::endl;
    std::cout << "Tempo de execucao: " << metricas.tempoExecucao << std::endl;
    std::cout << "Memoria usada: " << metricas.memoriaUsada << std::endl;
    
    return 0;
}
