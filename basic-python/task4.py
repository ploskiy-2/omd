days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]
week_revenue = 0
max_revenue_day = ""
max_revenue = -1
avg_per_order = {}
returns_20_days = set()


for day in days:
    week_revenue += day["revenue"]
    if day["revenue"] > max_revenue:
        max_revenue = day["revenue"]
        max_revenue_day = day["day"]

    avg_per_order[day["day"]] = day["revenue"] / day["orders"]
    if day["returns"] / day["orders"] > 0.2:
        returns_20_days.add(day["day"])

print(f"Выручка за всю неделю составляет: {week_revenue}")
print(f"День с самой большой выручкой - {max_revenue_day}")
print('Средняя выручка на заказ:')
for day, value in avg_per_order.items():
    print(f"{day}: {value}")
print(f"Дни, где возвратов больше 20% заказов: {returns_20_days}")