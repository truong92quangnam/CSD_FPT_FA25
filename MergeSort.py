#Đây là một dạng giải thuật này trong thuật toán chia để trị
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    #Mình sẽ dùng một thuật toán khá là đơn giản đấy là thuật toán 2 con trỏ
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    #Dùng method append sẽ khiến cho đưa về thành dạng [a,b,[c,d,f]] nên mới phải dùng extend để đưa về [a,b,c,d,f]
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
    else:
        return arr
    left_half= arr[:mid]
    right_half= arr[mid:]

    sorted_left_half=mergesort(left_half)
    sorted_right_half=mergesort(right_half)
    return list(merge(sorted_left_half, sorted_right_half))

if __name__=="__main__":
    a=[23,1,4,5,2,10,100]
    a=mergesort(a)
    for i in a:
        print(i,end=' ')