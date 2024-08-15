#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct {
    int comparacoes;
    int trocas;
    double tempoExecucao;  // Em segundos
    size_t memoriaUsada;   // Em bytes
} Metricas;

void bubbleSort(int* arr, int n, Metricas* metricas) {
    metricas->memoriaUsada += n * sizeof(int);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            metricas->comparacoes++;
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                metricas->trocas++;
            }
        }
    }
}

int* carregarVetor(int tamanho, const char* caso, int* vetorSize) {
    FILE* file = fopen("D:/Documentos/cefet/AEDS/Trabalho_3/vetores/vetores_input.txt", "r");
    if (!file) {
        printf("Erro ao abrir o arquivo!\n");
        exit(1);
    }

    char line[256];
    char key[50];
    snprintf(key, sizeof(key), "%d %s:", tamanho, caso);

    int* vetor = NULL;
    while (fgets(line, sizeof(line), file)) {
        if (strcmp(line, key) == 0) {
            vetor = (int*)malloc(tamanho * sizeof(int));
            *vetorSize = 0;

            fgets(line, sizeof(line), file);
            char* token = strtok(line, " ");
            while (token != NULL) {
                vetor[*vetorSize] = atoi(token);
                printf("%d",atoi(token));
                (*vetorSize)++;
                token = strtok(NULL, " ");
            }
            break;
        }
    }

    fclose(file);
    
    return vetor;
}

int main() {
    Metricas metricas = {0,0,0.0,0};
    int vetorSize = 0;
    int* arr = carregarVetor(1000, "aleatorios", &vetorSize);

    clock_t inicio = clock();
    bubbleSort(arr, vetorSize, &metricas);
    clock_t fim = clock();
    metricas.tempoExecucao = (double)(fim - inicio) / CLOCKS_PER_SEC;

    printf("Comparacoes: %d\n", metricas.comparacoes);
    printf("Trocas: %d\n", metricas.trocas);
    printf("Tempo de execucao: %f segundos\n", metricas.tempoExecucao);
    printf("Memoria usada: %lu bytes\n", (unsigned long)metricas.memoriaUsada);

    free(arr);
    return 0;
}
