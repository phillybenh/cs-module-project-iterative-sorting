# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # can do this w/o smallest_index, but will do it the Lambda way
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], \
            arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    n = len(arr)
    # 1. Loop through your array
    for i in range(n):
        # - Compare each element to its neighbor
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # - If elements in wrong position (relative to each other, 
                # swap them)
                arr[j], arr[j+1] = arr[j+1], arr[j]
# 2. If no swaps performed, stop. Else, go back to the element at index 0 
#     and repeat step 1.

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
    O(n+k)-->O(n)
'''
def counting_sort(arr, maximum=None):
    # check arr to make sure it contains values,
    # and stop the sort
    if len(arr) == 0:
        return []
    # find maximum if it isn't passed in
    elif maximum is None:
        maximum = max(arr)
        print (maximum)

    m = maximum + 1
    # initialize the count array of '0' values
    count = [0 for i in range(m)]
    output = [0 for i in range(m)]
    # increment count array to store how many of each value exists in arr
    for x in arr:
        # check for negative values
        if x < 0:
            return "Error, negative numbers not allowed in Count Sort"
        # add to count array, where the index matches the value
        # ex. count = [0, 1, 3] means arr = [2, 1, 2, 2,]
        count[x] += 1
    # add value of previous position to count[i]
    for i in range(m):
        count[i] += count[i-1]
    # build output array
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    
    # i = 0
    # for y in range(m):
    #     for z in range(count[y]):
    #         arr[i] = y
    #         i += 1
    return output




