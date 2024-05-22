def bubble_sort(a):

    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > a[j + 1]:
                aux = a[j]
                a[j] = a[j + 1]
                a[j + 1] = aux

arr = [38, 27, 43, 3, 9, 82, 10]

bubble_sort(arr)

print(arr)
