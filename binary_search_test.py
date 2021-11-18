def binarySearch(array, target):
    return binary_search_helper(array, target, 0, len(array)-1)


def binary_search_helper(array, target, left, right):
    # define base case doesn't fine target
    if left > right:
        return -1

    midx = (left + right) // 2  # round down of sum of left and right
    # store possible match
    possible_match = array[midx]
    # secondary base winning case return index where found
    if target == possible_match:
        return midx
    # define if target is less than midx possible match
    elif target < possible_match:
        # Make right edge index of middle -1 and Continue
        return binary_search_helper(array, target, left, midx - 1)
    else:
        # make left edge index of middle +1 and Continue
        return binary_search_helper(array, target, midx + 1, right)


arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]

print(binarySearch(arr, 33))
