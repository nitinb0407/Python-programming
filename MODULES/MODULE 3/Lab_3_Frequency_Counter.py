# MODULE 3 - LAB EXERCISE 3
# Frequency counter using dictionaries (character frequency).

text = input("Enter a word: ").lower()
frequency = {}
for character in text:
    if character != " ":
        frequency[character] = frequency.get(character, 0) + 1

print("Character frequencies:")
for character, count in frequency.items():
    print(character, ":", count)

# SAMPLE INPUT
# Enter a word: programming
# SAMPLE OUTPUT
# Character frequencies:
# p : 1
# r : 2
# o : 1
# g : 2
# a : 1
# m : 2
# i : 1
# n : 1
