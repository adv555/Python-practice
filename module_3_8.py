# Вариант 1

def cost_delivery(quantity,*_,discount=0):
    price_for_fist_item = 5
    price_for_next_item = 2

    delivery_price_for_fist_item = price_for_fist_item - price_for_fist_item * discount
    delivery_price_for_next_item = price_for_next_item - price_for_next_item * discount

    sum = delivery_price_for_fist_item

    if quantity == 1:
        return sum
    if quantity > 1:
       for _ in range(quantity-1):
           sum+=delivery_price_for_next_item
    
    return sum

# Вариант 2

def cost_delivery_2(quantity, *_, discount=0):
    """Функция возвращает общую сумму доставки.

    Первый параметр &mdash; количество товаров в заказе.
    Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0."""
    
   
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result

print(cost_delivery_2.__doc__)
  


print(cost_delivery(2, 1, 2, 3))
print(cost_delivery(3, 3))
print(cost_delivery(1))
print(cost_delivery(2, 1, 2, 3, discount=0.5))

print(cost_delivery_2(2, 1, 2, 3))
print(cost_delivery_2(3, 3))
print(cost_delivery_2(1))
print(cost_delivery_2(2, 1, 2, 3, discount=0.5))