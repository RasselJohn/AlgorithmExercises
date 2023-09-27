# Given two strings s and goal, return true if you can swap two letters in s
# so the result is equal to goal, otherwise, return false.
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j
# and swapping the characters at s[i] and s[j].
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
#
# Example 1:
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
#
# Example 2:
# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
#
# Example 3:
# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
#
# Constraints:
#
# 1 <= s.length, goal.length <= 2 * 104
# s and goal consist of lowercase letters.

def buddy_strings(s: str, g: str) -> bool:
    s_len = len(s)
    g_len = len(g)

    if s_len == 1 or s_len != g_len:
        return False

    s_set_len = len(set(s))
    g_set_len = len(set(g))
    if s_set_len != g_set_len:
        return False

    if s == g:
        return s_set_len == 1 or s_len != s_set_len

    f1 = f2 = -1
    s1 = s2 = -1

    for ch1, ch2 in zip(s, g):
        if ch1 != ch2:
            if f1 == -1:
                f1, s1 = ch1, ch2
            elif f2 == -1:
                f2, s2 = ch1, ch2
            else:
                return False

    if f1 == -1 or f2 == -1:
        return False

    return f1 == s2 and f2 == s1
