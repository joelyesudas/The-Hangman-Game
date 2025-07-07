import random

words = ['python', 'developer', 'hangman', 'project', 'keyboard']
word = random.choice(words)

guessed_letters = []
tries = 6
display_word = ['_' for _ in word]

print("🕹️ Welcome to Hangman!")

while tries > 0 and '_' in display_word:
    print("\nWord: ", ' '.join(display_word))
    print(f"Tries left: {tries}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that.")
    elif guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong!")
        tries -= 1
    
    guessed_letters.append(guess)

if '_' not in display_word:
    print(f"\n🎉 You won! The word was: {word}")
else:
    print(f"\n💀 You lost! The word was: {word}")