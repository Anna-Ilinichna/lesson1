product={"city":"Москва","temperature":20}
# print(product["city"])
# print(product["temperature"]-5)
product.update({"country": "Россия"})
product["date"] = "27.05.2019"
print(product)
print(len(product))