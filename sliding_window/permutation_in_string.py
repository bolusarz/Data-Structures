import math


def find_permutation(s, pattern):
    window_start = 0
    mem = {}
    pattern_mem = {}

    for char in pattern:
        if char in pattern_mem:
            pattern_mem[char] += 1
        else:
            pattern_mem[char] = 1

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in pattern:
            if right_char in mem:
                mem[right_char] += 1
            else:
                mem[right_char] = 1

            while mem[right_char] > pattern_mem[right_char]:
                mem[s[window_start]] -= 1
                window_start += 1
        else:
            mem.clear()
            window_start = window_end + 1

        if window_end - window_start + 1 == len(pattern):
            return True
        math.inf

    return False


print(find_permutation("odicf", "dc"))
