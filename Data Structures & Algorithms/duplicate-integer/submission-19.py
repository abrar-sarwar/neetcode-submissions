class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = set()
        for num in nums:
            
            if num in test:
                return True
            test.add(num)
        return False