def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # Swap smallest and largest elements
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


def bubble_sort(arr):
    # Keep looping while elements have been swapped
    swapped_elements = True
    while swapped_elements:

        # Reset swapped elements
        swapped_elements = False

        for i in range(0, len(arr) - 1):

            # Is this pair of elements sorted?
            if arr[i] > arr[i+1]:
                # swap the elements, note that elements have been swapped
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped_elements = True

    return arr


'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

> We need the "+1" to include a space for zero
> Also, this algorithm will only work if we both the minimum and maximum value
> If the minimum value is negative, we need to know

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?

> The time complexity of the counting sort is O(n). It does 3 loops, starting by finding the minimum
> and maximum values. Then it loops through and counts the number of occurances of each value.
> Finally, it loops over the counts to generate the sorted list
>
> The space complexity of counting sort is `O(n)`. We have to create an array that is at least
> `maximum - minimum` elements large.
'''


def counting_sort(arr, minimum=None, maximum=None):
    if len(arr) <= 1:
        return arr
    if minimum is None or maximum is None:
        minimum = arr[0]
        maximum = arr[0]
        for val in arr:
            if val < minimum:
                minimum = val
            if val > maximum:
                maximum = val
    counts = [0] * (maximum - minimum + 1)
    for val in arr:
        counts[val - minimum] += 1

    resultIdx = 0
    for val, count in enumerate(counts):
        for i in range(0, count):
            arr[resultIdx] = val + minimum
            resultIdx += 1
    return arr
