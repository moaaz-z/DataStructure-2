def MaxHeapify(arr,n,i):
    l=2*i+1
    r=2*i+2 #Calculate the children
    max=i #Assume the current node is the largest
    if(l<n and arr[l]>arr[max]): #l < n: the left child exists in the array. - arr[l] > arr[max]: the left child is greater than the current largest value.
        max=l
    if(r<n and arr[r]>arr[max]):
        max=r
    if(max!=i):#max found or not 
        arr[i], arr[max] = arr[max], arr[i]
        MaxHeapify(arr,n,max)#max is the index where the swapped element moved.
def BuildHeap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):#The last non-leaf node is at index n // 2 - 1
        MaxHeapify(arr, n, i)
def HeapSort(arr):
    n=len(arr)
    BuildHeap(arr)#Now the Max is in the Top
    for i in range(n-1,-1,-1):
        arr[0], arr[i] = arr[i], arr[0]
        MaxHeapify(arr,i,0)
