

def binarySearch(arr,target):
    if(arr is not sorted ):
        arr=sorted(arr)
    low,high=0,len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if (target==arr[mid]):
            return mid
        elif (target>arr[mid]):
            low=mid+1
        elif(target<arr[mid]):
            high=mid-1
    return -1        


arr=[3,7,10]


def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        swap=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swap=True
        if not swap:
            break
    return arr

print(bubbleSort(arr))
            

