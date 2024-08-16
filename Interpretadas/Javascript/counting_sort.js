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

function countingSort(arr, metrics) {
    let max = Math.max(...arr);
    let count = new Array(max + 1).fill(0);
    let output = new Array(arr.length);

    metrics.memoriaUsada += (max + 1) * 4 + (arr.length + count.length + output.length) * 4 ;

    for (let i = 0; i < arr.length; i++) {
        count[arr[i]]++;
    }

    for (let i = 1; i <= max; i++) {
        count[i] += count[i - 1];
    }

    for (let i = arr.length - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
        metrics.trocas++;
    }

    for (let i = 0; i < arr.length; i++) {
        arr[i] = output[i];
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
    countingSort(arr, metricas);
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