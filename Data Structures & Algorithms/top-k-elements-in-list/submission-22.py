class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kevin = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            kevin[num] = 1 + kevin.get(num, 0)
        for num,cnt in kevin.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res