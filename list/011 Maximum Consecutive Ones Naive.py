def maxConsecutiveOnes(arr, n):
    res = 0

    for i in range(0, n):

        curr = 0

        for j in range(i, n):

            if arr[j] == 1:
                curr += 1

            else:
                break

        res = max(res, curr)

    return res


if __name__ == "__main__":
    arr = [0, 1, 1, 1, 0, 1, 1]
    n = len(arr)

    print(maxConsecutiveOnes(arr, n))
