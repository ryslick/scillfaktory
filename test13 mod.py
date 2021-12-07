tiket = input("Введите требуемое кол-во билетов: ")

pirce = 0
tiket_numb = 1

while tiket_numb <= int(tiket):
    if tiket_numb <= int(tiket):
        age_for_tiket = dict.fromkeys([tiket_numb],)
        print('укажите возраст посетителя для', tiket_numb, 'билета')
        age_for_tiket[tiket_numb] = int(input())

        if int(age_for_tiket[tiket_numb]) < 18:
            print("посетителю конференции менее 18 лет, он проходит на конференцию бесплатно")
        elif 18 <= age_for_tiket[tiket_numb] < 25:
            print("стоимость билета для данного посетитея будет составлять: ", 990, "руб.")
            pirce += 990
        else:
            print("стоимость билета для данного посетитея будет составлять: ", 1390, "руб.")
            pirce += 1390

        tiket_numb += 1


    else:
        print("Подсчет стоимости Вашего заказа окончен")

if int(tiket) < 4:
    print("Сумма к оплате - ", pirce)
else:
    pirce = pirce - ((pirce * 10) / 100)
    print("Сумма к оплате - ", pirce)