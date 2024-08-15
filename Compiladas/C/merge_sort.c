#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

// Estrutura para armazenar as metricas
typedef struct {
    int comparacoes;
    int trocas;
    double tempoExecucao;  // Armazena o tempo de execucao em segundos
    size_t memoriaUsada;   // Armazena a quantidade de memoria usada em bytes
} Metricas;

// Funcao para mesclar duas metades do array
void merge(int arr[], int l, int m, int r, Metricas *metricas) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    // Arrays temporarios
    int *L = (int *)malloc(n1 * sizeof(int));
    int *R = (int *)malloc(n2 * sizeof(int));
    metricas->memoriaUsada += (n1 + n2) * sizeof(int);

    // Copiar dados para arrays temporarios L[] e R[]
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    // Mesclar os arrays temporarios de volta em arr[l..r]
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        metricas->comparacoes++;
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copiar os elementos restantes de L[], se houver
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copiar os elementos restantes de R[], se houver
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }

    // Liberar a memoria dos arrays temporarios
    free(L);
    free(R);
}

// Funcao recursiva do Merge Sort
void mergeSort(int arr[], int l, int r, Metricas *metricas) {
    if (l < r) {
        int m = l + (r - l) / 2;

        // Ordenar a primeira e a segunda metade
        mergeSort(arr, l, m, metricas);
        mergeSort(arr, m + 1, r, metricas);

        // Mesclar as metades ordenadas
        merge(arr, l, m, r, metricas);
    }
}

// Funcao para imprimir um array
void printArray(int A[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
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

// Funcao principal
int main(int argc, char *argv[]) {
    int tamanho;
    int *arr;
    int *vetorsize;
    if (argc < 3) {
        printf("Uso: %s <tamanho do vetor> <caminho do arquivo>\n", argv[0]);
        return 1;
    }

    tamanho = atoi(argv[1]);
    char *caso = argv[2];

    arr = (int *)malloc(tamanho * sizeof(int));
    if (arr == NULL) {
        printf("Erro ao alocar memória.\n");
        return 1;
    }
    arr = carregarVetor(tamanho,caso,&vetorsize);

    Metricas metricas = {0, 0, 0.0, 0};


    // printf("Array inicial: \n");
    // printArray(arr, N);

    // Capturar o tempo de início
    clock_t inicio = clock();
    mergeSort(arr, 0, tamanho - 1, &metricas);
    // Capturar o tempo de termino
    clock_t fim = clock();

    // Calcular o tempo de execucao em segundos
    metricas.tempoExecucao = ((double) (fim - inicio)) / CLOCKS_PER_SEC;

    // printf("\nArray ordenado: \n");
    // printArray(arr, N);
    printf("Comparacoes: %d\n", metricas.comparacoes);
    printf("Trocas: %d\n", metricas.trocas);
    printf("Tempo de execucao: %f\n", metricas.tempoExecucao);
    printf("Memoria usada: %zu\n", (unsigned long)metricas.memoriaUsada);


    // Liberar a memoria alocada para o vetor
    free(arr);

    return 0;
}
