#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <limits.h>

typedef struct {
    int comparacoes;
    int trocas;
    double tempoExecucao;  // Em segundos
    size_t memoriaUsada;   // Em bytes
} Metricas;

void countingSortForRadix(int* arr, int n, int exp, Metricas* metricas) {
    int* output = (int*)malloc(n * sizeof(int));
    int count[10] = {0};

    metricas->memoriaUsada += (sizeof(count) + n * sizeof(int));

    for (int i = 0; i < n; i++) {
        int index = (arr[i] / exp) % 10;
        count[index]++;
    }

    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    for (int i = n - 1; i >= 0; i--) {
        int index = (arr[i] / exp) % 10;
        output[count[index] - 1] = arr[i];
        count[index]--;
    }

    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }

    free(output);
}

void radixSort(int* arr, int n, Metricas* metricas) {
    int max_val = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max_val) {
            max_val = arr[i];
        }
    }

    for (int exp = 1; max_val / exp > 0; exp *= 10) {
        countingSortForRadix(arr, n, exp, metricas);
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
    Metricas metricas = {0, 0, 0.0, 0};
    int vetorSize = 0;
    int* arr = carregarVetor(1000, "aleatorios", &vetorSize);

    clock_t inicio = clock();
    radixSort(arr, vetorSize, &metricas);
    clock_t fim = clock();
    metricas.tempoExecucao = (double)(fim - inicio) / CLOCKS_PER_SEC;

    printf("Comparacoes: %d\n", metricas.comparacoes);
    printf("Trocas: %d\n", metricas.trocas);
    printf("Tempo de execucao: %f segundos\n", metricas.tempoExecucao);
    printf("Memoria usada: %lu bytes\n", (unsigned long)metricas.memoriaUsada);

    free(arr);
    return 0;
}
