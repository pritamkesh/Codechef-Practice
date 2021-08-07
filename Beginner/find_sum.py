def find_sum(first_no, second_no):
    a = first_no
    b = second_no
    if a > 0 and b > 0:
        sum = a + b
        return sum
    elif a > 0 and b <= 0:
        return a
    elif a <= 0 and b > 0:
        return b
    else:
        return "The sum is zero as both the numbers are zero"


if __name__ == "__main__":
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))
    print(find_sum(a, b))
