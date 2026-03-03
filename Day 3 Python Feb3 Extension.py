apple = 2
while apple <=5:
    print(apple)
    apple = apple + 1

    secret_number = 9
    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit:
        guess = int(input("Guess the secret number: "))
        if guess == secret_number:
            print("Your guess is correct!")  # when the trial is correct, this is printed
            break  # Allows us to break the while loop
        else:
            guess_count += 1  # Equivalent to guess_count = guess_count + 1
            if guess_count < guess_limit:
                print("Incorrect guess. Try again")  # when incorrect, this is printed
            else:
                print("Sorry, too many failed attempts")  # this is printed after three attempts
###################################################################################################################
#day 4 review adding onto day 3
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
