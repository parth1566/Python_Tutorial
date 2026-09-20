import random

def play_game():
    lucky_num = random.randint(1, 50)

    while True:
        user_num = int(input("Guess the lucky num: "))
        if(user_num == lucky_num):
            print("Congratulations! You guessed it right")
            break
        elif user_num < lucky_num:
            print("Too low")
        else :
            print("Too High")



play_game()
print("Thanks for playing")
