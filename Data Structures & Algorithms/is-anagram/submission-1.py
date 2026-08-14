class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # can't do a set because there can be duplicate letters
        # hashmap letter -> number of times it appears
        # we can see if the hashmap are equal to eachother

        # check if they are the same length
        if len(s) != len(t):
            return False
        

        counts_s = {}
        counts_t = {}

        for char in s:
            counts_s[char] = counts_s.get(char, 0) + 1

        for char in t:
            counts_t[char] = counts_t.get(char, 0) + 1

        return counts_s == counts_t

        