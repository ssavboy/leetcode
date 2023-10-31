class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index in range(len(nums)):
            complemet = target - nums[index]
            if complemet in hashmap:
                return [hashmap[complemet], index]
            hashmap[nums[index]] = index