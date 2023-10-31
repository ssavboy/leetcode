class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for key, value in enumerate(nums):
            for index in range(key + 1, len(nums)):
                if value + nums[index] == target:
                    return [key, index]