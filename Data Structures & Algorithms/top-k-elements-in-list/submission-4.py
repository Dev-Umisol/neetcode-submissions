class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        array = []
        for num, ct in count.items():
            array.append([ct, num])
        
        array.sort()
        result = []

        while len(result) < k:
            result.append(array.pop()[1])
        
        return result