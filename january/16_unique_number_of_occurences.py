from typing import List


def uniqueOccurrences(arr: List[int]) -> bool:
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i]+=1
    
    arr=[]
    for i in count:
        if count[i] not in arr:
            arr.append(count[i])
        else:
            return False
    return True


print(uniqueOccurrences(arr = [1,2,2,1,1,3]))
print(uniqueOccurrences(arr = [1,2]))
print(uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))