# Python Program to check
# whether given matrix is
# Diagonally Dominant Matrix.

# check the given given
# matrix is Diagonally
# Dominant Matrix or not.
def isDDM(m, n):
    # for each row
    for i in range(0, n):

        # for each column, finding
        # sum of each row.
        sum = 0
        for j in range(0, n):
            sum = sum + abs(m[i][j])

            # removing the
        # diagonal element.
        sum = sum - abs(m[i][i])

        # checking if diagonal
        # element is less than
        # sum of non-diagonal
        # element.
        if (abs(m[i][i]) < sum):
            return False

    return True


# Driver Code
n = 3
m = [[22.3, 2.9, -31.1],
     [43.9, -86.1, -97.7],
     [-1.6, 1.3, 24.2]]

if ((isDDM(m, n))):
    print("YES")
else:
    print("NO")

