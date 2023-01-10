
def find_max_sum(arr, k):
    """Brute Force"""
    # max_sum = 0
    #
    # for i in range(len(arr) - k + 1):
    #     total = 0
    #
    #     for j in range(i, i+k):
    #         total += arr[j]
    #
    #     if total > max_sum:
    #         max_sum = total
    #
    # return max_sum

    """Sliding window"""
    max_sum = 0
    window_start, window_sum = 0, 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1

    return max_sum


print(find_max_sum([2, 3, 4, 1, 5], 2))
