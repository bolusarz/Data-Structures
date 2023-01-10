# Longest Substring with Same Letters after Replacement

def length_of_longest_substring(s, k):
    maxRepeatCount, window_start, max_len = 0, 0, 0
    mem = {}

    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char not in mem:
            mem[right_char] = 1
        else:
            mem[right_char] += 1

        maxRepeatCount = max(maxRepeatCount, mem[right_char])

        if window_end - window_start + 1 - maxRepeatCount > k:
            left_char = s[window_start]
            mem[left_char] -= 1
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    return max_len


print(length_of_longest_substring("aabccbb", 2))
