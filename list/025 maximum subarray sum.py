def subArraySum(arr, n, sm):
    curr_sum = arr[0]
    start = 0

    for i in range(1, n + 1):

        while curr_sum > sm and start < i - 1:
            curr_sum = curr_sum - arr[start]
            start += 1

        if curr_sum == sm:
            print(start, i - 1)
            return

        if i < n:
            curr_sum = curr_sum + arr[i]

    print('"No subarray found')


if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    sm = 23

    subArraySum(arr, n, sm)
