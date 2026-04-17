def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False #入れ替えが発生したかどうか
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True  #一度でも入れ替えが発生したらTrueになる

        if not swapped:
            break

    return arr


#並び替えたい配列
arr = [5, 3, 8, 4, 2]

arr = bubble_sort(arr)

print(arr)

