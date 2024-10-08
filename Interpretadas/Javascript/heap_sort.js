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

function heapify(arr, n, i, metrics) {
    let largest = i;
    let left = 2 * i + 1;
    let right = 2 * i + 2;
    metrics.memoriaUsada+= (largest+left+right) * 4;
    metrics.comparacoes++;
    if (left < n && arr[left] > arr[largest])
        largest = left;
        metrics.trocas++;
    metrics.comparacoes++;
    if (right < n && arr[right] > arr[largest])
        largest = right;
        metrics.trocas++;
    metrics.comparacoes++;
    if (largest !== i) {
        swap(arr, i, largest);
        metrics.trocas++;
        heapify(arr, n, largest, metrics);
    }
}

function heapSort(arr, metrics) {
    let n = arr.length;
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--)
        heapify(arr, n, i, metrics);

    for (let i = n - 1; i > 0; i--) {
        swap(arr, 0, i);
        metrics.trocas++;
        heapify(arr, i, 0, metrics);
    }
}

function carregarVetor(tamanho, caso, caminhoVetor) {
    const data = fs.readFileSync(caminhoVetor, 'utf8');
    const lines = data.split('\n');
    const key = `${tamanho} ${caso}:`;
    for (let i = 0; i < lines.length; i++) {
        if (lines[i].trim() === key) {
            return lines[i + 1].trim().split(' ').map(Number);
        }
    }
    return [];
}

function main(tamanho, caso, caminhoVetor) {
    const metricas = new Metricas();
    const arr = carregarVetor(tamanho, caso, caminhoVetor);
    
    const inicio = performance.now();
    heapSort(arr, metricas);
    const fim = performance.now();
    
    metricas.tempoExecucao = (fim - inicio) / 1000; // Em segundos
    return {
        "Comparacoes": metricas.comparacoes,
        "Trocas": metricas.trocas,
        "Tempo de execucao": metricas.tempoExecucao,
        "Memoria usada": metricas.memoriaUsada
    };
}


const args = process.argv.slice(2);
const tamanho = parseInt(args[0]);
const caso = args[1];
const caminhoVetor = args[2];

const resultado = main(tamanho, caso, caminhoVetor);
console.log(resultado);