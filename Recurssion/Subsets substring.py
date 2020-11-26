def printSub(strng,curr,ind):
    if ind == len(strng):

        print(curr,end=' ')
        return
    printSub(strng,curr,ind+1)
    printSub(strng,curr+strng[ind],ind+1)


strng = "ABC"
printSub(strng,'',0)