def calculate_change(product_price, payment, available_coins):
    change = payment - product_price
    coins = sorted(available_coins, reverse=True)
    change_coins = []

    for coin in coins:
        while change >= coin and available_coins[coin] > 0:
            change -= coin
            available_coins[coin] -= 1
            change_coins.append(coin)

    if change == 0:
        return change_coins
    else:
        return None

# Часть 1: Неограниченное количество монет
products = {
    "молоко": 20,
    "хлеб": 15
}

available_coins_unlimited = {1: float('inf'), 5: float('inf'), 7: float('inf'), 10: float('inf'), 15: float('inf')}

product_name = input("Выберите продукт из списка (молоко, хлеб): ")
product_price = products.get(product_name)
payment = int(input("Введите сумму, которую вы дали: "))

if product_price and payment >= product_price:
    change_coins = calculate_change(product_price, payment, available_coins_unlimited)
    if change_coins:
        print(f"Сдача: {sum(change_coins)} рублей, монетами: {change_coins}")
    else:
        print("Невозможно выдать сдачу.")
else:
    print("Недостаточно средств.")

# Часть 2: Ограниченное количество монет
available_coins_limited = {1: 0, 5: 4, 10: 0, 15: 0, 20: 2}

product_price = 30
payment = 40

change_coins = calculate_change(product_price, payment, available_coins_limited)
if change_coins:
    print(f"Сдача: {sum(change_coins)} рублей, монетами: {change_coins}")
else:
    print("Невозможно выдать сдачу.")