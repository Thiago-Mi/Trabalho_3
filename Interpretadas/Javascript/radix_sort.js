const fs = require('fs');
const { performance } = require('perf_hooks');

class Metricas {
    constructor() {
        this.comparacoes = 0; // Comparacoes não são feitas diretamente no Radix Sort
        this.trocas = 0;      // Trocas não são feitas diretamente no Radix Sort
        this.tempoExecucao = 0.0; // Em segundos
        this.memoriaUsada = 0;    // Em bytes
    }
}

function countingSortForRadix(arr, exp, metricas) {
    const n = arr.length;
    const output = new Array(n).fill(0);
    const count = new Array(10).fill(0);

    metricas.memoriaUsada += (count.length + output.length) * 4;

    for (let i = 0; i < n; i++) {
        const index = Math.floor(arr[i] / exp) % 10;
        count[index]++;
    }

    for (let i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    for (let i = n - 1; i >= 0; i--) {
        const index = Math.floor(arr[i] / exp) % 10;
        output[count[index] - 1] = arr[i];
        count[index]--;
    }

    for (let i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

function radixSort(arr, metricas) {
    const max_val = Math.max(...arr);
    for (let exp = 1; Math.floor(max_val / exp) > 0; exp *= 10) {
        countingSortForRadix(arr, exp, metricas);
        metricas.Comparacoes++;
    }
}

function carregarVetor(tamanho, caso) {
    const data = fs.readFileSync('D:/Documentos/cefet/AEDS/Trabalho_3/vetores/vetores_input_2.txt', 'utf8');
    const lines = data.split('\n');
    const key = `${tamanho} ${caso}:`;
    for (let i = 0; i < lines.length; i++) {
        if (lines[i].trim() === key) {
            return lines[i + 1].trim().split(' ').map(Number);
        }
    }
    return [];
}

function main(tamanho, caso) {
    const metricas = new Metricas();
    const arr = carregarVetor(tamanho, caso);
    
    const inicio = performance.now();
    radixSort(arr, metricas);
    const fim = performance.now();
    metricas.tempoExecucao = (fim - inicio) / 1000;

    console.log({
        "Comparacoes": metricas.comparacoes,
        "Trocas": metricas.trocas,
        "Tempo de execucao": metricas.tempoExecucao,
        "Memoria usada": metricas.memoriaUsada
    });
}

// Exemplo de chamada
// main(1000, "aleatorios");
