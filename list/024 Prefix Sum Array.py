def preSum(arr, n, prefix_sum):
    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]


def getSum(prefix_sum, l, r):
    if l != 0:
        return prefix_sum[r] - prefix_sum[l - 1]
    else:
        return prefix_sum[r]


if __name__ == "__main__":
    arr = [2, 8, 3, 9, 6, 5, 4]
    n = len(arr)
    k = 3

    prefix_sum = [0] * 1000

    preSum(arr, n, prefix_sum)

    print(getSum(prefix_sum, 1, 3))
    print(getSum(prefix_sum, 0, 2))
