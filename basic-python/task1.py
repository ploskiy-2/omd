moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}

both_city = moscow.intersection(kazan)
moscow_goods = moscow - kazan
kazan_goods = kazan - moscow
unique_goods = moscow.symmetric_difference(kazan) + both_city


print(f"Можно забрать в любом из двух городов товары: ", both_city)
print(f"Можно забрать только в Москве: ", moscow_goods )
print(f"Можно забрать только в Казани ", kazan_goods )
print(f"Всего разных товаров в двух городах: ", len(unique_goods))

