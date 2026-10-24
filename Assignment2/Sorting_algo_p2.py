import SortingAlgorithms as s
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

def hybrid_merge_sort(arr, threshold):
    if len(arr) <= threshold:
        return s.selection_sort(arr)#apply selection sort on len(arr)<=threshold

    mid = len(arr) // 2

    left = hybrid_merge_sort(arr[:mid], threshold)
    right = hybrid_merge_sort(arr[mid:], threshold)

    return merge(left, right)