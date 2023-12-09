# Given a string s, find the length of the longest
# substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

def length_of_longest_substring(s: str) -> int:
    """
    Doc tests:
    >>> length_of_longest_substring("abcabcbb")
    3
    >>> length_of_longest_substring("bbbbb")
    1
    >>> length_of_longest_substring("pwwkew")
    3
    >>> length_of_longest_substring("aa")
    1
    >>> length_of_longest_substring("au")
    2
    >>> length_of_longest_substring("aab")
    2
    >>> length_of_longest_substring("dvdf")
    3
    """
    if (len_s := len(s)) < 2:
        return len_s

    curr_substr = []
    result_substr = []

    while s:
        curr_substr.append(s[0])

        for ch in s[1:]:
            if ch in curr_substr:
                break

            curr_substr.append(ch)

        if len(result_substr) < len(curr_substr):
            result_substr = curr_substr[:]

        curr_substr.clear()
        s = s[1:]

    return len(result_substr)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
