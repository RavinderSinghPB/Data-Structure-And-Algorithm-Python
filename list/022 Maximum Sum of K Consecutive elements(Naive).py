from math import inf


def maxSum(arr, n, k):
    max_sum = -inf

    for i in range(0, n - k + 1):       # i+k-1 < n => i < n-k+1
        sm = 0

        for j in range(0, k):
            sm += arr[i + j]

        max_sum = max(max_sum, sm)

    return max_sum


if __name__ == "__main__":
    arr = [1, 8, 30, -5, 20, 7]
    n = len(arr)
    k = 3
    print(maxSum(arr, n, k))
