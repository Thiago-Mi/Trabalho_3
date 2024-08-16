#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

typedef struct {
    int comparacoes;
    int trocas;
    double tempoExecucao;
    int memoriaUsada;
} Metricas;

void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int medianaDeTres(int arr[], int low, int high) {
    int mid = low + (high - low) / 2;
    if (arr[low] > arr[mid])
        swap(&arr[low], &arr[mid]);
    if (arr[low] > arr[high])
        swap(&arr[low], &arr[high]);
    if (arr[mid] > arr[high])
        swap(&arr[mid], &arr[high]);
    swap(&arr[mid], &arr[high]); // Coloca o pivot no final
    return arr[high];
}

int partition(int arr[], int low, int high, Metricas* metricas) {
    int pivot = medianaDeTres(arr, low, high);
    int i = low - 1;
    metricas->memoriaUsada += sizeof(int); // Considera o espaço ocupado pelo pivot

    for (int j = low; j <= high - 1; j++) {
        metricas->comparacoes++;
        if (arr[j] < pivot) {
            i++;
            metricas->trocas++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    metricas->trocas++;
    return (i + 1);
}

void quickSort(int arr[], int low, int high, Metricas* metricas) {
    metricas->comparacoes++;
    if (low < high) {
        int pi = partition(arr, low, high, metricas);
        quickSort(arr, low, pi - 1, metricas);
        quickSort(arr, pi + 1, high, metricas);
    }
}

void loadArray(int arr[], int size, const char* caseType) {
    FILE* file = fopen("D:/Documentos/cefet/AEDS/Trabalho_3/vetores/vetores_input.txt", "r");
    if (file == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        exit(1);
    }
    
    char key[20];
    snprintf(key, sizeof(key), "%d %s:", size, caseType);
    
    char line[256];
    while (fgets(line, sizeof(line), file)) {
        if (strncmp(line, key, strlen(key)) == 0) {
            for (int i = 0; i < size; ++i)
                fscanf(file, "%d", &arr[i]);
            break;
        }
    }
    fclose(file);
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        printf("Uso: ./quick_sort <tamanho do vetor> <caso>\n");
        return 1;
    }
    int tamanho = atoi(argv[1]);
    char* caso = argv[2];

    Metricas metricas = {0, 0, 0.0, 0};
    int* arr = (int*)malloc(tamanho * sizeof(int));
    if (arr == NULL) {
        printf("Erro ao alocar memória.\n");
        return 1;
    }

    loadArray(arr, tamanho, caso);

    clock_t inicio = clock();
    quickSort(arr, 0, tamanho - 1, &metricas);
    clock_t fim = clock();
    metricas.tempoExecucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;

    printf("Comparacoes: %d\n", metricas.comparacoes);
    printf("Trocas: %d\n", metricas.trocas);
    printf("Tempo de execucao: %lf\n", metricas.tempoExecucao);
    printf("Memoria usada: %d\n", metricas.memoriaUsada);

    free(arr);
    return 0;
}
