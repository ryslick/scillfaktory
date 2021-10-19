per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("введите сумму"))/100


deposit = per_cent.values()
deposit = [int(i * money) for i in deposit]

print(deposit)

print("Максимальная сумма, которую вы можете заработать — " and max(deposit))
