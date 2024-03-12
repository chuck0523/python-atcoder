def main():
    h, w, n = map(int, input().split())
    moves = input()
    grid = [input() for _ in range(h)]

    answer = 0

    # 探索
    for i in range(h):
        for j in range(w):
            # 外周はスキップ
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                continue

            # 不時着失敗
            if grid[i][j] == '#':
                continue

            # 移動
            pos = [i, j]
            for move in moves:
                if move == 'U':
                    pos[0] -= 1
                if move == 'D':
                    pos[0] += 1
                if move == 'L':
                    pos[1] -= 1
                if move == 'R':
                    pos[1] += 1
                if grid[pos[0]][pos[1]] == '#':
                    pos = [0, 0]
                    break

            # エリア外
            if pos[0] < 0 or pos[0] >= h or pos[1] < 0 or pos[1] >= w:
                continue

            # 正解ルート
            if grid[pos[0]][pos[1]] == '.':
                answer += 1

    print(answer)

main()