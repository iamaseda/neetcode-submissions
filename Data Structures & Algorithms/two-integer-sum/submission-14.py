class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {val: i for i, val in enumerate(nums)}
        
        for i in range(len(nums)):
            if (target - nums[i] in vals):
                if i != vals[target - nums[i]]:
                    return [i, vals[target - nums[i]]]
        