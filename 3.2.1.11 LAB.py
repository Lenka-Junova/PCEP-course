# 3.2.1.11 LAB task - Write a program that uses: a for loop; the concept of conditional execution (if-elif-else); the continue statement. Your program must: ask the user to enter a word;use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry; use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word; assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
word_without_vowels = ""
user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)
