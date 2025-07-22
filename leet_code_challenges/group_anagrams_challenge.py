from typing import List;
from collections import defaultdict;

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = []

        tab = defaultdict(list)

        for s in strs:
            char_feq = [0 for _ in range(26)]
            for c in s:
                char_feq[ord(c)-97]+=1
            tab["".join([chr(idx+97)+str(f) for idx,f in enumerate(char_feq)])].append(s)

        for value in tab.values():
            op.append(value)
        return op


input = ["bdddddddddd","bbbbbbbbbbc"]


print(Solution().groupAnagrams(input))

