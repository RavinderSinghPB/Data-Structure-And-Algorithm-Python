def maxConsecutiveOnes(arr, n):
    res = 0
    curr = 0

    for i in range(0, n):

        if arr[i] == 0:
            curr = 0

        else:
            curr += 1
            res = max(res, curr)

    return res


if __name__ == "__main__":
    arr = [0, 1, 1, 0, 1, 1, 1]
    n = len(arr)

    print(maxConsecutiveOnes(arr, n))
