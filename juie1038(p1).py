name = "Nafisa Sultana Juie"
vowels = 0
consonants = 0

for ch in name:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
