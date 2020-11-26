def isSorted(arr,n):

    for i in range(n):

        for j in range(i+1,n):

            if arr[j]<arr[i]:
                return False

    return True

if __name__ == '__main__':
    arr = [7,2,30,10]
    n = 4

    print(isSorted(arr,n))
