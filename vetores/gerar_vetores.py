import random

# Gera vetores de tamanhos especificados com diferentes padrões
sizes = [1000, 10000, 100000, 200000, 400000, 800000, 1000000]
cases = ["aleatorios", "crescente", "decrescente"]
vectors = {}

# Gera vetores e armazena em um dicionário
for size in sizes:
    vectors[size] = {}
    # Vetores aleatórios
    vectors[size]["aleatorios"] = [random.randint(0, size) for _ in range(size)]
    # Vetores em ordem crescente
    vectors[size]["crescente"] = list(range(size))
    # Vetores em ordem decrescente
    vectors[size]["decrescente"] = list(range(size, 0, -1))

# Salva os vetores em um arquivo txt
with open('vetores/vetores/vetores_input.txt', 'w') as f:
    for size in sizes:
        for case in cases:
            f.write(f"{size} {case}:\n")
            f.write(" ".join(map(str, vectors[size][case])) + "\n")

'vetores/vetores/vetores_input.txt'  # Retorna o caminho do arquivo gerado

