secret_word ='pythonlearner'
Guess_count = 1
Guesses = 0
while Guess_count <=3:
    guess = input("enter your guess : ")
    Guesses += 1
    if guess == secret_word:
        print("you won!")
        break
    Guess_count += 1
else:
    print("you lost!")