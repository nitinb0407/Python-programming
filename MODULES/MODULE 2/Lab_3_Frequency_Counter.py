# MODULE 2 - LAB EXERCISE 3
# Frequency counter using dictionaries.

sentence = input("Enter a sentence: ").lower()
frequency = {}
for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequencies:")
for word, count in frequency.items():
    print(word, ":", count)

# SAMPLE INPUT
# Enter a sentence: apple banana apple orange banana apple
# SAMPLE OUTPUT
# Word frequencies:
# apple : 3
# banana : 2
# orange : 1
