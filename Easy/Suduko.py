"""Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true


nicetry=[[1,2,3,1], [5,6,7,8]]


"""

def checkRows(row):
    
    for item in row:
        checkList=[]
        nums=0
        print(item)
        for nums in range(len(row[nums])):
            if item[nums].isdigit() and 1 <= int(item[nums]) <= 9:            
                
                if item[nums] in checkList:
                    print("dupe")
                    return False
                
                checkList.append(item[nums])   
            else:
                print("ignore") 
        
def checkColumns(self, column: list[list[str]]) -> bool:

def checkSquares(self, square: list[list[str]]) -> bool:





class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        