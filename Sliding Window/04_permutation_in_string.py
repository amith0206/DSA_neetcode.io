'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 
Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count={}
        s2count={}
        sub_string=[]

      #Counter function returns a dictionary having all characters as keys and occurences of corresponding character as values
        s1count=Counter(s1)
        for i in range(len(s2)):
            sub_string.append(s2[i:i+len(s1)])
        for string in sub_string:
            s2count=Counter(string)
            if s1count == s2count:
                return True
        return False
