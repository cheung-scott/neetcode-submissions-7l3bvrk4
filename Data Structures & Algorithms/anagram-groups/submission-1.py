class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for n in strs:
            count = [0] * 26

            for x in n:
                count[ord(x) - ord("a")] +=1

            output[tuple(count)].append(n)
        return list(output.values())



