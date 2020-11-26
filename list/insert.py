def insertele(arr, n, x, cap, pos):
    if n == cap:
        return n

    idx = pos - 1

    i = n - 1
    while i >= idx:
        arr[i + 1] = arr[i]
        i -= 1

    arr[idx] = x

    return n + 1


def main():
    arr = [0] * 5
    cap, n = 5, 3

    arr[0], arr[1], arr[2] = 5, 10, 20

    print('before insertion')

    for i in range(n):
        print(arr[i], end=' ')
    print()

    x = 7
    pos = 2
    n = insertele(arr, n, x, cap, pos)

    print('after insertion')

    for i in range(n):
        print(arr[i], end=' ')


main()
