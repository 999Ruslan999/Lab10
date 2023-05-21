with open('r.en-ru.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

dictionary = {}
for line in data:
    words = line.strip().split(' - ')
    if len(words) < 2:
        continue
    eng_word = words[0]
    rus_words = words[1].split(', ')
    for rus_word in rus_words:
        if rus_word not in dictionary:
            dictionary[rus_word] = [eng_word]
        else:
            dictionary[rus_word].append(eng_word)

with open('ru-en.txt', 'w', encoding='utf-8') as f:
    for key in sorted(dictionary.keys()):
        eng_words = ', '.join(sorted(dictionary[key]))
        f.write(f"{key} - {eng_words}\n")

print("Словарь успешно создан и сохранен в файл ru-en.txt")