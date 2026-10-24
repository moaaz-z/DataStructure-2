def bubble_sort(arr) :
    for j in range (len(arr)):
        ##swapped = False
        for i in range (len(arr)-1-j) :
            if arr[i]>arr[i+1] :
                arr[i],arr[i+1]=arr[i+1],arr[i]
                ##swapped = True
       ## if not swapped:
           ## break   --> If no swaps occur during a pass, the array is already sorted, so we terminate early.(saves time)
    return arr


##[50,80,20,10,30,40,60,70,90]
def insertion_sort(arr): 
    for j in range (1,len(arr)) : ##cuz first element is considered sorted.
        temp = arr[j]  
        i=j-1 
        while (i>=0 and arr[i]>temp):##While the current element is greater than the temp value, shift the current element to the right
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = temp ##Insert the temp value in the correct position

        
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):##i=1 cuz no need to compare the currect element with itself
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i] ##Swap
    return arr







def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # takes the arr from the start to mid - 1
    right = merge_sort(arr[mid:])  # takes the arr from mid to end

    #this part basically splits the arr into single leaves so we can compare them and merge 
    
    return merge(left, right)


def merge(left, right):
    res = []
    i = 0
    j = 0

   
    while i < len(left) and j < len(right):     # if both have aelements we compare and append the smaller one
        if left[i] <= right[j]:  
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

 
    res.extend(left[i:])                        # if right finishes while left still has elements
    res.extend(right[j:])                       # if left finishes while right still has elements

    return res






    





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


def hybrid_merge_sort(arr, threshold):
    if len(arr) <= threshold:
        return selection_sort(arr)#apply selection sort on len(arr)<=threshold

    mid = len(arr) // 2

    left = hybrid_merge_sort(arr[:mid], threshold)
    right = hybrid_merge_sort(arr[mid:], threshold)

    return merge(left, right)