#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

struct Metricas {
    int comparacoes = 0;
    int trocas = 0;
    double tempoExecucao = 0.0;
    int memoriaUsada = 0;
};

void merge(std::vector<int>& arr, int l, int m, int r, Metricas& metricas) {
    int n1 = m - l + 1;
    int n2 = r - m;

    std::vector<int> L(n1), R(n2);
    metricas.memoriaUsada += (n1 + n2) * sizeof(int);

    for (int i = 0; i < n1; ++i)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; ++j)
        R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        metricas.comparacoes++;
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(std::vector<int>& arr, int l, int r, Metricas& metricas) {
    if (l < r) {
        int m = l + (r - l) / 2;

        mergeSort(arr, l, m, metricas);
        mergeSort(arr, m + 1, r, metricas);

        merge(arr, l, m, r, metricas);
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
        std::cerr << "Uso: ./merge_sort <tamanho do vetor> <caso>\n";
        return 1;
    }

    int tamanho = std::stoi(argv[1]);
    std::string caso = argv[2];

    Metricas metricas;
    std::vector<int> arr = loadArray(tamanho, caso);

    auto start = std::chrono::high_resolution_clock::now();
    mergeSort(arr, 0, tamanho - 1, metricas);
    auto end = std::chrono::high_resolution_clock::now();

    metricas.tempoExecucao = std::chrono::duration<double>(end - start).count();

    std::cout << "Comparacoes: " << metricas.comparacoes << std::endl;
    std::cout << "Trocas: " << metricas.trocas << std::endl;
    std::cout << "Tempo de execucao: " << metricas.tempoExecucao << std::endl;
    std::cout << "Memoria usada: " << metricas.memoriaUsada << std::endl;

    return 0;
}
