def find_maximum(arr,n):
    if n==1:
        return arr[0]
    maximum=find_maximum(arr,n-1)
    if arr[n-1]>maximum:
        return arr[n-1]
    else:
        return maximum

arr=[3,7,10]
result=find_maximum(arr,len(arr))
print("Maximum element is:",result)
   