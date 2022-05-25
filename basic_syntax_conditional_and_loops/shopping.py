budget = int(input())

while True:
    current_product_price = input()
    if current_product_price == 'End':
        print(f'You bought everything needed.')
        break

    else:
        budget -= int(current_product_price)
    if budget < 0:
        print(f'You went in overdraft!')
        break