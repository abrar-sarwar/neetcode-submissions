class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        test = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for n in s:
                count[ord(n) - ord('a')] += 1
            test[tuple(count)].append(s)
        return list(test.values())