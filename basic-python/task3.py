orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

sum_returned = 0
users_returned = set()
count_delivered = 0
sum_delivered = 0 

for order in orders:
    if order["status"] == "returned":
        sum_returned += order["amount"]
        users_returned.add(order["buyer"])
    if order["status"] == "delivered":
        count_delivered += 1
        sum_delivered += order["amount"] 
print(f"Было оформлено возвратов на сумму: {sum_returned}")  

print(f"Люди, которые хоть раз оформляли возврат: {users_returned}")

print(f"Было доставлено заказов: {count_delivered}")
print(f"Средний чек, доставленных заказов: {sum_delivered / count_delivered}")
