
grid = [
    [0,9,4,5,8,3,2,1,6],
    [8,0,6,7,2,1,4,9,5],
    [1,5,0,4,9,6,7,8,3],
    [0,0,7,0,4,0,2,0,0],
    [4,2,7,3,1,9,5,0,8],
    [9,0,4,9,6,0,0,0,5],
    [0,7,0,8,0,0,0,1,2],
    [1,2,0,1,0,7,4,0,0],
    [0,4,9,6,0,6,0,0,7]
]



##########################################
#
# print sudoku grid
#
##########################################

def print_sudoku_board(board):
    print_sudoku(board)

def print_sudoku(board):
    print("-"*37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("."*37)
        elif i % 3 == 2:
            print("|" + "---+"*8 + "---|")
        else:
            print("|" + "   +"*8 + "   |")




##########################################
#
# Solve sudoku grid
#
##########################################


def solve_sudoku(board):

    #
    #       Step 1 :
    #       check for last free cell
    #

    last_free_cell(board)



def last_free_cell(board):
    for i in range(len(board)):
        check_last_free_cell(i,board[i])



def check_last_free_cell(i,r):
    if(r.count(0)==1):
        index = r.index(0)
        for k in range(1,10):
            if(r.count(k)!=1):
                grid[i][index] = k
                print(f"\nUsing Last Free Cell Method..")
                print(f"Found {k} at {i+1} row @ {index+1} position")
                print_sudoku_board(grid)





##########################################
#
# Call the Program to solve it
#
##########################################

print_sudoku_board(grid)
solve_sudoku(grid)
print(f'Sudoku solved till now')
print_sudoku(grid)
