class Solution:
    def search(self, nums: List[int], target: int) -> int:
        path = []
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            value_at_mid = nums[mid]
            path.append(value_at_mid)
        
            if target == value_at_mid:
                return mid
            elif target > value_at_mid:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
