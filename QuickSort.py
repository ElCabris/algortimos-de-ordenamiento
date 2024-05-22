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
            a[i], a[elementos_menores] = a[elementos_menores], a[i]
            elementos_menores += 1

    a[elementos_menores], a[mayor] = a[mayor], a[elementos_menores]
    return elementos_menores
