class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            _l = {}
            _l = {str(item): 0 for item in range(1, 10)}
            k = 0
            while k < 9:
                if board[i][k] != '.':
                    _l[board[i][k]] += 1
                    if _l[board[i][k]] > 1:
                        return False
                k = k + 1
        for j in range(9):
            _l = {}
            _l = {str(item): 0 for item in range(1, 10)}
            k = 0
            while k < 9:
                if board[k][j] != '.':
                    _l[board[k][j]] += 1
                    if _l[board[k][j]] > 1:
                        return False
                k = k + 1
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                _l = {}
                _l = {str(item): 0 for item in range(1, 10)}
                for r in range(3):
                    for c in range(3):
                        if board[i + r][j + c] != '.':
                            _l[board[i + r][j + c]] += 1
                            if _l[board[i + r][j + c]] > 1:
                                return False   
        return True