#LIS (Longest increasing subsequence) hay còn được hiểu dãy con tăng dần dài nhất.
#Ý tưởng bài làm là mình sẽ chia cụm số ra rồi check trong dãy đấy có những phần tử nào bé hơn so với phần tử ở index_arr rồi so sánh.
def lis(arr):
    n=len(arr)
    d=[1]*n
    for index_arr in range(n):
        for index_arr1 in range(index_arr):
            if arr[index_arr1]<arr[index_arr]:
                d[index_arr]=max(d[index_arr], d[index_arr1]+1)
    ans=d[0]
    for i in d:
        ans=max(i, ans)
    print(ans)

if __name__=="__main__":
    arr=[4,3,2,1,4,7,8,0]
    lis(arr)