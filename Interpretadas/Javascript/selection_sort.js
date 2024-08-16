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

function selectionSort(arr, metricas) {


    let n = arr.length;
    for (let i = 0; i < n-1; i++) {
        let min_idx = i;
        for (let j = i+1; j < n; j++) {
            metricas.comparacoes++;
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        [arr[min_idx], arr[i]] = [arr[i], arr[min_idx]];
        metricas.trocas++;
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
    selectionSort(arr, metricas);
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