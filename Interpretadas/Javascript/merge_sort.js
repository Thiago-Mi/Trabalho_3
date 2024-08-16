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

function merge(arr, l, m, r, metrics) {
    let n1 = m - l + 1;
    let n2 = r - m;

    let L = new Array(n1);
    let R = new Array(n2);

    for (let i = 0; i < n1; i++) L[i] = arr[l + i];
    for (let j = 0; j < n2; j++) R[j] = arr[m + 1 + j];

    let i = 0, j = 0, k = l;
    metrics.memoriaUsada+= (n1+n2+L.length+R.length+k) * 4;
    while (i < n1 && j < n2) {
        metrics.comparacoes++;
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
        metrics.trocas++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
        metrics.trocas++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
        metrics.trocas++;
    }
}

function mergeSort(arr, l, r, metrics) {
    if (l >= r) {
        return;
    }

    let m = Math.floor((l + r) / 2);
    mergeSort(arr, l, m, metrics);
    mergeSort(arr, m + 1, r, metrics);
    merge(arr, l, m, r, metrics);
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
    mergeSort(arr, 0, arr.length - 1, metricas);
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