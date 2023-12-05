#191. Number of 1 Bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0 # 迴圈前面 ans=0

        while n>0: # 要把 n剝光光
            ans += n%2 # 撥下來的皮
            n = n//2 # n 撥完就變小了

        return ans # 迴圈後面 ans 拿來用