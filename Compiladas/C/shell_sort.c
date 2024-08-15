#include <stdio.h>
#include <time.h>

typedef struct {
    int comparacoes;
    int trocas;
    double tempoExecucao;
} Metricas;

void shellSort(int arr[], int n, Metricas* metricas) {
    clock_t inicio = clock();

    for (int gap = n/2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                metricas->comparacoes++;
                arr[j] = arr[j - gap];
                metricas->trocas++;
            }
            arr[j] = temp;
            metricas->trocas++;
        }
    }

    clock_t fim = clock();
    metricas->tempoExecucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
}

int main() {
    int arr[] = {12, 34, 54, 2, 3};
    int n = sizeof(arr)/sizeof(arr[0]);

    Metricas metricas = {0, 0, 0.0};
    shellSort(arr, n, &metricas);

    printf("Sorted array: \n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    printf("\nComparacoes: %d\nTrocas: %d\nTempo de execucao: %lf segundos\n", metricas.comparacoes, metricas.trocas, metricas.tempoExecucao);
    return 0;
}
