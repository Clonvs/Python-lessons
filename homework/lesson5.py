# Семинар 5


# 1) Сделать игру морской бой

# from random import randint
# board = []
# for x in range(6):
#     board.append(["O"] * 6)
# def print_board(board):
#     for row in board:
#         print((" ").join(row)) 
# def random_row(board):
#     return randint(0, len(board) - 1) 
# def random_col(board):
#     return randint(0, len(board[0]) - 1) 
# print("\nНачнем игру в Морской бой!\nу вас 10 попыток:")
# print_board(board)
# ship_row = random_row(board) 
# ship_col = random_col(board)
# for turn in range(10): 
#     print ("Ход: ", turn)
#     guess_row = int(input("Введите номер строки 0-5: ")) 
#     guess_col = int(input("Введите номер столбца 0-5: ")) 
#     if guess_row == ship_row and guess_col == ship_col: 
#         board[ship_row][ship_col] = "*" 
#         print_board(board)
#         print("Корабль подбит!"  )
#         break
#     else:
#         if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
#             print("Таких координат нет")
#         elif(board[guess_row][guess_col] == "X"): 
#             print("Эти координаты вы уже называли.")
#         else:
#             print("Мимо!")
#             board[guess_row][guess_col] = "X" 
#     if turn == 9:
#         print("Игра окончена!") 
#     print_board(board)