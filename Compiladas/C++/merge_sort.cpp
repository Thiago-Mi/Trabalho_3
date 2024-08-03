#include <iostream>
#include <cstdlib>
#include <ctime>
#include <locale>
#include <vector>

// Estrutura para armazenar as metricas
struct Metricas {
    int comparacoes;
    int trocas;
    double tempoExecucao;  // Armazena o tempo de execucao em segundos
    size_t memoriaUsada;   // Armazena a quantidade de memoria usada em bytes
};

// Funcao para mesclar duas metades do array
void merge(std::vector<int>& arr, int l, int m, int r, Metricas* metricas) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    // Arrays temporarios
    std::vector<int> L(n1);
    std::vector<int> R(n2);
    metricas->memoriaUsada += (n1 + n2) * sizeof(int);

    // Copiar dados para arrays temporarios L[] e R[]
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Mesclar os arrays temporarios de volta em arr[l..r]
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        metricas->comparacoes++;
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copiar os elementos restantes de L[], se houver
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copiar os elementos restantes de R[], se houver
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Funcao recursiva do Merge Sort
void mergeSort(std::vector<int>& arr, int l, int r, Metricas* metricas) {
    if (l < r) {
        int m = l + (r - l) / 2;

        // Ordenar a primeira e a segunda metade
        mergeSort(arr, l, m, metricas);
        mergeSort(arr, m + 1, r, metricas);

        // Mesclar as metades ordenadas
        merge(arr, l, m, r, metricas);
    }
}

// Funcao para imprimir um array
void printArray(const std::vector<int>& A) {
    for (int i = 0; i < A.size(); i++)
        std::cout << A[i] << " ";
    std::cout << std::endl;
}

// Funcao para gerar um vetor de acordo com a opcao fornecida
std::vector<int> gerarVetor(int N, int opcao, int repeticao) {
    std::vector<int> vetor(N);

    if (opcao == 0) { // Vetor aleatorio
        srand(time(NULL));
        if (repeticao == 1) {
            for (int i = 0; i < N; i++) {
                vetor[i] = rand() % N; // Valores aleatorios entre 0 e N-1
            }
        } else {
            std::vector<int> temp(N);
            for (int i = 0; i < N; i++) {
                temp[i] = i;
            }
            for (int i = 0; i < N; i++) {
                int j = rand() % (N - i);
                vetor[i] = temp[j];
                temp[j] = temp[N - i - 1];
            }
        }
    } else if (opcao == 1) { // Vetor crescente
        for (int i = 0; i < N; i++) {
            vetor[i] = i;
        }
    } else if (opcao == 2) { // Vetor decrescente
        for (int i = 0; i < N; i++) {
            vetor[i] = N - i;
        }
    } else {
        std::cerr << "Opcao invalida" << std::endl;
        exit(1);
    }

    return vetor;
}

// Funcao principal
int main() {
    int N = 10000; // Tamanho do vetor
    int opcao = 0; // 0 para aleatorio, 1 para crescente, 2 para decrescente
    int repeticao = 1; // 0 para sem repeticao, 1 para com repeticao
    Metricas metricas = {0, 0, 0.0, 0};

    // Gerar vetor de acordo com a opcao fornecida
    std::vector<int> arr = gerarVetor(N, opcao, repeticao);

    // Adicionar memoria usada pelo vetor gerado
    metricas.memoriaUsada += N * sizeof(int);

    // std::cout << "Array inicial: " << std::endl;
    // printArray(arr);

    // Capturar o tempo de início
    clock_t inicio = clock();

    mergeSort(arr, 0, N - 1, &metricas);

    // Capturar o tempo de termino
    clock_t fim = clock();

    // Calcular o tempo de execucao em segundos
    metricas.tempoExecucao = static_cast<double>(fim - inicio) / CLOCKS_PER_SEC;

    // std::cout << "\nArray ordenado: " << std::endl;
    // printArray(arr);

    std::cout << "\nMetricas: " << std::endl;
    std::cout << "Comparacoes: " << metricas.comparacoes << std::endl;
    std::cout << "Trocas: " << metricas.trocas << std::endl;
    std::cout << "Tempo de execucao: " << metricas.tempoExecucao << " segundos" << std::endl;
    std::cout << "Memoria usada: " << metricas.memoriaUsada << " bytes" << std::endl;

    return 0;
}
