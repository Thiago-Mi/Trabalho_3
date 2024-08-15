const fs = require('fs');
const { performance } = require('perf_hooks');

class Metricas {
    constructor() {
        this.comparacoes = 0;
        this.trocas = 0;
        this.tempoExecucao = 0.0; // Em segundos
        this.memoriaUsada = 0; // Em bytes
    }
}

function swap(arr, i, j) {
    [arr[i], arr[j]] = [arr[j], arr[i]];
}

// Função para escolher a mediana de três como pivot
function medianaDeTres(arr, low, high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[low] > arr[mid]) swap(arr, low, mid);
    if (arr[low] > arr[high]) swap(arr, low, high);
    if (arr[mid] > arr[high]) swap(arr, mid, high);
    swap(arr, mid, high); // Coloca o pivot no final
    return arr[high];
}

function partition(arr, low, high, metrics) {
    const pivot = medianaDeTres(arr, low, high);
    let i = (low - 1);

    for (let j = low; j < high; j++) {
        metrics.comparacoes++;
        if (arr[j] < pivot) {
            i++;
            swap(arr, i, j);
            metrics.trocas++;
        }
    }
    swap(arr, i + 1, high);
    metrics.trocas++;
    return (i + 1);
}

function quickSort(arr, low, high, metrics) {
    if (low < high) {
        const pi = partition(arr, low, high, metrics);

        quickSort(arr, low, pi - 1, metrics);
        quickSort(arr, pi + 1, high, metrics);
    }
}

function carregarVetor(tamanho, caso) {
    const data = fs.readFileSync('D:/Documentos/cefet/AEDS/Trabalho_3/vetores/vetores_input.txt', 'utf8');
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
    quickSort(arr, 0, arr.length - 1, metricas);
    const fim = performance.now();
    
    metricas.tempoExecucao = (fim - inicio) / 1000; // Em segundos
    console.log(tamanho, caso);
    return {
        "Comparacoes": metricas.comparacoes,
        "Trocas": metricas.trocas,
        "Tempo de execucao": metricas.tempoExecucao,
        "Memoria usada": metricas.memoriaUsada
    };
}
