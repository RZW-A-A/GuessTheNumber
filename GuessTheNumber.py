import random as r

def guesstheno():

    gen_num = r.randint(1, 10)              #random number generating

    for i in range(1, 6):                   #for 5 chances (1,6)

        user_num=int(input("Enter number between 1 to 10 = "))           #user entered number

        if user_num == gen_num:
            print("Congratulations you are the winner.\nYou guessed right number.")
            print(user_num, "is your number.")
            print(gen_num, "is generated number by computer.")
            break

        elif user_num > 10 or user_num < 1:
            print("Invalid entry")
            guesstheno()
            break               #restart the game with differnet generated number if invalid entry

        elif user_num < gen_num:
            print("Guess a higher number than your {}.".format(user_num))

        else:
            print("Guess a lower number than your {}.".format(user_num))

        print(5-i, "chances left")

    else:
        print("!!! YOU LOSE !!!")

guesstheno()
