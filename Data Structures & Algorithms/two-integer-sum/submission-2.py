class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0;
        end = len(nums)

        while (i < (end - 1)):
            for j in range(i + 1, end):
                if (nums[i] + nums[j] == target):
                    return [i, j]
            i += 1