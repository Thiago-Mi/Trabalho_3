#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
    int comparacoes;
    int trocas;
    double tempoExecucao;
} Metricas;

void selectionSort(int arr[], int n, Metricas* metricas) {
    clock_t inicio = clock();
    
    for (int i = 0; i < n-1; i++) {
        int min_idx = i;
        for (int j = i+1; j < n; j++) {
            metricas->comparacoes++;
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
        metricas->trocas++;
    }
    
    clock_t fim = clock();
    metricas->tempoExecucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    Metricas metricas = {0, 0, 0.0};
    selectionSort(arr, n, &metricas);
    
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    
    printf("\nComparacoes: %d\nTrocas: %d\nTempo de execucao: %lf segundos\n", metricas.comparacoes, metricas.trocas, metricas.tempoExecucao);
    return 0;
}
