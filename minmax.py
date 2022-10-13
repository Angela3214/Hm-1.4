import grid

cache = dict()
#Зачем дублировать точно такую же функцию? Лучше объединить их в одну
def computer_wins(g):
    g_str = g.to_str() #g_str лучше переименовать в string_grid
    if g_str in cache:
        return cache[g_str]
    verdict = g.who_won()
    if verdict == grid.COMPUTER_WON:
        cache[g_str] = True
        return True
    elif verdict == grid.PLAYER_WON:
        cache[g_str] = False
        return False
    else:
        n = g.n #переименование в size
        for i in range(n): #Аналогично с i, j, n
            for j in range(n):
                if g.get(i, j) == grid.CELL_EMPTY:
                    g.set(i, j, grid.CELL_COMPUTER)
                    result = player_wins(g)
                    g.set(i, j, grid.CELL_EMPTY)
                    if not result:
                        cache[g_str] = True
                        return True
        cache[g_str] = False
        return False

def player_wins(g):
    g_str = g.to_str() #Аналогично
    verdict = g.who_won()
    if g_str in cache:
        return not cache[g_str]
    if verdict == grid.COMPUTER_WON:
        cache[g_str] = True
        return False
    elif verdict == grid.PLAYER_WON:
        cache[g_str] = False
        return True
    else:
        n = g.n #Аналогично
        for i in range(n):
            for j in range(n):
                if g.get(i, j) == grid.CELL_EMPTY:
                    g.set(i, j, grid.CELL_PLAYER)
                    result = computer_wins(g)
                    g.set(i, j, grid.CELL_EMPTY)
                    if not result:
                        cache[g_str] = False
                        return True
        cache[g_str] = True
        return False