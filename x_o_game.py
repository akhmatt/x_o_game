board = list(range(1, 10))

def show_board():  # отображение поля игры
    for i in range(3):
        print(board[0+i*3], board[1+i*3], board[2+i*3]) #выводит в консоль по 3 элемента из списка board на каждом шагу  цикла for



def take(choise): # ввод
    while True:
        value = input('Куда поставить - ' + choise + '?')
        if not (value in '123456789'):
            print('Неверный ввод. Введите заново')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO': # проверка на занятость клетки
            print("место занято")
            continue
        board[value-1] = choise
        break

wins_vars = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def win(): # проверка выигрыша
    for j in wins_vars:
        if board[j[0] - 1] == (board[j[1] - 1]) == (board[j[2] - 1]): #сначала я тут все три случая взял в скобки и игра запускалась но не понимала выигрышей, поискал в инете и понял что проверяется на равенство первая и вторая позиция (board[j[0] - 1] == (board[j[1] - 1])). Выражение принимает значения true or false соответственно, а затем результат, то есть одно из булевых значений, сравнивается с третьей позицией, поэтому программа не понимает, когда кто-то выиграл.
            return board[j[1]-1]
    else:
        return False


def main_func():
    counter = 0 # переменная подсчета ходов 
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

