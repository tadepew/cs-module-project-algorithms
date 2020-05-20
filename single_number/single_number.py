'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):

    # first try: 56 steps in pythontutor

    # seen = set()
    # dup = []

    # for x in arr:
    #     if x not in seen:
    #         seen.add(x)
    #     else:
    #         dup.append(x)

    # for x in seen:
    #     if x not in dup:
    #         return x

    # one for loop: 40 steps in pythontutor // ranges from .003-.008 secs
    # unique = []
    # for i in arr:
    #     if i not in unique:
    #         unique.append(i)
    #     else:
    #         unique.remove(i)

    # return unique

    # one for loop but uses .sort() which has nlogn complexity: 44 steps in pythontutor // always .002 secs
    # arr.sort()
    # for i in range(0, len(arr)):
    #     if i % 2 == 0:
    #         if i == len(arr)-1:
    #             return arr[i]
    #         if arr[i] != arr[i+1]:
    #             return arr[i]
    #     else:
    #         if arr[i] != arr[i-1]:
    #             return arr[i]

    res = arr[0]

    # Do XOR of all elements and return
    for i in range(1, len(arr)):
        res = res ^ arr[i]

    return res


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    single_number(arr)
    print(f"The odd-number-out is {single_number(arr)}")
