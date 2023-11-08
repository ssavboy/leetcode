# O(n2)
class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        substring = str()
        length = list()
        if string == '': return 0
        for i in range(len(string)):
            for j in range(i, len(string)):
                if string[j] not in substring:
                    substring += string[j]
                else:
                    break
            length.append(len(substring))
            substring = ''
        return max(length)