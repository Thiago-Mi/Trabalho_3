#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


typedef struct {
    int comparacoes;
    long trocas;
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

void loadArray(int arr[], int size, const char* caseType, const char* caminhoVetor) {
    FILE* file = fopen(caminhoVetor, "r");
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
    if (argc != 4) {
        printf("Uso: ./counting_sort <tamanho do vetor> <caso> <caminho do arquivo>\n");
        return 1;
    }
    int tamanho = atoi(argv[1]);
    char* caso = argv[2];
    char* caminhoVetor = argv[3];

    Metricas metricas = {0, 0, 0.0, 0};
    int* arr = (int*)malloc(tamanho * sizeof(int));
    if (arr == NULL) {
        printf("Erro ao alocar memória.\n");
        return 1;
    }

    loadArray(arr, tamanho, caso, caminhoVetor);

    clock_t inicio = clock();
    countingSort(arr,tamanho, &metricas);
    clock_t fim = clock();
    metricas.tempoExecucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;

    printf("Comparacoes: %d\n", metricas.comparacoes);
    printf("Trocas: %ld\n", metricas.trocas);
    printf("Tempo de execucao: %lf\n", metricas.tempoExecucao);
    printf("Memoria usada: %d\n", metricas.memoriaUsada);

    free(arr);
    return 0;
}

