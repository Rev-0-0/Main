won = False

while not won:
    try:
        print("Throw the first dart")
        scr1 = int(input("Enter score 1\n>> "))

        print("Throw second dart")
        scr2 = int(input("Enter score 2\n>> "))

        print("Throw last dart")
        scr3 = int(input("Enter score 3\n>> "))

        total = scr1 + scr2 + scr3

        print("-" * 30)
        print(f"Your final score is {total}")

        if total < 100:
            print("You win! Your score is less than 100!")
            print("-" * 30)
            won = True
        else:
            print("You lose. Score is 100 or more.")
            print("Next player step up.")
            print("-" * 30)

    except ValueError:
        print("\nWrong value input, restarting")
        print("-" * 30)