# Семинар 6

# 1) Сделать игру морской бой

from random import randint
comp_board = []
user_board = []
for x in range(6):
    comp_board.append(["O"] * 6)
def print_board(comp_board):
    for row in comp_board:
        print((" ").join(row)) 
for x in range(6):
    user_board.append(["O"] * 6)
def print_board(user_board):
    for row in user_board:
        print((" ").join(row)) 
def random_row(comp_board):
    return randint(0, len(comp_board) - 1) 
def random_col(board):
    return randint(0, len(comp_board[0]) - 1) 
def random_row(user_board):
    return randint(0, len(user_board) - 1) 
def random_col(user_board):
    return randint(0, len(user_board[0]) - 1) 
print("\nНачнем игру в Морской бой!\nу вас 10 попыток:")

ship_row = random_row(comp_board) 
ship_col = random_col(comp_board)

for turn in range(10): 
    print ("Ход компьтера: ", turn)
    guess_row = randint(0, len(comp_board) - 1) 
    guess_col = randint(0, len(comp_board[0]) - 1) 
    print(guess_row, guess_col)
    if guess_row == ship_row and guess_col == ship_col: 
        comp_board[ship_row][ship_col] = "*" 
        print_board(comp_board)
        print("Корабль подбит, компьютер win!"  )
        break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print("Таких координат нет")
        elif(comp_board[guess_row][guess_col] == "X"): 
            print("Эти координаты вы уже называли.")
        else:
            print("Мимо!")
            comp_board[guess_row][guess_col] = "X" 
    if turn == 9:
        print("Ходов больше нет, игра окончена!") 
    print_board(comp_board)

    print ("Ход игрока: ", turn)
    guess_row = int(input("Введите номер строки 0-5: ")) 
    guess_col = int(input("Введите номер столбца 0-5: ")) 
    if guess_row == ship_row and guess_col == ship_col: 
        user_board[ship_row][ship_col] = "*" 
        print_board(user_board)
        print("Корабль подбит, игрок win!"  )
        break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print("Таких координат нет")
        elif(user_board[guess_row][guess_col] == "X"): 
            print("Эти координаты вы уже называли.")
        else:
            print("Мимо!")
            user_board[guess_row][guess_col] = "X" 
    if turn == 9:
        print("Ходов больше нет, конец игры!") 
    print_board(comp_board)
    print('-' * 11)
    print_board(user_board)
