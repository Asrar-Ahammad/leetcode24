from collections import Counter
import math

def minOperations(nums):
    count = Counter(nums)
    n=0
    # for i in count:
    #     if count[i]%3 == 0:
    #         n = n+(count[i]/3)
    #         continue
    #     elif(count[i]%2 == 0):
    #         n = n+(count[i]/2)
    #     else:
    #         return -1
    for c in count.values():
            if c == 1: 
                return -1
            n += math.ceil(c / 3)
    return int(n)


nums = [2, 3, 3, 2, 2, 4, 2, 3, 4]
# nums = [2, 1, 2, 2, 3, 3]
# nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]
print(minOperations(nums))
