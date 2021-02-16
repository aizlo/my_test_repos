products = []
order = 1

while order <= 2:
    title = input('Введите название товара: ')
    price = input('Введите стоимость товара: ')
    amount = input('Введите количество: ')
    unit = input('Введите единицы измерения: ')

    current_product = (
        order,
        {
            'title': title,
            'price': price,
            'amount': amount,
            'unit': unit
        })
    products.append(current_product)
    order += 1  # equeval order = order + 1

print(products)
