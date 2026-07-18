import random


words = ["python", "java", "c++", "mern", "django"]


word = random.choice(words)


guessed_letters = []


display = ["_"] * len(word)

attempts = 6

print("=" * 40)
print("        HANGMAN GAME")
print("=" * 40)

while attempts > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print("Wrong Guess!")

if "_" not in display:
    print("\nCongratulations!")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)