
def find_average_arr(arr, k):
    average_arr = []
    window_start, window_sum = 0, 0.0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            average_arr.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1

    return average_arr


print(find_average_arr([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
