'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # sort the arr
    arr.sort()

    if arr[0] != arr[1]:
        return arr[0]

    if arr[len(arr)-1] != arr[len(arr)-2]:
        return arr[len(arr)-1]

    # loop through the arr if it's a pair, increment 2
    for i in range(1, len(arr)-1):
        prev_item = arr[i-1]
        next_item = arr[i+1]
        item = arr[i]
        if item != prev_item and item != next_item:
            return item


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
