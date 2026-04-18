def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        #整列済みになってない場所から探索 
        #最初値それ自体ではなく、最小値となるインデックスに着目してる 
        min_index = i  
        for j in range(i,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]

    return arr
                    


arr = [5, 3, 8, 4, 2]
arr = selection_sort(arr)
print(arr)