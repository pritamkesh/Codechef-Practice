def maxArraySliding(a, n, w):
    max = 0
    for element in range(n - w +1):
        max = a[element]
        for i in range(1, w):
            if a[element + i] > max:
                max = a[element+i]
                print(str(max) + " " + ",")


if __name__ == "__main__":
    a = [1, 3, -1, -3, 5, 3, 6, 7]
    n = len(a)
    w = 3
    print(maxArraySliding(a,n,w))
