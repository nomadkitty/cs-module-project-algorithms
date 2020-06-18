'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number_naive(arr):  # O (n log n)
    # sort the arr O(n log n)
    arr.sort()

    # handle head and tail edge cases:
    if arr[0] != arr[1]:
        return arr[0]

    if arr[len(arr)-1] != arr[len(arr)-2]:
        return arr[len(arr)-1]

    # loop through the arr to check if the item is not equal to both previous and next item
    for i in range(1, len(arr)-1):  # O(n)
        prev_item = arr[i-1]
        next_item = arr[i+1]
        item = arr[i]
        if item != prev_item and item != next_item:
            return item


def single_number(nums):  # O(n)
    # keep track of number of times an item occurs in input
    counts = {}
    # loop through input list O(n)
    for num in nums:
        # if item in counts
        if num in counts:
            # remove item
            del counts[num]
        # otherwise
        else:
            counts[num] = 1
            # add item
    for k, v in counts.items():  # O(1)
        if v == 1:
            return k


def single_number_optimized_2(arr):  # O(n) for time O(1) for space
    s = set()
    # use either a dictionary or a set
    # sets: holding onto unique elements
    # loop through our arr
    for x in arr:
        # for each element
        # check if it is already in our set
        # if it is, then that's not our out-element-out
        if x in s:
            # remove the element from our set
            s.remove(x)
        else:
            s.add(x)
    # the odd-element-out will be the only element in the set
    return list(s)[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
