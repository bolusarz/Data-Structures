import math


def smallest_subarray_with_given_sum(arr, s):
    window_start, window_sum = 0, 0
    min_window_len = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_window_len = min(window_end - window_start + 1, min_window_len)
            window_sum -= arr[window_start]
            window_start += 1

    return 0 if (min_window_len == math.inf) else min_window_len


print(smallest_subarray_with_given_sum([3, 4, 1, 1, 6], 8))

