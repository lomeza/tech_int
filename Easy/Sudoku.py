"""
Instruction:

Create a def to check whether or not a sudoku board is valid.
Board must be in 9*9 format with "." for blanks.
Board doesnt have to be solvable.

Example:

Input: board =[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

obj1=Sudoku()
obj1.isValidSudoku(board)

Output: true



"""
class Sudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #creating default dictionaries that will accept an empty set
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                #skips if these is an "."
                if (board[r][c] == "."):
                    continue
                #all the rows will be checked after they are filled, returns false if failed
                #in squares we are dividing ints by 3 to make 3*3 squares
                if (board[r][c] in rows[r] or
                    board[r][c] in columns[c] or
                    board[r][c] in squares[(r //3,  c//3)]):
                    return False
                #here is where the board is added to sets
                #col 0-8 is added from board [0][0-8]
                columns[c].add(board[r][c])
                #row 0 is added from board[0][0-8]
                rows[r].add(board[r][c])
                #the key is made of 9 squares add board [0][0-8]
                squares[(r // 3, c //3)].add(board[r][c])
        
        return True