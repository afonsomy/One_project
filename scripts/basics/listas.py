
def crialista(tamanho: int) -> list:

    lista_temp = []

    for i in range(tamanho):
        lista_temp.append(i)

    return lista_temp


def main():
    lista_a = crialista(3)
    lista_b = crialista(4)
    lista_c = [lista_a,lista_b]
    print(lista_c)
    lista_c[1].remove(1)

    print(lista_c)

if __name__ == "__main__":
    main()

