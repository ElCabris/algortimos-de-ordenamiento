def selection_sort(a):

    n = len(a)
    for i in range(n):
        elemento_minimo = i
        for j in range(i + 1, n):
            if a[j] < a[elemento_minimo]:
                elemento_minimo = j
        aux = arr[i]
        arr[i] = arr[elemento_minimo]
        arr[elemento_minimo] = aux

arr = [38, 27, 43, 3, 9, 82, 10]
selection_sort(arr)
print(arr)
