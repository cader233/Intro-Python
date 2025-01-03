def exact_change(user_total):
    num_quarters = int(user_total // 25)
    user_total %= 25
    num_dimes = int(user_total // 10)
    user_total %= 10
    num_nickels = int(user_total // 5)
    user_total %= 5
    num_pennies = user_total
    return(num_pennies, num_nickels, num_dimes, num_quarters)

if __name__ == '__main__':
    input_val = int(input())
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)
    if input_val <= 0:
        print("no change")
    else:
        if num_pennies >= 1:
            if num_pennies == 1:
                print('1 penny')
            else:
                print(f'{num_pennies} pennies')
    if num_nickels >= 1:
        if num_nickels == 1:
            print('1 nickel')
        else:
            print(f'{num_nickels} nickel')
    if num_dimes >= 1:
        if num_dimes == 1:
            print('1 dime')
        else:
            print(f'{num_dimes} dimes')
    if num_quarters >= 1:
        if num_quarters == 1:
            print('1 quarter')
        else:
            print(f'{num_quarters} quarters')
