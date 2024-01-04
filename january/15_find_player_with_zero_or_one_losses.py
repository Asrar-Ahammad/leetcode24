from typing import List

def findWinners(matches: List[List[int]]):
    count = {}
    j = 0
    for i in matches:
        if i[0] not in count:
            count[i[0]] = [1,0]
        else:
            count[i[0]][0]+=1
        if i[1] not in count:
            count[i[1]] = [0,1]
        else:
            count[i[1]][1]+=1
    winner = []
    one_match = []
    for i in count:
        if count[i][1]==0:
            winner.append(i)
        if count[i][1] == 1:
            one_match.append(i)
    winner.sort()
    one_match.sort()
    return [winner,one_match]

print(findWinners(matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))