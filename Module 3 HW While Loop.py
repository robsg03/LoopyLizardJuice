Password = "admin123"
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    guess = input("Input your password: ")
    if guess == Password:
        print("Your password is correct! You can continue your work")
        break
    else:
        guess_count += 1
        if guess_count < guess_limit:
            print("Incorrect password. Try again")
        else:
            print("Sorry, too many failed attempts.")
#######################################################################
# IN class example on day 4
Password = "admin123"
guess_count = 0
guess_limit = 4

while guess_count < guess_limit:
    guess = input("Enter your Password: ")
    if guess == Password:
        print("Correct!")
        break
    else:
        guess_count = guess_count + 1
        attempts_left = guess_limit - guess_count

        if attempts_left > 0:
            #print(f"Incorrect PW. {attempts_left} attempt(s) remaining.")
            print("Incorrect guess.", attempts_left, "attempts remaining")
        else:
            print("Sorry, too many failed attempts")
