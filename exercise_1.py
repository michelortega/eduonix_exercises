"""
Exercise 1 Eduonix Machine Learning
"""


class GuessTheNumber():

    def __init__(self):
        import random
        self.__number = random.randint(1, 25)

    def start(self):
        while True:
            try:
                self.__games = int(input('\nHow many games do you want to play?'))
            except ValueError:
                print("\nNot an integer! Try again.")
                continue
            else:
                break

        for guess in range(self.__games):
            while True:
                try:
                    self.__selected_number = int(input('\nSelect a number between 1 and 25'))
                except ValueError:
                    print("\nNot an integer! Try again.")
                    continue
                else:
                    if self.__selected_number > 0 and self.__selected_number <= 25:
                        break
                    else:
                        print("\nNot a number between 1 and 25! Try again.")
                        continue

            if self.__selected_number == self.__number:
                print(f"\nYou have selected {self.__selected_number}. You win. It took you {guess + 1} guess/es")
                break

            if self.__selected_number > self.__number:
                print(f"\nYou have selected {self.__selected_number}. Your number is higher.")

            if self.__selected_number < self.__number:
                print(f"\nYou have selected {self.__selected_number}. Your number is lower.")

            if guess < self.__games - 1:
                print(f"\nTry again")

            if guess == self.__games - 1:
                print(f"\nThat was your last guess. You lose.")