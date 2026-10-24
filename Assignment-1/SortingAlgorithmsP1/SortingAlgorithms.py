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


