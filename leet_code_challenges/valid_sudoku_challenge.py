from typing import List;
from collections import defaultdict;

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0,9):
            visited = defaultdict(bool)
            for j in range(0,9):
                val = board[i][j]
                if val != ".":
                    if visited[val]:
                        return False
                    visited[val] = True

            visited = defaultdict(bool)
            for k in range(0,9):
                val = board[k][i]
                if val != ".":
                    if visited[val]:
                        return False
                    visited[val] = True


        for r in range(0,9,3):
            for c in range(0,9,3):
                visited = defaultdict(bool)
                for i in range(c,c+3):
                    for j in range(r,r+3):
                        val = board[i][j]
                        if val != ".":
                            if visited[val]:
                                return False
                            visited[val] = True
        return True






input = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(input))