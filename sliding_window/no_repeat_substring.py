
# def no_repeat_substring(s):
#     mem = {}
#     window_start, max_len = 0, 0
#
#     for window_end in range(len(s)):
#         if s[window_end] in mem:
#             mem[s[window_end]] += 1
#         else:
#             mem[s[window_end]] = 1
#
#         while mem[s[window_end]] > 1:
#             mem[s[window_end]] -= 1
#
#             if mem[s[window_end]] == 0:
#                 del mem[s[window_end]]
#
#             window_start += 1
#
#         max_len = max(max_len, window_end - window_start + 1)
#
#     return max_len

def no_repeat_substring(s):
    mem = {}
    window_start, max_len = 0, 0

    for window_end in range(len(s)):
        char = s[window_end]
        if char in mem:
            window_start = max(window_start, mem[char] + 1)

        mem[char] = window_end
        max_len = max(max_len, window_end - window_start + 1)

    return max_len


print(no_repeat_substring("aabccbb"))
print(no_repeat_substring("abbbb"))
print(no_repeat_substring("abccde"))
