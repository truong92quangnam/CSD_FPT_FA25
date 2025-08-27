#Thuật toán này có điểm hay là chỉ điểm các phần tử trong array thành các xô hay còn gọi là các nhóm nhỏ để
#Triển khai những gì cần sắp xếp
#Dạng này phù hợp khi trong mảng chỉ có các số thập phân
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Đẩy các phẩn tử vòng trung các xô
    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)

    # Sắp xếp các nhóm hay xô vào trong dạng insertion sort
    for bucket in buckets:
        insertion_sort(bucket)

    #Tập hợp lại để đưa về lại dạng array
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucket_sort(arr)
print("Sorted array is:")
print(" ".join(map(str, arr)))