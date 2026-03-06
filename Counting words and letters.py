text = input("Привет!\nВведите текст: ")

words = text.split()

clean_words = []
for word in words:
    clean = word.strip(".,!?;:'\"()-")
    if clean and clean.isalpha():
        clean_words.append(clean.lower())

total_words = len(clean_words)
unique_words = len(set(clean_words))

freq = {}
for char in text.lower():
    if char.isalpha():
        freq[char] = freq.get(char, 0) + 1

print(f"Слов всего: {total_words}")
print(f"Уникальных слов: {unique_words}")
print(f"Частота букв: {freq}")