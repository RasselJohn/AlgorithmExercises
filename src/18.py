# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

def is_anagram(str1: str, str2: str) -> bool:
    chars = {}
    for ch in str1:
        chars[ch] = chars[ch] + 1 if ch in chars else 1

    for ch in str2:
        if ch not in chars:
            return False

        chars[ch] -= 1
        if chars[ch] == 0:
            del chars[ch]

    return not bool(chars)
