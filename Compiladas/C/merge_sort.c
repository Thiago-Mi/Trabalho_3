#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

// Estrutura para armazenar as metricas
typedef struct {
    int comparacoes;
    int trocas;
    double tempoExecucao;  // Armazena o tempo de execucao em segundos
    size_t memoriaUsada;   // Armazena a quantidade de memoria usada em bytes
} Metricas;

// Funcao para mesclar duas metades do array
void merge(int arr[], int l, int m, int r, Metricas *metricas) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    // Arrays temporarios
    int *L = (int *)malloc(n1 * sizeof(int));
    int *R = (int *)malloc(n2 * sizeof(int));
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

    // Liberar a memoria dos arrays temporarios
    free(L);
    free(R);
}

// Funcao recursiva do Merge Sort
void mergeSort(int arr[], int l, int r, Metricas *metricas) {
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
void printArray(int A[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

// Funcao para gerar um vetor de acordo com a opcao fornecida
int* gerarVetor(int N, int opcao, int repeticao) {
    setlocale(LC_ALL, "Portuguese");
    int *vetor = (int *)malloc(N * sizeof(int));
    if (!vetor) {
        printf("Erro ao alocar memoria\n");
        exit(1);
    }

    if (opcao == 0) { // Vetor aleatorio
        srand(time(NULL));
        if (repeticao == 1) {
            for (int i = 0; i < N; i++) {
                vetor[i] = rand() % N; // Valores aleatorios entre 0 e 99
            }
        } else {
            int temp[N];
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
        printf("Opcao invalida\n");
        free(vetor);
        exit(1);
    }

    return vetor;
}

// Funcao principal
int main() {

    setlocale(LC_ALL, "Portuguese");

    int N = 10000; // Tamanho do vetor
    int opcao = 0; // 0 para aleatorio, 1 para crescente, 2 para decrescente
    int repeticao = 1; // 0 para sem repeticao, 1 para com repeticao
    Metricas metricas = {0, 0, 0.0, 0};

    // Gerar vetor de acordo com a opcao fornecida
    int *arr = gerarVetor(N, opcao, repeticao);

    // Adicionar memoria usada pelo vetor gerado
    metricas.memoriaUsada += N * sizeof(int);

    // printf("Array inicial: \n");
    // printArray(arr, N);

    // Capturar o tempo de início
    clock_t inicio = clock();

    mergeSort(arr, 0, N - 1, &metricas);

    // Capturar o tempo de termino
    clock_t fim = clock();

    // Calcular o tempo de execucao em segundos
    metricas.tempoExecucao = ((double) (fim - inicio)) / CLOCKS_PER_SEC;

    // printf("\nArray ordenado: \n");
    // printArray(arr, N);

    printf("\nMetricas: \n");
    printf("Comparacoes: %d\n", metricas.comparacoes);
    printf("Trocas: %d\n", metricas.trocas);
    printf("Tempo de execucao: %f segundos\n", metricas.tempoExecucao);
    printf("Memoria usada: %zu bytes\n", (unsigned long)metricas.memoriaUsada);


    // Liberar a memoria alocada para o vetor
    free(arr);

    return 0;
}
