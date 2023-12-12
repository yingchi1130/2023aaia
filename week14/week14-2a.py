#每日挑戰 2023-12-01 把字串 .join() 起來, 看他們是否相同
# LeetCode 1662. Check If Two String Arrays are Equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ''.join(word1) 
        b = ''.join(word2)  

        if a==b: return True
        else: return False