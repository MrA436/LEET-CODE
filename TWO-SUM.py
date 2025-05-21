class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):# iterating every element
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target: # adding the value of i and j to check if it equals to target
                    return [i, j] # returning the value of i and j

''' 
used my own logic this time
'''
