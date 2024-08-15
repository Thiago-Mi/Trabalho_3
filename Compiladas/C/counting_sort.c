#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
    int comparacoes;
    int trocas;
    double tempoExecucao;
    int memoriaUsada;
} Metricas;

void countingSort(int arr[], int n, Metricas* metricas) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    int* count = (int*)calloc(max + 1, sizeof(int));
    int* output = (int*)malloc(n * sizeof(int));
    metricas->memoriaUsada = (max + 1) * sizeof(int) + n * sizeof(int);

    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    for (int i = 1; i <= max; i++) {
        count[i] += count[i - 1];
    }

    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
        metricas->trocas++;
    }

    free(count);
    free(output);
}

int main() {
    int arr[] = {4, 2, 2, 8, 3, 3, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    Metricas metricas = {0, 0, 0.0, 0};
    clock_t inicio = clock();
    countingSort(arr, n, &metricas);
    clock_t fim = clock();
    metricas.tempoExecucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;

    printf("Sorted array: \n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    printf("\nComparacoes: %d\nTrocas: %d\nTempo de execucao: %lf segundos\nMemoria usada: %d bytes\n",
           metricas.comparacoes, metricas.trocas, metricas.tempoExecucao, metricas.memoriaUsada);

    return 0;
}
