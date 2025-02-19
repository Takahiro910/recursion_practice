import random


while True:
    try:
        n = int(input("input small number."))
        m = int(input("input learge number."))
        if n <= m: break
        else: print("small number should be smaller than learge number.")
    except ValueError:
        print("please input integer.")

secret_number = random.randint(n, m)
attempts = 0
max_attempts = 10

print(f"Guess the secret number between {n} and {m}.")

while attempts < max_attempts:
    try:
        guess = int(input("please input integer: "))
        attempts += 1

        if guess == secret_number:
            print("You got it!")
            break
        elif guess > secret_number:
            print("smaller")
        else:
            print("learger")
    except ValueError:
        print("please input integer.")

if attempts == max_attempts:
    print(f"Sorry, time's up. The correct answer was {secret_number}")