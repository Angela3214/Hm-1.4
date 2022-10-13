import grid
import minmax

def computer_step(g):
    n = g.n #Лучше назвать size например
    for i in range(n): #Вместо i, j лучше использовать названия например row, col
        for j in range(n):
            if g.get(i, j) == grid.CELL_EMPTY:
                g.set(i, j, grid.CELL_COMPUTER)
                result = minmax.player_wins(g)
                if not result:
                    return
                g.set(i, j, grid.CELL_EMPTY)
    for i in range(n): #аналогично
        for j in range(n):
            if g.get(i, j) == grid.CELL_EMPTY:
                g.set(i, j, grid.CELL_COMPUTER)
                return

def player_step(g):
    print(g.draw())
    while True: #Лучше использовать флаги вместо while true (например пока флаг true)
        i, j = list(map(int, input("Enter row and column: ").split(' ')))
        i, j = i - 1, j - 1
        if g.valid_coords(i, j) and g.get(i, j) == grid.CELL_EMPTY:
            g.set(i, j, grid.CELL_PLAYER)
            break #Тогда и break тут не пригодится
        else:
            print('Invalid coordinates!')

def main():
    n = int(input("Enter grid size: ")) # Лучше использовать более понятные названия переменных: grid_size
    g = grid.Grid(n) #Тогда здесь лучше grid_class_obj
    empty_cells = n * n #grid_size * grid_size
    # Лучше использовать флаги вместо while true (например пока флаг true)
    while True: #Лучше ине дублировать код, а использовать else и флаги
        computer_step(g) #Имя переменной (как указано выше)
        if g.who_won() == grid.COMPUTER_WON:
            print('Computer won!')
            return
        empty_cells -= 1
        if empty_cells == 0:
            print('Neither won!')
            return
        player_step(g)
        if g.who_won() == grid.PLAYER_WON:
            print('Player won!')
            return
        empty_cells -= 1
        if empty_cells == 0:
            print('Neither won!')
            return

if __name__ == '__main__':
    main()