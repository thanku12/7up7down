import time
from random import randint

money = int(input("Welcom you, 7thup 7thdown is adics game which is played by betting on numbers more then 7 or less then 7. \n Two dies are rolled in the game "))
play = input("Do you want to play a game of 7th up 7th down? Y or N")
while play.startswith('y'):
    number = randint(1,12)
    bet = int(input("for how much money you want to bet for? "))
    if bet > money:
        print("Foul! Not enough money you need extra", bet-money,"rupess to place the bet, withdraw enough money next time")
        break
    guess = input("Bet from the ")
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print(" Dies are rolling...")
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print(".....")
    time.sleep(1)

    if guess.lower().startswith('a'):
        if number > 7:
            print("you have guessed correctly! the number was",number)
            money = money + bet
            print("you have", money, "rupees.")
            play = input(("play again? Y or N "))
            if money < 1:
                print("you have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your ATM")
        if number < 8:
            print("you have guessed wrong! the number was",number)
            money = money - bet
            print("you have",money," rupees.")
            play = input("play again? Y or N ")
            if money < 1:
                print("you have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your ATM")

    if guess.lower().startswith('b'):
        if number < 7:
            print(f"you have guessed correctly! the number was")
            money = money + bet
            print("you have", money, "rupees.")
            play = input(("play again? Y or N "))
            if money < 1:
                print("you have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your ATM")

        if number > 6:
            print("you have guessed wrong! the number was", number)
            money = money - bet
            print("you have", money, " rupees.")
            play = input("play again? Y or N ")
            if money < 1:
                print("you have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your ATM")

    if guess.lower().startswith('c'):
        if number == 7:
            print("you have guessed correctly! the number was", number)
            money = money + (bet * 2)
            print("you have", money, "rupees.")
            play = input(("play again? Y or N "))
            if money < 1:
                print("you have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your ATM")

        if number != 7:
            print("you have guessed wrong! the number was", number)
            money = money - (bet * 2)
            print("you have", money, " rupees.")
            play = input("play again? Y or N ")
            if money < 1:
                print("you have run out of money, time to go to the ATM")
                money = int(input("How much money you want to withdraw from your ATM")



print()
print("Okey, the game is over.")
print("you finished with", money, "rupees.")



"""

import time
from random import randint

# Start with the initial amount of money
print("Welcome! 7thup 7thdown is a dice game where you bet on whether the sum of two dice will be higher, lower, or exactly 7.")
play = input("Do you want to play a game of 7thup 7thdown? (Y/N): ").lower()

money = int(input("How much money do you want to start with? "))

# Check if the user ran out of money
if money < 1:
    print("You have run out of money, time to go to the ATM.")
    money = int(input("How much money do you want to withdraw from your ATM? "))

# Ask if the user wants to play

while play == 'y':
    number = randint(2, 12) # Dice sum should be between 2 and 12
    bet = int(input(f"How much money do you want to bet? You have {money} rupees: "))

    if bet > money:
        print(
            f"Not enough money! You need {bet - money} more rupees to place this bet. Withdraw enough money next time.")
        break

    if bet == 0:
        print(f"You should put the bet atlest 1 rupees to this bet. put 1 or more than 1 rupees next time.")
        bet = int(input(f"How much money do you want to bet? You have {money} rupees: "))

    # Check if the user ran out of money
    if money < 1:
        print("You have run out of money, time to go to the ATM.")
        money = int(input("How much money do you want to withdraw from your ATM? "))

    guess = input("Bet 'a' for more than 7, 'b' for less than 7, or 'c' for exactly 7: ").lower()

    # Simulate the dice rolling
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print("The dice are rolling...")
    time.sleep(1)
    print(".....")
    time.sleep(1)

    # Handle guesses
    if guess == 'a':
        if number > 7:
            print(f"You guessed correctly! The number was {number}.")
            money += bet
        else:
            print(f"You guessed wrong! The number was {number}.")
            money -= bet

    elif guess == 'b':
        if number < 7:
            print(f"You guessed correctly! The number was {number}.")
            money += bet
        else:
            print(f"You guessed wrong! The number was {number}.")
            money -= bet

    elif guess == 'c':
        if number == 7:
            print(f"You guessed correctly! The number was {number}. You win double your bet!")
            money += bet * 2
        else:
            print(f"You guessed wrong! The number was {number}. You lose double your bet!")
            money -= bet * 2
    else:
        print("Invalid guess! Please choose 'a', 'b', or 'c'.")

    # Check if the user ran out of money
    # if money < 1:
    # print("You have run out of money, time to go to the ATM.")
    # money = int(input("How much money do you want to withdraw from your ATM? "))

    # Ask if the player wants to continue playing
    # play = input("Do you want to play again? (Y/N): ").lower()

print()
print(f"Okay, the game is over. You finished with {money} rupees.")