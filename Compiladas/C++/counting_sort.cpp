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

void countingSort(std::vector<int>& arr, Metricas& metricas) {
    int max = *std::max_element(arr.begin(), arr.end());

    std::vector<int> count(max + 1, 0);
    std::vector<int> output(arr.size());

    metricas.memoriaUsada = (max + 1) * sizeof(int) + arr.size() * sizeof(int);

    for (int i = 0; i < arr.size(); i++) {
        count[arr[i]]++;
    }

    for (int i = 1; i <= max; i++) {
        count[i] += count[i - 1];
    }

    for (int i = arr.size() - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
        metricas.trocas++;
    }

    for (int i = 0; i < arr.size(); i++) {
        arr[i] = output[i];
    }
}

std::vector<int> loadArray(int size, const std::string& caseType, std::string caminhoVetor) {
    std::ifstream file(caminhoVetor);
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
    if (argc != 4) {
        std::cerr << "Uso: ./counting_sort <tamanho do vetor> <caso>\n";
        return 1;
    }

    int tamanho = std::stoi(argv[1]);
    std::string caso = argv[2];
    std::string caminhoVetor = argv[3];

    Metricas metricas;
    std::vector<int> arr = loadArray(tamanho, caso, caminhoVetor);

    auto start = std::chrono::high_resolution_clock::now();
    countingSort(arr, metricas);
    auto end = std::chrono::high_resolution_clock::now();

    metricas.tempoExecucao = std::chrono::duration<double>(end - start).count();

    std::cout << "Comparacoes: " << metricas.comparacoes << std::endl;
    std::cout << "Trocas: " << metricas.trocas << std::endl;
    std::cout << "Tempo de execucao: " << metricas.tempoExecucao << std::endl;
    std::cout << "Memoria usada: " << metricas.memoriaUsada << std::endl;

    return 0;
}
