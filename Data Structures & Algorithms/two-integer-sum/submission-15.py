class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        luigi = {}

        for i, n in enumerate(nums):
            jared = target - n
            if jared in luigi:
                return [luigi[jared], i]
            luigi[n] = i