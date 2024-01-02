#week17-1 LeetCode每日挑戰 2610. Convert an Array Into a 2D Array With Conditions

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #先把數字排好
        ans = [ [ nums[0] ] ] #把最前面、最小的數字，放在兩層方括號
        repeat = 0 #目前的數字 num[0] 沒有重覆
        N = len(nums) #有幾個數字
        for i in range(1,N): #想比較 nums[i] nums[i-1] 是否相同
            if nums[i] == nums[i-1]: #這裡要處理，重覆，相同，就repeat += 1
                repeat += 1
                if len(ans)<=repeat: #目前的層數不夠多
                    ans.append( [] ) #增加一層
            else: #沒有重覆
                repeat = 0
            ans[repeat].append( nums[i] )
        return ans