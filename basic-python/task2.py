queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]


all_searches = len(queries)

print(f"Всего поисковых запросов в ленте:", all_searches)

print()

counts = {}
for search in queries:
    counts[search] = counts.get(search, 0) + 1
print("Сколько раз ввели каждый запрос")
for key,value in counts.items():
    print(f"{key}: {value}")

print()

max_search = ""
max_count = -1
for key,value in counts.items():
    if value > max_count:
        max_count = value
        max_search = key
print(f"Чаще всего вводили запрос: {max_search}, {max_count} раз")
print(f"Самый частый вопрос занимает {max_count / all_searches} от всех запросов")
print("Запросы, которые встретились один раз:")
for key,value in counts.items():
    if value == 1:
        print(key, end=' ')
