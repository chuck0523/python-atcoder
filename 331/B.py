import math

def main():
    n, s, m, l = map(int, input().split())

    # サイズと単価のリストを作成
    data = [
        {'size': 's', 'unit_price': s / 6},
        {'size': 'm', 'unit_price': m / 8},
        {'size': 'l', 'unit_price': l / 12}
    ]
    # コスパ順にソート
    data = sorted(data, key=lambda x: x['unit_price'])


    cnt = n
    result = 0

    for i in range(len(data)):
        if cnt <= 0:
            break

        row = data[i]
        if row['size'] == 's':
            count = math.floor(n / 6)
            result += s * count
            cnt -= count * 6
            print(f"Sサイズを{count}パック({count * 6}個)買いました。残り{cnt}個です。")

        if row['size'] == 'm':
            count = math.floor(n / 8)
            result += m * count
            cnt -= count * 8
            print(f"Mサイズを{count}パック({count * 8}個)買いました。残り{cnt}個です。")

        if row['size'] == 'l':
            count = math.floor(n / 12)
            result += l * count
            cnt -= count * 12
            print(f"Lサイズを{count}パック({count * 12}個)買いました。残り{cnt}個です。")

    print(result)

main()