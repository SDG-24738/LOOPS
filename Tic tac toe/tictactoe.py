TheBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' , 
            '1': ' ' , '2': ' ' , '3': ' ' }
board_keys = []
for key in TheBoard:
    board_keys.append(key)
def printBoard(board):
    print(board['7'] +  '|' + board['8'] + '|' + board['9'])
    print('_+_+_')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('_+_+_')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def game():
    turn = 'x'
    count = 0
    for i in range(10):
        printBoard(TheBoard)
        print("It's your turn." + turn + ".Move to which place?")
        move = input()
        if TheBoard[move] == ' ':
            TheBoard[move] = turn
            count = count + 1
        else:
            print("That place is aldready filled, \nMove to which place?")
            continue
        if count >= 5:
            if TheBoard['7'] == TheBoard['8'] == TheBoard['9'] !=
            if count >= 5:

if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top

printBoard(theBoard)

print("\nGame Over.\n")

print(" **** " +turn + " won. ****")

break

elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle

printBoard(theBoard)

print("\nGame Over.\n")

print(" **** " +turn + " won. ****")

break

elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom

printBoard(theBoard)

print("\nGame Over.\n")

print(" **** " +turn + " won. ****")

break

elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side

printBoard(theBoard)

print("\nGame Over.\n")

print(" **** " +turn + " won. ****")

break

elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle

printBoard(theBoard)

print("\nGame Over.\n")

print(" **** " +turn + " won. ****")

break

elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side

printBoard(theBoard)

print("\nGame Over.\n")

print(" **** " +turn + " won. ****")

break

elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal

printBoard(theBoard)

print("\nGame Over.\n")

print(" **** " +turn + " won. ****")

break

elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 

printBoard(theBoard)

print("\nGame Over.\n")

print(" **** " +turn + " won. ****")

break



if count == 9:

print("\nGame Over.\n")

print("It's a Tie!!")



if turn =='X':

turn = 'O'

else:

turn = 'X'



restart = input("Do want to play Again?(y/n)")

if restart == "y" or restart == "Y":

for key in board_keys:

theBoard[key] = " "

game()

if __name__ == "__main__":

game()