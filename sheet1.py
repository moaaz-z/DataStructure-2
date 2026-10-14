def second_largest(arr):
    if len(arr)==0:
        return 
    elif len(arr)==1:
        print("array has only one element")
        return
    else:
        secmax=arr[0]
        firmax=arr[1]
        for i in range(len(arr)):
            if arr[i]>firmax:
                secmax=firmax
                firmax=arr[i]
        return secmax
arr=[3,7,10]
result=second_largest(arr)
print("Second largest element is:",result)
