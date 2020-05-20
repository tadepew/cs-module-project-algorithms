'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):

    # for x in arr:
    #     if x == 0:
    #         arr.remove(x)
    #         arr.append(x)

    # return arr

    non_zero_pointer = 0

    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[non_zero_pointer], arr[i] = arr[i], arr[non_zero_pointer]
            non_zero_pointer += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
