# Problem Statement : https://www.codechef.com/problems/HS08TEST
# cook your dish here
def atm(cash_to_withdraw, account_balance):
    bank_charges = 0.50
    if cash_to_withdraw + bank_charges > account_balance:
        print('%.2f' % account_balance)
    else:
        if cash_to_withdraw % 5 == 0:
            final_balance = (account_balance - cash_to_withdraw) - bank_charges
            print('%.2f' % final_balance)
        else:
            print('%.2f' % account_balance)


if __name__ == "__main__":
    # cash_to_withdraw, account_balance = map(float,input().split())
    cash_to_withdraw, account_balance = (input().split())
    cash_to_withdraw = int(cash_to_withdraw)
    account_balance = float(account_balance)
    atm(cash_to_withdraw, account_balance)
