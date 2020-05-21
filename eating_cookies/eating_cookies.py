'''
Input: an integer
Returns: an integer
'''
import functools


@functools.lru_cache(maxsize=None)
def eating_cookies(n):

    if n == 0:
        return 1

    if n < 4:
        initial = [1, 2, 4]
        return initial[n-1]
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
