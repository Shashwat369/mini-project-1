import random
computer=random.choice([1, 0, -1])
youstr=input("Enter your choice : ")
youDict = {"r" : 1 , "p":-1 , "s":0}
reverseDict= {1 : "Rock" , -1:"Paper" , 0 : "Scissor"}
you = youDict[youstr]

print(f"You Chose : {reverseDict[you]} \nComputer Chose : {reverseDict[computer]}")

if(computer==you):
    print("it's a Draw")
else:
    if(computer==1 and you ==-1): 
        print("You Win")
    elif(computer==1 and you ==0): 
        print("Better Luck Next Time!")
    elif(computer==-1 and you ==1): 
        print(" Better Luck Next Time!")
    elif(computer==-1 and you ==0): 
        print("You win")
    elif(computer==0 and you ==-1): 
        print("Better Luck Next Time!")
    elif(computer==0 and you ==1): 
        print("you win")
    else:
        print("Something went wrong!")
