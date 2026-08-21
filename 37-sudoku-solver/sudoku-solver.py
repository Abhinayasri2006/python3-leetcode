class Solution(object):
    def solveSudoku(self, board):
        h_row = [set() for i in range(9)]
        h_col = [set() for i in range(9)]
        h_box = [set() for i in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    h_row[r].add(board[r][c])
                    h_col[c].add(board[r][c])
                    formula = ((r // 3) * 3) + (c // 3)
                    h_box[formula].add(board[r][c])
                else:
                    empty.append((r, c))

        def backtracking(index):
            if index == len(empty):
                return True

            r, c = empty[index]
            formula = ((r // 3) * 3) + (c // 3)

            for val in "123456789":
                if (val not in h_row[r] and
                    val not in h_col[c] and
                    val not in h_box[formula]):

                    board[r][c] = val
                    h_row[r].add(val)
                    h_col[c].add(val)
                    h_box[formula].add(val)

                    if backtracking(index + 1):
                        return True

                    board[r][c] = "."
                    h_row[r].remove(val)
                    h_col[c].remove(val)
                    h_box[formula].remove(val)

            return False

        backtracking(0)
    
