distances = {
    'AB': 1,
    'AC': 2,
    'AD': 2,
    'AE': 1,
    'BC': 1,
    'BD': 2,
    'BE': 2,
    'CD': 1,
    'CE': 2,
    'DE': 1
}

def main():
    s = "".join(sorted(input()))
    t = "".join(sorted(input()))

    if distances[s] == distances[t]:
        print("Yes")
    else:
        print("No")

main()