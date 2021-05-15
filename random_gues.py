
import random

def computer_guess(x):
    while True:
        low = (int(input("Enter the lowest number the computer can guess :")))
        high = x
        feedback = int(input("Enter any integer number : "))
        guess = random.randint(low, high)
        while guess != feedback:
            print(guess)
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low
            if (feedback < guess):
                high = guess+1

            elif (feedback > guess):
                low = guess-1

        print(guess)

        print('The number is : ', guess)

        while True:
            Q = input("whould like to try again ? : (y/n)")
            if Q.lower() == "y":
                computer_guess(int(input("Enter the highest number the computer can guess : ")))

                break
            elif Q.lower() == "n":
                exit()
            else:
                print("Enter (y/n)")

computer_guess(int(input("Enter the highest number the computer can guess : ")))
