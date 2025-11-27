
def separar_pares_impares(numeros):
    """Recebe uma lista de inteiros e retorna (pares, impares), mantendo a ordem."""
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    return pares, impares


def ler_inteiro(msg):
    """Lê um número inteiro do usuário com re-prompt em caso de erro."""
    while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("⚠️  Entrada inválida. Digite um número inteiro.")


def main():
    print("=== Particionador de IDs por Shard (A/B) ===\n")
    ids = []
    for i in range(1, 21):
        n = ler_inteiro(f"Digite o {i}º ID: ")
        ids.append(n)

    shard_a, shard_b = separar_pares_impares(ids)

    print("\nLista (entrada):", ids)
    print(f"Shard A (PAR): {shard_a}  | total: {len(shard_a)}")
    print(f"Shard B (ÍMPAR): {shard_b}  | total: {len(shard_b)}")


if __name__ == "__main__":
    main()
