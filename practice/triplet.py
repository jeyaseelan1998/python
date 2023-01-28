def triplet(arr=[4, -16, 7, 4, -7, -36, 0]):
    "Check whether it contains a triplet that sums up to zero"
    n = len(arr)

    arr.sort()

    for i in range(n-2):
        l = i+1
        r = n - 1

        while l < r:
            sum = arr[i] + arr[l] + arr[r]
            if sum == 0:
                return 1
            elif sum < 0:
                l += 1
            else:
                r -= 1
    return 0


print(triplet())

# Input: n = 5, arr[] = {0, -1, 2, -3, 1}
# Output: 1
# Explanation: 0, -1 and 1 forms a triplet
# with sum equal to 0.

# Input: n = 3, arr[] = {1, 2, 3}
# Output: 0
# Explanation: No triplet with zero sum exists.
