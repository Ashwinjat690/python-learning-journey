game = input("enter what to do : ")
guess = 1
while guess <2:
    if game =="start":
        print("game started .... let's go")
        guess +=1

    elif game =="stop":
        print("game stopped")
        guess +=1
    elif game =="quit":
        print("game quit")
        guess +=1
    
if game != "start" and game != "stop" and game != "quit":
    print("invalid command ")