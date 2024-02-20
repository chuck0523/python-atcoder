def main():
    S = input()

    Dict = {}

    for i in range(len(S)):
        if S[i] in Dict:
            Dict[S[i]] += 1
        else:
            Dict[S[i]] = 1

    result = ""

    for key in Dict:
        # 初回
        if result == "":
            result = key
        # 数値が大きいので更新
        if Dict[key] > Dict[result]:
            result = key
        # 同値だが、文字コードが小さいので更新
        if Dict[key] == Dict[result] and key < result:
            result = key

    print(result)

main()