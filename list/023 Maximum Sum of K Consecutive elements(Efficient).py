def maxSum(arr, n, k):
    curr_sum = 0

    for i in range(0, k):
        curr_sum += arr[i]

    max_sum = curr_sum

    for i in range(k, n):
        curr_sum += (arr[i] - arr[i - k])
        max_sum = max(max_sum, curr_sum)

    return max_sum


if __name__ == "__main__":
    arr = [1, 8, 30, -5, 20, 7]
    n = len(arr)
    k = 3
    print(maxSum(arr, n, k))
