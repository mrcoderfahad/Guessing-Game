secrect_number = 5
guess_limit = 1
guess_count = 3

while guess_limit <= guess_count:
    user_guess_number = int(input("Guess<🎃> "))
    guess_limit += 1
    if user_guess_number == secrect_number:
        print("You Win 👻")
        break
else:
    print("You Lose 🧟")