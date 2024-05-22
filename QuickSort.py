def quick_sort(a, menor, mayor):
    if menor < mayor:
        indice_pivot = partition(a, menor, mayor)

        quick_sort(a, menor, indice_pivot - 1)
        quick_sort(a, indice_pivot + 1, mayor)

def partition(a, menor, mayor):
    pivote = a[mayor]
    elementos_menores = menor

    for i in range(menor, mayor):
        if a[i] < pivote:
            aux = a[i]
            a[i] = a[elementos_menores]
            a[elementos_menores] = aux
            elementos_menores += 1

    aux = a[elementos_menores]
    a[elementos_menores] = a[mayor]
    a[mayor] = aux
    return elementos_menores
