#Ý tưởng này cũng là dạng chia để trị nhưng mà nó điểm hay là dùng những digit trong số để sắp xếp dần các thứ tự
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1 , n):
               if arr[i] > arr[j]:
                    arr[i], arr[j]=arr[j], arr[i]

def radixSortWithBubbleSort(arr):
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        radixArray = [[],[],[],[],[],[],[],[],[],[]]
        
        for num in arr:
            radixIndex = (num // exp) % 10
            radixArray[radixIndex].append(num)
        
        for bucket in radixArray:
            bubbleSort(bucket)
        
        i = 0
        for bucket in radixArray:
            for num in bucket:
                arr[i] = num
                i += 1
        
        exp *= 10

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
radixSortWithBubbleSort(myArray)
print("Sorted array:", myArray)