
def fruit_in_basket(arr):
    mem = {}
    window_start, max_num = 0, 0

    for window_end in range(len(arr)):
        if arr[window_end] not in mem:
            mem[arr[window_end]] = 1
        else:
            mem[arr[window_end]] += 1

        while len(mem) > 2:
            mem[arr[window_start]] -= 1
            if mem[arr[window_start]] == 0:
                del mem[arr[window_start]]

            window_start += 1

        max_num = max(max_num, window_end - window_start + 1)

    return max_num


print(fruit_in_basket(['A', 'B', 'C', 'A', 'C']))
print(fruit_in_basket(['A', 'B', 'C', 'B', 'B', 'C']))
