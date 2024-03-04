def main():
    k, g, m = map(int, input().split())

    g_temp, m_temp = 0, 0
    for _ in range(0, k):
        # 1. グラスがいっぱい
        if g_temp == g:
            g_temp = 0
            continue

        # 2. マグカップが空
        if m_temp == 0:
            m_temp = m
            continue

        # 3. マグカップからグラスに移す
        gap = min(g - g_temp, m_temp)
        g_temp += gap
        m_temp -= gap

    print(g_temp, m_temp)

main()