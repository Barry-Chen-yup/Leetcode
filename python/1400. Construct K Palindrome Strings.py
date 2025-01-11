class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        """
        1. If k > length of s, return False.
        2. Initialize odd_count = 0 and char_count[26] to all zeros.
        3. For each character in s:
            a. Increment the corresponding count in char_count.
            b. If the count is odd, increment odd_count.
                Else, decrement odd_count.
        4. Return True if odd_count <= k, else return False.
        """
        if k > len(s):
            return False
        char_count = [0]*26
        ood_count = 0
        for char in s:
            char_count[ord(char)-ord('a')] += 1
            if char_count[ord(char)-ord('a')] % 2 == 1:
                ood_count += 1
            else:
                ood_count -= 1
        return ood_count<=k
