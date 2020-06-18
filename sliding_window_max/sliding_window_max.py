'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max_naive(nums, k):
    # created new empty list []
    new_list = []
    # loop through the array from idx 0 to len -k+1
    for idx in range(0, len(nums)-k+1):
        # create sub list [idx: idx+k]
        sub_list = nums[idx:idx+k]
        # append the max num of new array to new_list
        new_list.append(max(sub_list))
    # return new list
    return new_list


def sliding_window_max(nums, k):
    # set 1st window
    window = nums[:k]
    # set current_max to the 1st window max
    current_max = max(window)
    # create a list of max numbers with 1st item of current_max
    max_list = [current_max]

    # loop through the nums to slide window
    for num in nums[k:]:
        # append newest num to window
        window.append(num)
        # remove 1st num of the window
        # if it equal the current_max
        if window.pop(0) == current_max:
            # reassign the current_max value
            current_max = max(window)
        # check the newest value if it's max
        if num > current_max:
            # reassign x to current_max
            current_max = num
        # append current_max to max_list
        max_list.append(current_max)

    # return max_list
    return max_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
