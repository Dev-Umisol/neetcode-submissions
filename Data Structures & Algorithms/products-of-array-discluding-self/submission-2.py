class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_ct = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_ct += 1
        
        if zero_ct > 1:
            return [0] * len(nums)
        
        result = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_ct: result[i] = 0 if c else prod
            else: result[i] = prod // c
        
        return result