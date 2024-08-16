# Comparação de Desempenho e Complexidade de Algoritmos de Ordenação em C, C++, Python e JavaScript

## Introdução

Este documento apresenta uma análise comparativa do desempenho de algoritmos de ordenação implementados em quatro linguagens de programação: C, C++, Python e JavaScript. Estas linguagens foram divididas em dois grupos principais: **Compiladas** (C e C++) e **Interpretadas** (Python e JavaScript). A análise foca em dois aspectos principais:

1. **Complexidade de Tempo Big O**: Avaliação teórica da eficiência dos algoritmos.
2. **Desempenho Real**: Medição prática do tempo de execução dos algoritmos em diferentes linguagens.

## Algoritmos de Ordenação Avaliados

Os algoritmos de ordenação comparados neste estudo são:

- **Merge Sort**
- **Counting Sort**
- **Radix Sort**
- **Heap Sort**
- **Shell Sort**
- **Quick Sort**
- **Selection Sort**
- **Bubble Sort**

## Análise Big O

Abaixo está a análise de complexidade de tempo Big O para cada algoritmo de ordenação:

1. **Merge Sort**
   - **Complexidade de Tempo (Melhor caso, Médio, Pior caso)**: O(n log n)
   - **Complexidade de Espaço**: O(n)
   - **Descrição**: Merge Sort é um algoritmo de ordenação por divisão e conquista que divide a lista em sublistas menores até que cada sublista tenha apenas um elemento, e então combina essas sublistas em uma lista ordenada.

2. **Counting Sort**
   - **Complexidade de Tempo (Melhor caso, Médio, Pior caso)**: O(n + k), onde k é o valor máximo no array
   - **Complexidade de Espaço**: O(n + k)
   - **Descrição**: Counting Sort é um algoritmo de ordenação não-comparativa que conta a ocorrência de cada elemento e usa essa contagem para determinar a posição de cada elemento na lista ordenada.

3. **Radix Sort**
   - **Complexidade de Tempo (Melhor caso, Médio, Pior caso)**: O(d*(n + k)), onde d é o número de dígitos e k é o valor máximo possível dos dígitos
   - **Complexidade de Espaço**: O(n + k)
   - **Descrição**: Radix Sort ordena os números processando cada dígito de forma individual, utilizando um algoritmo de ordenação estável como o Counting Sort para cada posição do dígito.

4. **Heap Sort**
   - **Complexidade de Tempo (Melhor caso, Médio, Pior caso)**: O(n log n)
   - **Complexidade de Espaço**: O(1)
   - **Descrição**: Heap Sort converte a lista em uma estrutura de dados conhecida como heap, onde o maior (ou menor) elemento é sempre o nó raiz. Ele então remove o nó raiz e o coloca na posição final, repetindo o processo até que a lista esteja ordenada.

5. **Shell Sort**
   - **Complexidade de Tempo**: O(n log n) em muitos casos, variando dependendo da escolha dos gaps
   - **Complexidade de Espaço**: O(1)
   - **Descrição**: Shell Sort é uma versão otimizada do Insertion Sort que compara elementos distantes ao invés de adjacentes, o que reduz drasticamente o número de comparações necessárias.

6. **Quick Sort**
   - **Complexidade de Tempo**: O(n log n) no melhor e médio caso, O(n^2) no pior caso
   - **Complexidade de Espaço**: O(log n) (devido à pilha de recursão)
   - **Descrição**: Quick Sort é um algoritmo de ordenação por divisão e conquista que seleciona um elemento como pivô e particiona a lista em duas sublistas, uma com elementos menores e outra com elementos maiores que o pivô. O processo é repetido recursivamente.

7. **Selection Sort**
   - **Complexidade de Tempo (Melhor caso, Médio, Pior caso)**: O(n^2)
   - **Complexidade de Espaço**: O(1)
   - **Descrição**: Selection Sort é um algoritmo simples que percorre a lista repetidamente, selecionando o menor (ou maior) elemento e movendo-o para a posição correta.

8. **Bubble Sort**
   - **Complexidade de Tempo**: O(n^2) no pior e médio caso, O(n) no melhor caso
   - **Complexidade de Espaço**: O(1)
   - **Descrição**: Bubble Sort é um algoritmo de ordenação simples onde cada elemento é comparado com o próximo, trocando-os se estiverem fora de ordem. Este processo é repetido até que a lista esteja ordenada.

## Discussões

### Arquivo de Input

Todos os testes foram executados com os mesmos vetores de entrada aleatorios, garantindo que não haja disparidade no desempenho de cada algoritmo. Foi gerado 3 arquivos input com configurações diferentes de vetores, o que foi usado possui vetores de 100 a 150000 variando de 100 em 100 até chegar em 150000 em trios de aleatorios, crescente e decrescente para cada tamanho

### Impacto da Interpretação e Overhead

As linguagens interpretadas, como Python e JavaScript, sofrem de um overhead significativo devido à interpretação e à gestão de memória, o que impacta diretamente o tempo de execução dos algoritmos. No caso do Python, o Global Interpreter Lock (GIL) é um fator crítico, pois impede a execução simultânea de múltiplas threads em programas CPU-bound, limitando o potencial de paralelismo em operações que poderiam se beneficiar disso, como o Quick Sort.

### Comportamento dos Algoritmos de Ordenação

Os algoritmos com complexidade O(n log n), como Merge Sort e Quick Sort, apresentaram desempenho consistentemente melhor nas linguagens compiladas, enquanto os algoritmos O(n^2), como Selection Sort e Bubble Sort, mostraram diferenças mais pronunciadas entre as linguagens devido ao impacto do overhead.

### Observações Específicas sobre JavaScript

Uma discrepância interessante foi observada no tempo de execução do Bubble Sort em JavaScript. Esta discrepância pode ser atribuída a otimizações específicas do motor de JavaScript, como o V8, que possui otimizações de JIT (Just-In-Time compilation) e outras técnicas avançadas que melhoram o desempenho, especialmente em algoritmos simples e operações com arrays menores. Investigações mais detalhadas poderiam explorar se houve alguma outra variável externa, como a carga de trabalho da máquina durante os testes, que também poderia ter influenciado os resultados.

## Conclusão

As linguagens compiladas, como C e C++, mostraram-se superiores em termos de desempenho, especialmente para algoritmos com complexidade O(n log n) e O(n^2). Além disso, as linguagens compiladas se beneficiam de otimizações específicas do compilador e suporte nativo a paralelismo e multi-threading, o que não foi explorado neste estudo, mas poderia ter um impacto ainda maior em certos algoritmos.

Por outro lado, as linguagens interpretadas, como Python e JavaScript, apresentaram maiores tempos de execução devido ao overhead da interpretação e à gestão de memória. No entanto, vale destacar que essas linguagens oferecem uma maior facilidade de desenvolvimento e implementação de algoritmos, tornando-as ideais para prototipagem, scripts rápidos, e desenvolvimento ágil em contextos onde o desempenho absoluto não é o fator mais crítico.


## Instruções de Execução

Todos os arquivos em python foram projetados para serem executados em suas respectivas pastas de origem.
Caso tenha problemas para executar os algoritmos entre no arquivo comparações.py e modifique o caminho presente nos dicionários algorithms_(x) onde o x 
é o tipo de arquivo como py ou cpp.
Modifique o caminho do arquivo txt de vetores a ser carregado em cada algoritmo de ordenação em todas as linguagens por meio de um DEFINE.

Para reproduzir os benchmarks, siga as instruções abaixo para cada linguagem:

### C/C++
1. Compile cada código da pasta utilizando `gcc`.

### JavaScript

1. Instale o Node.js.

### Python

1. Modifique também o caminho  que será usado para ser salvo os graficos gerados.
2. Certifique-se de ter Python 3.12.x instalado.
3. Execute o script  comparacoes.py com `python`.


