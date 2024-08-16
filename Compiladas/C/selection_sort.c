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

void selectionSort(int arr[], int n, Metricas* metricas) {   
    for (int i = 0; i < n-1; i++) {
        int min_idx = i;
        for (int j = i+1; j < n; j++) {
            metricas->comparacoes++;
            if (arr[j] < arr[min_idx])
                min_idx = j;
                 metricas->trocas++;
        }
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
        metricas->trocas++;
        metricas->memoriaUsada += (min_idx + temp)*sizeof(int);
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
    selectionSort(arr, tamanho, &metricas);
    clock_t fim = clock();
    metricas.tempoExecucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;

    printf("Comparacoes: %d\n", metricas.comparacoes);
    printf("Trocas: %d\n", metricas.trocas);
    printf("Tempo de execucao: %lf\n", metricas.tempoExecucao);
    printf("Memoria usada: %d\n", metricas.memoriaUsada);

    free(arr);
    return 0;
}
