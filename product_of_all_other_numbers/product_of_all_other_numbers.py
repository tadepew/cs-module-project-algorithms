'''
Input: a List of integers
Returns: a List of integers
'''

# TODO: loop over array and multiply every number except the index of which you are currently looping


def product_of_all_other_numbers(arr):
    # two for loops not nested is still O(n)

    # array of ones
    # basically multiplying everything to the left of each # by everything to the right of each # in this output array
    output = [1] * len(arr)

    # prod is everything multiplied before
    prod = 1
    # going to the right starting at the beginning
    for i in range(len(arr)):
        print(prod)
        # multiply everything before it
        output[i] = output[i] * prod
        # insert into element
        prod = prod * arr[i]

    prod = 1
    # decrement from the end going to the left
    for i in range(len(arr) - 1, -1, -1):
        print(prod)
        # multiply everything after it
        output[i] = output[i] * prod
        # insert into element
        prod = prod * arr[i]

    return output


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
    #        9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
