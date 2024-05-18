import json
def first():
    with open('jsn.json', 'r', encoding = "utf-8") as file:
        spisok = json.load(file)
    for product in spisok['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
def second():
    with open('jsn.json', 'r', encoding = "utf-8") as file:
        spisok = json.load(file)

    new_product = {}
    new_product['name'] = input()
    new_product['price'] = int(input())
    new_product['weight'] = int(input())
    new_product['available'] = bool(input())
    spisok['products'].append(new_product)

    with open('products.json', 'w',encoding = "utf-8") as file:
        json.dump(spisok, file)
    for product in spisok['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
def third():
    ruen = {}
    with open('en-ru.txt', 'r', encoding = 'utf-8') as file:
        for stroka in file:
            en = stroka.split(' - ')[0]
            ru = stroka.split(' - ')[1]
            rus_slova = ru.split(', ')
            for slovo in rus_slova:
                if slovo in ruen:
                    ruen[slovo].append(en)
                else:
                    ruen[slovo] = [en]

    ruen = dict(sorted(ruen.items()))
    with open('ru-en.txt', 'w', encoding = 'utf-8') as file:
        for ru_word, en_words in ruen.items():
            file.write(f'{ru_word} - {"".join(en_words)}\n')

third()
