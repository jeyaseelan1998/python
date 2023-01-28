
def square(n):
    return n * n


def checkTriplet(a):
    # code here
    n = len(a)
    # print(n)
    # print(a)

    a.sort()
    print(a)

    flag = False

    for i in range(0, len(a)-2):
        for j in range(i+1, len(a)-1):
            print(a[i], a[j])
            if (a[i]*a[i]+a[j]*a[j])**0.5 in a:
                flag = True
                break
        if flag == True:
            break
        print()
    return flag


print(checkTriplet([4, 49, 1, 59, 19]))
print()
