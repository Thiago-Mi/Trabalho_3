#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// Estrutura para armazenar as metricas
typedef struct {
    int comparacoes;
    long trocas;
    double tempoExecucao;
    int memoriaUsada;
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


void loadArray(int arr[], int size, const char* caseType) {
    FILE* file = fopen("D:/Documentos/cefet/AEDS/Trabalho_3/vetores/vetores_input_2.txt", "r");
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
    mergeSort(arr, 0, tamanho - 1, &metricas);
    clock_t fim = clock();
    metricas.tempoExecucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;

    printf("Comparacoes: %d\n", metricas.comparacoes);
    printf("Trocas: %ld\n", metricas.trocas);
    printf("Tempo de execucao: %lf\n", metricas.tempoExecucao);
    printf("Memoria usada: %d\n", metricas.memoriaUsada);

    free(arr);
    return 0;
}
