'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import sys
INT_MIN = -sys.maxsize - 1


def sliding_window_max(nums, k):

    # length must be greater than k
    if not len(nums) > k:
        print("Invalid")
        return -1

    # Find of first window of size k
    max_sum = INT_MIN
    window_max = []
    window_max.append(max(nums[:k]))

    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    for i in range(1, len(nums)-k+1):
        new_window_right = i + k
        new_window_left = i
        window_max.append(max(nums[new_window_left:new_window_right]))

    return window_max


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
