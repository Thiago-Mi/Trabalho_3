#include <stdio.h>
#include <time.h>

typedef struct {
    int comparacoes;
    int trocas;
    double tempoExecucao;
} Metricas;

void swap(int* a, int* b, Metricas* metricas) {
    int t = *a;
    *a = *b;
    *b = t;
    metricas->trocas++;
}

void heapify(int arr[], int n, int i, Metricas* metricas) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    metricas->comparacoes++;
    if (left < n && arr[left] > arr[largest])
        largest = left;

    metricas->comparacoes++;
    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(&arr[i], &arr[largest], metricas);
        heapify(arr, n, largest, metricas);
    }
}

void heapSort(int arr[], int n, Metricas* metricas) {
    clock_t inicio = clock();

    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i, metricas);

    for (int i = n - 1; i > 0; i--) {
        swap(&arr[0], &arr[i], metricas);
        heapify(arr, i, 0, metricas);
    }

    clock_t fim = clock();
    metricas->tempoExecucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
}

int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    Metricas metricas = {0, 0, 0.0};
    heapSort(arr, n, &metricas);

    printf("Sorted array: \n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    printf("\nComparacoes: %d\nTrocas: %d\nTempo de execucao: %lf segundos\n", metricas.comparacoes, metricas.trocas, metricas.tempoExecucao);
    return 0;
}
