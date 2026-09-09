class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = defaultdict(list)

        for str in strs:
            sortedS = ''.join(sorted(str))
            sortedMap[sortedS].append(str)

        return list(sortedMap.values())


        