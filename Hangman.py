# Hangman Homework

import random

fruits = ["apple", "apricots", "avacado", "banana", "blackberries", "blueberries", "cherries", "cranberries", 
            "grapefruit", "grapes", "lemon", "lime",
          "mango", "orange", "pear", "pineapple", "raspberries", "strawberries", "pineapple"]


class Hangman:
    def __init__(self):
        self.word = random.choice(fruits)
        self.display = ["_" for letter in self.word]
        self.guesses = 0
        self.guessed_words = []

    def show(self):
        display = "".join(self.display)
        print(f"Mystery Word: {display}")

    def get_word_index(self, guess):
        positions = []
        for index, char in enumerate(list(self.word)):
            if char == guess:
                positions.append(index)
        return positions

    def update(self, idx, letter):
        for number in idx:
            self.display[number] = letter

    def check_guess(self, guess):
        if guess in self.word not in self.guessed_words:
            idx = self.get_word_index(guess)
            self.update(idx, guess)
        elif guess in self.guessed_words:
            print("Already guessed. Please try again.")
        elif guess not in self.word:
            self.guesses += 1
            self.guessed_words.append(guess)
            print("Incorrect. Try again.")


    def check_for_win(self):
        display = "".join(self.display)
        word = self.word
        if display == word:
            print("~*" * 50)
            print("Winner Winner Chicken Dinner")
            print("~*" * 50)
            return True


def game():
    played = []
    word = Hangman()
    while True:
        guess = input("\nGuess your letter: ")
        word.check_guess(guess)
        word.show()
       
        played.append(guess)
        if word.check_for_win():
            print("~*" * 50)
            print("Winner Winner Chicken Dinner!")
            print("~*" * 50)
            break
        elif word.guesses > 6:
            print("Loser, better luck next time.")
            break
        

def loop():
    while True:
        print("=~=" * 50)
        response = input(
            "\nWant to play a game? Press y to play 'y'. To exit press 'n':  ")
        print("=~=" * 50)
        if response == "y/n":
            break
        game()


loop()
