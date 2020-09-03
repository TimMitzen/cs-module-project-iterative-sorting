def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    first = 0 #set to pointers
    last = len(arr) - 1
    while first <= last:# loops contunies as log as low is less than or equal to high
        middle_point = (first + last) //2 # gets the middle index
        guess = arr[middle_point]# middle retrieves the item from the arr
        if guess == target:#if the guess is correct
            return middle_point# if the guess matches
        if guess > target: #if its to high
            last = middle_point - 1# if too high with reduce the poss by half
        else:               #if its to low
            first = middle_point + 1# we changedthe low to one point after the middle

    return -1  # not found
