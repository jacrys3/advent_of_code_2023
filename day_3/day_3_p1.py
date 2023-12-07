

"""def search_bounds(bound_start_row, bound_end_row, bound_start_col, bound_end_col, num):
    for row in range(bound_start_row, bound_end_row):
        for col in range(bound_start_col, bound_end_col):
            if schematic[row][col] != '.' and not schematic[row][col].isdigit():
                print("hit!")
                return int(num)
    return 0

with open('day_3.txt') as f:
    schematic = f.readlines()

    ans = 0
    min_row = 0
    max_row = len(schematic)
    min_col = 0
    max_col = len(schematic[0])

    i = 0
    while i < max_row:
        j = 0
        while j < max_col:
            if schematic[i][j].isdigit():
                # find whole digit bounds with clamping to edges
                start_col = end_col = j
                
                while end_col < max_col and schematic[i][end_col].isdigit():
                    end_col += 1
                j = end_col
                print(schematic[i][start_col:end_col])
                print(i, start_col, end_col)
                # now we have start and end of word 

                bound_start_col = max(min_col, start_col - 1)
                bound_end_col = min(max_col, end_col + 2)
                bound_start_row = max(min_row, i - 1)
                bound_end_row = min(max_row, i + 2)
                print(bound_start_col, bound_end_col, bound_start_row, bound_end_row)

                ans += search_bounds(bound_start_row, bound_end_row, bound_start_col, bound_end_col, schematic[i][start_col:end_col])
                            
            else:
                j += 1
                
        i += 1
    print(ans)"""

# solution found online
import math as m, re

board = list(open('day_3.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))