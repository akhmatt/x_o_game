board = list(range(1, 10))

def show_board():  # отображение поля игры
    for i in range(3):
        print(board[0+i*3], board[1+i*3], board[2+i*3])



def take(choise): # ввод
    while True:
        value = input('Куда поставить - ' + choise + '?')
        if not (value in '123456789'):
            print('Неверный ввод. Введите заново')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print("место занято")
            continue
        board[value-1] = choise
        break

wins_vars = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def win(): # проверка выигрыша
    for j in wins_vars:
        if board[j[0] - 1] == (board[j[1] - 1]) == (board[j[2] - 1]):
            return board[j[1]-1]
    else:
        return False


def main_func():
    counter = 0
    while True:
        show_board()
        if counter % 2 == 0:
            take('X')
        else:
            take('O')
        if counter > 3:
            winner = win()
            if winner:
                show_board()
                print(winner, 'Победил!')
                break
        counter += 1
        if counter > 8:
            show_board()
            print('Ничья!')
            break

main_func()

