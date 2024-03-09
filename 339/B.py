def main():
    h, w, n = map(int, input().split())

    # 初期グリッド作成
    grid = [['.' for _ in range(w)] for _ in range(h)]

    # 位置と方向
    pos = [0,0]
    dir = 0

    for _ in range(n):
        current = grid[pos[1]][pos[0]]

        # 塗る
        if current == '.':
            grid[pos[1]][pos[0]] = '#'
            dir = dir + 90 if dir < 270 else 0
        else:
            grid[pos[1]][pos[0]] = '.'
            dir = dir - 90 if dir > 0 else 270

        # 移動
        if dir == 0:
            next_y = pos[1]-1 if pos[1] > 0 else h-1
            pos = [pos[0], next_y]
        elif dir == 90:
            next_x = pos[0]+1 if pos[0] < w-1 else 0
            pos = [next_x, pos[1]]
        elif dir == 180:
            next_y = pos[1]+1 if pos[1] < h-1 else 0
            pos = [pos[0], next_y]
        elif dir == 270:
            next_x = pos[0]-1 if pos[0] > 0 else w-1
            pos = [next_x, pos[1]]

    print('\n'.join([''.join(row) for row in grid]))

main()