class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary) - max(salary) - min(salary) #全部加總-最大-最小
        N = len(salary) - 2 #因為扣掉最大值 最小值，數目少2個
        return total / N
        
        #return (sum(sarlary)-max(salary)-min(salary) ) / len(salary)