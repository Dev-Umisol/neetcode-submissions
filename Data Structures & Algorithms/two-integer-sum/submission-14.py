class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # this starts traversal from index 0
            for j in range(i + 1, len(nums)): # this starts traversal from index 1
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []