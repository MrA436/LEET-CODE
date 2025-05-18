class Solution(object):
    def twoSum(self, nums, target):
        for pos_x in range(len(nums)): 
            # Iterating over every element in Nums list
            for pos_y in range(pos_x+1, len(nums)): 
                # For every element in Nums List , iterating over other Numbers except self. 
                if nums[pos_x] + nums[pos_y] == target: 
                    # if x + y == target
                    return [pos_x, pos_y] 
                    # return the position of Number x and y
                    
                    
sol= Solution()
nums=[1,5,7,3]
target= 4

result = sol.twoSum(nums, target)
print(result)

# solved using brute force method
