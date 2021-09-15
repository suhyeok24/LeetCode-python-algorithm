class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #import collections
        anagram=collections.defaultdict(list)
        for str in strs:
            anagram["".join(sorted(str))].append(str)
        #for value in anagram.values():
        #   value=value.sort()
        return list(anagram.values())
