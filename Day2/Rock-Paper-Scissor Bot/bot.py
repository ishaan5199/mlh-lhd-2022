import random

dict1 = {
    0: "rock",
    1: "paper",
    2: "scissors",
}

decider = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]

while True:

    # display and test
    action = int(input("\nChoose your weapon! rock[0], paper[1], scissors[2]...end[3]: "))
    if action == 3:
        print("\nThanks for playing :) Bbye\n")
        break
    
    if action not in dict1.keys():
        print("Invalid Option!")
        continue
    
    print(f"You chose {dict1[action]}!")
    counterAction = random.randint(0, 2)
    print(f"The computer chose {dict1[counterAction]}!")

    # result
    if decider[action][counterAction]:
        if action == counterAction:
            print("Its a tie!")
        else:
            print("You won :)")    
    else:
        print("You lost :(")
