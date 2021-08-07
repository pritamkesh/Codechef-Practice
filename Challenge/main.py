def deliver(qty, unit_price):
    threshold = 1000
    total_amount = unit_price * qty
    if total_amount > threshold:
        print("The order value can not be more than threshold")
        return "The order value can not be more than threshold"
    elif total_amount < threshold:
        if total_amount > 0:
            if total_amount % 5 == 0:
                print("The order is fizz")
            elif total_amount % 11 == 0:
                print("The order is buzz")
            elif total_amount % 5 == 0 and total_amount % 11 == 0:
                print("The order is fizzbuzz")


if __name__ == "__main__":
    quantity, per_unit_price = (input().split())
    quantity = int(quantity)
    per_unit_price = int(per_unit_price)
    deliver(quantity, per_unit_price)