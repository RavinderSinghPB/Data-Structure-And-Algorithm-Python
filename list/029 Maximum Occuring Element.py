def maxOcc(L, R, n):
    arr = [0] * 1000

    for i in range(n):
        arr[L[i]] += 1
        arr[R[i] + 1] -= 1

    maxm = arr[0]
    res = 0

    for i in range(1, 1000):
        arr[i] += arr[i - 1]

        if maxm < arr[i]:
            maxm = arr[i]
            res = i

    return res


if __name__ == "__main__":
    L = [1, 2, 3]
    R = [3, 5, 7]
    n = 3

    print(maxOcc(L, R, n))
