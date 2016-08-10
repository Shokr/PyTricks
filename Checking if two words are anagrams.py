# Trick [8]: Checking if two words are anagrams

from collections import Counter

def is_anagram(str1, str2):
    """Checks whether the words are anagrams.
    word1: string
    word2: string
    returns: boolean
    """
    return Counter(str1) == Counter(str2)

print("is_anagram? ", is_anagram('abcd','dbca'))

print("  ")
