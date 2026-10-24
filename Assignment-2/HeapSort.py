def MaxHeapify(arr,n,i):
    l=2*i+1
    r=2*i+2 #Calculate the children
    max=i #Assume the current node is the largest
    if(l<n and arr[l]>arr[max]): #l < n: the left child exists in the array. - arr[l] > arr[max]: the left child is greater than the current largest value.
        max=l
    if(r<n and arr[r]>arr[max]):
        max=r
    if(max!=i):#max found or not 
        temp=arr[i]
        arr[i]=arr[max]
        arr[max]=arr[temp]
        MaxHeapify(arr,n,max)#max is the index where the swapped element moved.
