from typing import List

def findContentChildren( g: List[int], s: List[int]) -> int:
        i = 0
        j = 0
        count = 0
        g.sort()
        s.sort()
        while j < len(s) and i < len(g):
            if g[i] <= s[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count


# g = [1,2,3]
# s = [1,1]

g = [1,2]
s = [1,2,3]
print(findContentChildren(g, s))