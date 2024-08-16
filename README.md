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
   - **Complexidade de Espaço**: O(k)
   - **Descrição**: Counting Sort é um algoritmo de ordenação não-comparativa que conta a ocorrência de cada elemento e usa essa contagem para determinar a posição de cada elemento na lista ordenada.

3. **Radix Sort**
   - **Complexidade de Tempo (Melhor caso, Médio, Pior caso)**: O(d*(n + k)), onde d é o número de dígitos e k é o valor máximo possível dos dígitos
   - **Complexidade de Espaço**: O(n + k)
   - **Descrição**: Radix Sort ordena os números processando cada dígito de forma individual, geralmente utilizando Counting Sort como sub-rotina.

4. **Heap Sort**
   - **Complexidade de Tempo (Melhor caso, Médio, Pior caso)**: O(n log n)
   - **Complexidade de Espaço**: O(1)
   - **Descrição**: Heap Sort é um algoritmo de ordenação baseado em uma estrutura de dados chamada heap binário. Ele converte a lista em um heap e então extrai o maior elemento repetidamente para formar a lista ordenada.

5. **Shell Sort**
   - **Complexidade de Tempo**
     - **Melhor caso**: O(n log n) (depende da sequência de gap usada)
     - **Médio**: entre O(n log² n) e O(n^(3/2))
     - **Pior caso**: O(n²)
   - **Complexidade de Espaço**: O(1)
   - **Descrição**: Shell Sort é uma generalização do Insertion Sort que permite a troca de elementos que estão longe um do outro, melhorando a eficiência comparada ao Insertion Sort.

6. **Quick Sort**
   - **Complexidade de Tempo**
     - **Melhor caso**: O(n log n)
     - **Médio**: O(n log n)
     - **Pior caso**: O(n²) (ocorre quando o pivô escolhido é o menor ou maior elemento)
   - **Complexidade de Espaço**: O(log n)
   - **Descrição**: Quick Sort é um algoritmo de ordenação por divisão e conquista que escolhe um pivô e particiona a lista em elementos menores e maiores que o pivô, ordenando-os recursivamente.

7. **Selection Sort**
   - **Complexidade de Tempo (Melhor caso, Médio, Pior caso)**: O(n²)
   - **Complexidade de Espaço**: O(1)
   - **Descrição**: Selection Sort é um algoritmo de ordenação simples que seleciona repetidamente o menor (ou maior) elemento de uma lista não ordenada e o coloca na posição correta.

8. **Bubble Sort**
   - **Complexidade de Tempo**
     - **Melhor caso**: O(n) (ocorre quando a lista já está ordenada)
     - **Médio**: O(n²)
     - **Pior caso**: O(n²)
   - **Complexidade de Espaço**: O(1)
   - **Descrição**: Bubble Sort é um algoritmo simples de ordenação que repetidamente percorre a lista, trocando elementos adjacentes que estão na ordem errada.

## Objetivo

O objetivo deste estudo é entender como a natureza das linguagens de programação compiladas versus interpretadas afeta o desempenho dos algoritmos de ordenação. Embora a complexidade de tempo Big O ofereça uma visão teórica sobre o comportamento dos algoritmos, o desempenho real pode variar significativamente entre as diferentes linguagens devido a fatores como:

- **Eficiência do compilador ou interpretador**
- **Gestão de memória**
- **Optimizações internas**
- **Overhead de interpretação**

## Metodologia

### Complexidade de Tempo Big O

Cada algoritmo foi analisado teoricamente para determinar sua complexidade de tempo Big O, que serve como base para prever o desempenho em grandes volumes de dados.

### Desempenho Real

Os algoritmos foram implementados em C, C++, Python e JavaScript. Em seguida, rodamos testes de benchmark utilizando diferentes tamanhos de entrada, (100, 1000, 10000, 100000) para medir o tempo de execução de cada algoritmo em cada linguagem. Estes testes foram executados em condições controladas para garantir a consistência dos resultados.

### Ferramentas Utilizadas

- **C/C++**: Compilador GCC.
- **Python**: Python 3.12.x.
- **JavaScript**: Node.js.

### Métricas Coletadas

- **Tempo de Execução**: Medido em milissegundos.
- **Trocas de valor entre variáveis** Avaliado sempre que possível.
- **Comparações entre variáveis** Avaliado sempre que possível.
- **Diferenças Semânticas e Sintáticas**: Observações sobre como as características das linguagens afetam a implementação dos algoritmos.

## Resultados e Discussão

Os resultados são apresentados em gráficos que mostram o tempo de execução de cada algoritmo nas diferentes linguagens para diferentes tamanhos de entrada. Discussões subsequentes abordam as seguintes questões:

- Como a natureza compilada de C e C++ proporciona vantagens em termos de velocidade de execução?
- De que maneira as linguagens interpretadas, como Python e JavaScript, apresentam sobrecargas que afetam o desempenho?
- Há diferenças significativas no desempenho de algoritmos que dependem fortemente de operações de comparação versus aqueles que dependem de operações aritméticas?
- Como a gestão de memória e otimizações internas das linguagens influenciam o desempenho dos algoritmos?

- Este estudo revela que, embora a complexidade Big O seja um indicador importante, o desempenho real dos algoritmos de ordenação varia consideravelmente entre as linguagens de programação. As linguagens compiladas (C e C++) tendem a ser bem mais rápidas, especialmente para grandes volumes de dados, enquanto as linguagens interpretadas (Python e JavaScript) sofrem com maior overhead, embora ofereçam maior flexibilidade e facilidade de uso. O python por exemplo sofre com o limite de tarefas em recurção que é baixo, por padrão são 1000, esse fato gera a necessidade de aplicar melhoria nos algoritmos para diminuir o volume recursivo, como no caso do quick_sort, em seu pior caso, a escolha de um pivo ruim estoura facilmente o limite de tarefas recursivas no python, o que não acontece no javascript e nem nas linguagens compiladas, considerando o volume de dados utilizado.

## Conclusão

- Linguagens compiladas como C e C++ oferecem desempenho superior para algoritmos de ordenação devido à sua execução direta no hardware, permitindo otimizações de baixo nível e controle eficiente da memória. Isso resulta em tempos de execução significativamente mais rápidos e previsíveis em comparação com linguagens interpretadas. Além disso, C e C++ têm melhor suporte para paralelismo e multi-threading, o que é crucial para manipular grandes volumes de dados de maneira eficaz, linguagens interpretadas como Python e JavaScript sofrem com overhead adicional causado pela interpretação em tempo de execução e pela coleta de lixo, o que pode levar a tempos de execução menos consistentes e mais lentos. Além disso, essas linguagens oferecem menos controle sobre a memória e são menos eficientes em operações de baixo nível, tornando-as menos ideais para tarefas críticas de desempenho, como a ordenação de grandes conjuntos de dados. Por outro lado, a implementação desses algoritmos nas linguagens interpretadas é muito mais direta e facilitada pela natureza mais simplificada das linguagens.

## Instruções de Execução

Para reproduzir os benchmarks, siga as instruções abaixo para cada linguagem:

### C/C++

1. Compile o código utilizando `gcc`.
2. Execute o binário gerado.

### Python

1. Certifique-se de ter Python 3.12.x instalado.
2. Execute o script com `python`.

### JavaScript

1. Instale o Node.js.
2. Execute o script com `node`.
