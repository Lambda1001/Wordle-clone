import pathlib
import random
from string import ascii_letters


def get_random_word():
    wordList = pathlib.Path("wordlist.txt")
    words = [
            words.upper()
            for word in wordList.read_text(encoding="utf-8").split("\n")
            if len(word) == 5 and all(letter in ascii_letters for letter in word)
        ]
    return random.choice(words)

def show_guess(guess, word):
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters: ", " , ".join(sorted(correct_letters)))
    print("Misplaced letters: ", " , ".join(sorted(misplaced_letters)))
    print("Wrong letters: ", " , ".join(sorted(wrong_letters)))

def game_over(word):
    print(f"The word was {word}")  

def main():
    #pre processing
    word = get_random_word()
    
    #main loop
    for guess_num in range(1,7):
        guess = input(f"\nGuess {guess_num}: ").upper()

        show_guess(guess, word)
        if guess == word:
            break

    #post processing
    else:
        game_over(word)
if __name__ == "__main__":
    main()
