import random , input , print # type: ignore

def Game():

    computer = random.choice([-1,0,1])

    youstr = input("Enter Your Choice: ")
    youdict = {"s" : -1 , "w" : 0 , "g" : 1}
    you = youdict[youstr]
    altdict = {-1 : "snake", 0 : "water", 1 : "gun"}

    print(f"You Choose: {altdict[you]}\nComputer Choose: {altdict[computer]}")

    if(computer == you):
        print("Its a Draw")
    else:
        if(computer == -1 and you == 0):
            print("You Lose")
        elif(computer == -1 and you == 1):
            print("You Win")
        elif(computer == 0 and you == 1):
            print("You Win")
        elif(computer == 0 and you == -1):
            print("You Lose")
        elif(computer == 1 and you == 0):
            print("You Lose")
        elif(computer == 1 and you == -1):
            print("You Lose")
        else:
            print("something went wrong")
        
while True:
    Game()
    cont = input("Do You Want To Continue (y/n): ").lower()
    if cont == "n":
        print("Thanks for playing!")
        break
    elif cont != "y":
        print("Invalid input! Exiting the game.")
        break