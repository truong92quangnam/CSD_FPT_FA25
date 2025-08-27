#Ý tưởng thuật toán này sẽ tập trung vào việc lấy các phần tử nhỏ thứ n-th để tìm kiếm rồi swap lại
def SelectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index= i
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


if __name__=="__main__":
    arr = [64, 25, 12, 22, 11]
    arr=SelectionSort(arr)
    print(arr)
