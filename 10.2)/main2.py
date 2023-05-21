import json

with open('r.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for product in data['products']:
    print("Название:", product['name'])
    print("Цена:", product['price'])
    print("Вес:", product['weight'])
    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")

new_product = {}
new_product['name'] = input("Введите название продукта: ")
new_product['price'] = float(input("Введите цену продукта: "))
new_product['weight'] = float(input("Введите вес продукта: "))
new_product['available'] = input("Есть ли продукт в наличии? (y/n): ").lower() == 'y'

data['products'].append(new_product)

with open('r.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("\nИтоговый список продуктов:")
for product in data['products']:
    print("Название:", product['name'])
    print("Цена:", product['price'])
    print("Вес:", product['weight'])
    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")