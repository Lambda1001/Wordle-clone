import pathlib
import random
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme


console = Console(width=40, theme = Theme({" warning ":" red on yellow "}))


def get_random_word(wordList):
    """
    Getting a 5 letter word from a list of strings

    ##Example: 
    >>> get_random_word(["SNAKE","WORD","it'll"])
    'SNAKE'
    
    """
    words = [
            word.upper()
            for word in wordList
        ]
    return random.choice(words)

def show_guesses(guesses, word):
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
    console.print("".join(styled_guess), justify="center")

def game_over(guesses, word, guessed_correctly):
    refresh_page(headline="Game over")
    show_guesses(guesses, word)

    if guessed_correctly:
        console.print(f"\n [bold white on green] Correct, the word is {word} [/]")
    else:
        console.print(f"\n [bold white on red] Sorry, the word is {word} [/]")
    

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold red] :leafy_green: {headline} :leafy_green: [/]\n")

def main():
    #pre processing
    path = pathlib.Path("wordlist2.txt")
    word = get_random_word(path.read_text(encoding="utf-8").split("\n"))
    guesses = ["_" *5]*6

    #main loop
    for idx in range(6):
        refresh_page(headline = f"Guess {idx + 1}")
        show_guesses(guesses, word)

        guesses[idx] = input(f"\nGuess {idx+1}: ").upper()
        if guesses[idx] == word:
            break

    game_over(guesses, word, guessed_correct = guesses[idx] == word)

if __name__ == "__main__":
    main()
