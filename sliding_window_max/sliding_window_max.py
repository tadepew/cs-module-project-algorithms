'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):

    # length must be greater than k
    if not len(nums) > k:
        return -1

    # for a list of length 8 and window of 3, 8-3 = 5 + = 6 maxes
    window_max = [0] * (len(nums)-k+1)

    # need to add 1 because i is the first # in the window, so if the window is 3 and the length is 8 then it will stop at 5 but we need the range to stop at 6 to include 5 becuase the stop in range isn't inclusive
    for i in range(0, len(nums)-k+1):
        # doesn't include below index in slice end
        new_window_right = i + k
        # does include i in slice start
        new_window_left = i
        window_max[i] = max(nums[new_window_left:new_window_right])

    return window_max


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
