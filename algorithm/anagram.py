from collections import Counter


def are_anagrams(s1, s2):
    """
    Basic solution using hash tables
    Time complexity: O(n)
    Space Complexity: O(n)
    """
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}

    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False

    return True


def are_anagrams2(s1, s2):
    """
    Basic solution with hash table reducing the line of code
    Time complexity: O(n)
    Space Complexity: O(n)
    """
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}

    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    return freq1 == freq2


def are_anagrams3(s1, s2):
    """
    Shorter version of anagrams using Counter function
    Time complexity: O(n)
    Space Complexity: O(n)
    :param s1:
    :param s2:
    :return: boolean
    """
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


def are_anagrams4(s1, s2):
    """
    Using sorting to check if they are anagrams
    Time complexity: O(nlog(n))
    Space Complexity: O(n)
    :param s1:
    :param s2:
    :return:
    """

    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def main():
    s1 = 'triangle'
    s2 = 'integral'

    print(f'{s2} is {"an anagram" if are_anagrams4(s1, s2) else "not an anagram"} of {s1}')


main()
