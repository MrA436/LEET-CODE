class Solution(object):
    def singleNumber(self, nums):
        result = 0 
        for num in nums: #iterating
            result ^= num # used XOR method
        return result
                           
                    
sol= Solution()
nums= [4,1,2,1,2]

result = sol.singleNumber(nums)
print(result)
