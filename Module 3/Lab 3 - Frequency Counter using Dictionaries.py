# Lab Exercise 3: Frequency Counter using Dictionaries

text = input("Enter a sentence: ").lower()
frequency = {}

for character in text:
    if character != " ":
        frequency[character] = frequency.get(character, 0) + 1

print("\nCharacter Frequency:")
for character, count in sorted(frequency.items()):
    print(f"{character}: {count}")

print("\nWord Frequency:")
word_frequency = {}
for word in text.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1

for word, count in sorted(word_frequency.items()):
    print(f"{word}: {count}")
