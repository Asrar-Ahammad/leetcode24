from typing import List


def min_falling_pathSum(matrix: List[List[int]]) -> int:
    # My Solution
    # min_val_index = matrix[0].index(min(matrix[0]))
    # i = 1
    # sum = min(matrix[0])
    # print(sum)
    # prev, cur, nex = 0, 0, 0
    # while i < len(matrix):
    #     cur = matrix[i][min_val_index]
    #
    #     if min_val_index - 1 >= 0:
    #         prev = matrix[i][min_val_index - 1]
    #     else:
    #         prev = float('inf')
    #     if min_val_index + 1 < len(matrix[i]):
    #         nex = matrix[i][min_val_index + 1]
    #     else:
    #         nex = float('inf')
    #     print(min(prev, cur, nex))
    #     sum += (min(prev, cur, nex))
    #     min_val_index = matrix[i].index(min(prev, cur, nex))
    #     i += 1
    # return sum

    # Solution
    N = len(matrix)
    for r in range(1,N):
        for c in range(N):
            mid = matrix[r-1][c]
            left = matrix[r-1][c-1] if c>0 else float('inf')
            right = matrix[r-1][c+1] if c<N-1 else float('inf')
            matrix[r][c] = matrix[r][c]+min(mid,left,right)
    return min(matrix[-1])


# print(min_falling_pathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
# print(min_falling_pathSum(matrix=[[-19, 57], [-40, -5]]))
# print(min_falling_pathSum(matrix=[[17, 82], [1, -44]]))
print(min_falling_pathSum(matrix=[[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]])) # Correct o/p : -36


# solution
# def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#     M = len(matrix)
#     N = len(matrix[0])
#
#     prevRow = matrix[0][:]  # Initialize with the first row
#
#     for r in range(1, M):
#         currRow = [0] * N
#         for c in range(N):
#             curr = matrix[r][c]
#             top = curr + prevRow[c]
#             topL = curr + prevRow[c - 1] if c > 0 else float('inf')
#             topR = curr + prevRow[c + 1] if c < N - 1 else float('inf')
#             currRow[c] = min(top, topL, topR)
#
#         prevRow = currRow  # Update the previous row with the current row
#
#     return min(prevRow)