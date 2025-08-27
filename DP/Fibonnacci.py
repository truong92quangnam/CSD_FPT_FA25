#Đây là một dạng bài mở đầu để mọi người hiểu thêm một chút về cách hoạt động của quy hoạch động động chạm đến array 
# để thực hiện bài toán.
if __name__=="__main__":
    n=100
    a=[0]*(n+1)
    a[1]=1
    a[2]=1
    for i in range(3, n+1):
        a[i]=a[i-1]+a[i-2]
    print(a)