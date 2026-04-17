def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        key = arr[i]    #挿入する値
        j = i-1

        #左の整列済み部分の一番右から順に比較
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j] #右にずらす
            j -= 1

        arr[j+1] = key  #jは「入れるべき位置の1つ左」で止まっていることに注意

    return  arr

arr = [5, 3, 8, 4, 2]

arr = insertion_sort(arr)

print(arr)