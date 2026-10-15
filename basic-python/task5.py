reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

avg_rating = {}
stars_sum = {}
reviews_count = {}

for review in reviews:
    review["product"] = review["product"].lower()

for review in reviews:
    name = review["product"]
    stars_sum[name] = stars_sum.get(name, 0) + review['stars']
    reviews_count[name] = reviews_count.get(name, 0) + 1

for review in stars_sum:
    name = review["product"]
    avg_rating[name] = stars_sum[name] / reviews_count[name]

print("Средняя оценка товаров:")
for name, value in avg_rating.items():
    print(f"{name}: {value}")

worst_good = ""
words_avg = 10000000000
for name in reviews_count.keys():
    if reviews_count[name] >= 2:
        if words_avg > avg_rating[name]:
            worst_good = name
            words_avg = avg_rating[name] 
print(f"Худший товар по средней оценке среди тех, у кого хотя бы два отзыва: {worst_good}")

stars_1or2 = 0
for review in reviews:
    if review["stars"] in (1 , 2):
        stars_1or2 += 1
         

print(f"Отзывов на 1 или 2 здвезды: {stars_1or2}")

print(f"Доля таких отзывов: {stars_1or2 / len(reviews)}")