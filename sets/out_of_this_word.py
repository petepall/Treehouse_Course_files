import random
import os


WORDS = (
    "treehouse",
    "python",
    "learner",
)


def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')


def prompt_for_words(challenge):
    guesses = set()
    print(f"What words can you find in the word {challenge}")
    print("(Enter Q to Quit)")
    while True:
        guess = input(f"{len(guesses)} words >  ")
        if guess.lower() == 'q':
            break

        guesses.add(guess.lower())
    return guesses


def output_results(results):
    for word in results:
        print(f"*\t{word}")


def statistics(words_player1, words_player2):
    return words_player1 - words_player2


challenge_word = random.choice(WORDS)

clear_screen()
print("Play - Player 1:")
player1_words = prompt_for_words(challenge_word)
print("\nPlay - Player 2:")
player2_words = prompt_for_words(challenge_word)

clear_screen()
print("Results processing:")
print("===================")
print("\nPlayer 1 results:")
player1_unique = statistics(player1_words, player2_words)
print(f"{len(player1_words)} guesses, {len(player1_unique)} unique")
output_results(player1_unique)
print("-" * 10)
print("Player 2 results:")
player2_unique = statistics(player2_words, player1_words)
print(f"{len(player2_words)} guesses, {len(player2_unique)} unique")
output_results(player2_unique)
print("-" * 10)
print("Shared guesses")
shared_words = player1_words & player2_words
output_results(shared_words)
