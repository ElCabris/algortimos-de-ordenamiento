def selection_sort(a):

    n = len(a)
    for i in range(n):
        elemento_minimo = i
        for j in range(i + 1, n):
            if a[j] < a[elemento_minimo]:
                elemento_minimo = j
        aux = a[i]
        a[i] = a[elemento_minimo]
        a[elemento_minimo] = aux
