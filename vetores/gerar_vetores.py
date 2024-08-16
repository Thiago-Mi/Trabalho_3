import random

# Gera vetores de tamanhos especificados com diferentes padrões
cases = ["aleatorios", "crescente", "decrescente"]
vectors = {}

# Gera vetores e armazena em um dicionário
for size in range(100, 15000, 100):
    vectors[size] = {}
    # Vetores aleatórios
    intervalo = list(range(1, size + 1))
    # Seleciona uma amostra aleatória do intervalo sem repetição
    vectors[size]["aleatorios"] = random.sample(intervalo, size)
    # Vetores em ordem crescente
    vectors[size]["crescente"] = list(range(size))
    # Vetores em ordem decrescente
    vectors[size]["decrescente"] = list(range(size, 0, -1))

# Salva os vetores em um arquivo txt
with open('vetores/vetores_input_3.txt', 'w') as f:
    for size in range(100, 15000, 100):
        for case in cases:
            f.write(f"{size} {case}:\n")
            f.write(" ".join(map(str, vectors[size][case])) + "\n")

'/vetores/vetores_input_3.txt'  # Retorna o caminho do arquivo gerado

