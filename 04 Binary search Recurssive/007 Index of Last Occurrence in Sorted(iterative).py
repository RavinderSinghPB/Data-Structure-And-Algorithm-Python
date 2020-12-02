def lastOcc(arr,n,x):

    low = 0
    high = n-1

    while low <= high:

        mid = (low+high)//2

        if x > arr[mid]:
            low = mid + 1

        elif x < arr[mid]:
            high = mid - 1

        else:
            if mid == n - 1 or arr[mid + 1] != arr[mid]:
                return mid
            else:
                low = mid + 1

    return -1


if __name__ == "__main__":
    arr = [5, 10, 10, 10, 10, 20, 20]
    n = 7
    x = 10

    print(lastOcc(arr,n,x))