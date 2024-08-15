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

// Função para escolher a mediana de três como pivot
int medianaDeTres(int arr[], int low, int high) {
    int mid = low + (high - low) / 2;
    if (arr[low] > arr[mid])
        swap(&arr[low], &arr[mid], NULL);
    if (arr[low] > arr[high])
        swap(&arr[low], &arr[high], NULL);
    if (arr[mid] > arr[high])
        swap(&arr[mid], &arr[high], NULL);
    swap(&arr[mid], &arr[high], NULL); // Coloca o pivot no final
    return arr[high];
}

int partition(int arr[], int low, int high, Metricas* metricas) {
    int pivot = medianaDeTres(arr, low, high);
    int i = (low - 1);
    
    for (int j = low; j <= high - 1; j++) {
        metricas->comparacoes++;
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j], metricas);
        }
    }
    swap(&arr[i + 1], &arr[high], metricas);
    return (i + 1);
}

void quickSort(int arr[], int low, int high, Metricas* metricas) {
    if (low < high) {
        int pi = partition(arr, low, high, metricas);
        quickSort(arr, low, pi - 1, metricas);
        quickSort(arr, pi + 1, high, metricas);
    }
}

int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    Metricas metricas = {0, 0, 0.0};
    clock_t inicio = clock();

    quickSort(arr, 0, n-1, &metricas);

    clock_t fim = clock();
    metricas.tempoExecucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;

    printf("Sorted array: \n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    printf("\nComparacoes: %d\nTrocas: %d\nTempo de execucao: %lf segundos\n", metricas.comparacoes, metricas.trocas, metricas.tempoExecucao);
    return 0;
}
