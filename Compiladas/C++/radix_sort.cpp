#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <ctime>
#include <algorithm>
#include <chrono>

struct Metricas {
    int comparacoes = 0; // Comparacoes não são feitas diretamente no Radix Sort
    int trocas = 0;      // Trocas não são feitas diretamente no Radix Sort
    double tempoExecucao = 0.0; // Em segundos
    int memoriaUsada = 0;    // Em bytes
};

void countingSortForRadix(std::vector<int>& arr, int exp, Metricas& metricas) {
    int n = arr.size();
    std::vector<int> output(n);
    int count[10] = {0};

    metricas.memoriaUsada += (sizeof(count) + n * sizeof(int));

    for (int i = 0; i < n; i++) {
        int index = (arr[i] / exp) % 10;
        count[index]++;
    }

    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    for (int i = n - 1; i >= 0; i--) {
        int index = (arr[i] / exp) % 10;
        output[count[index] - 1] = arr[i];
        count[index]--;
    }

    for (int i = 0; i < n; i++) {
        metricas.trocas += 1;
        arr[i] = output[i];
    }
}

void radixSort(std::vector<int>& arr, Metricas& metricas) {
    int max_val = *std::max_element(arr.begin(), arr.end());
    for (int exp = 1; max_val / exp > 0; exp *= 10) {
        countingSortForRadix(arr, exp, metricas);
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
        std::cerr << "Uso: ./radix_sort <tamanho do vetor> <caso>\n";
        return 1;
    }
    int tamanho = std::stoi(argv[1]);
    std::string caso = argv[2];

    Metricas metricas;
    std::vector<int> arr = loadArray(tamanho, caso);

    auto start = std::chrono::high_resolution_clock::now();
    radixSort(arr, metricas);
    auto end = std::chrono::high_resolution_clock::now();
    metricas.tempoExecucao = std::chrono::duration<double>(end - start).count();

    std::cout << "Comparacoes: " << metricas.comparacoes << std::endl;
    std::cout << "Trocas: " << metricas.trocas << std::endl;
    std::cout << "Tempo de execucao: " << metricas.tempoExecucao << std::endl;
    std::cout << "Memoria usada: " << metricas.memoriaUsada << std::endl;

    return 0;
}
