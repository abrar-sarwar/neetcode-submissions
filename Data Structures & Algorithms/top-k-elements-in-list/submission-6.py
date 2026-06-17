class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       joey = {}
       john = [[] for i in range(len(nums) + 1)]

       for num in nums:
            joey[num] = 1 + joey.get(num, 0)
       for num,jared in joey.items():
            john[jared].append(num)
            
       kevin = []

       for i in range(len(john) - 1, 0, -1):
            for num in john[i]:
                kevin.append(num)
                if len(kevin) == k:
                    return kevin