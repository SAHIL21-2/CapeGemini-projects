import random
while(True):
    computer_choice = random.randint(1,3) # RANDOM NUMBER BETWEEN 1 TO 3
    print("CHOOSE ONE:-\n1 FOR Rock \n2 FOR Paper \n3 FOR Scissor\n")
    user_choice = int(input("Enter your choice: ")) #USER CHOICE
    print("Computer's choice: ", computer_choice)
    
        # CHECK FOR INVALID NUMBER
    if(user_choice<1 or user_choice>3):
        print("\nINVALID CHOICE❌! Please Choose a number Between 1 TO 3\n")
        continue #IF USER MAKE INVALID CHOICE THEN WE NEED TO RESET THE GAME
    
    # CHECK WETHER COMPUTER AND USER CHOOSE SAME // DRAW CONDITION
    elif(computer_choice==user_choice):
        print("It's a DRAW!")
        continue #IF IT IS DRAW THEN WE ALSO NEED TO RESET THE GAME
    
    
    # CHECK THE WINNING CONDITONS FOR USER 
    elif((user_choice== 1 and computer_choice == 3) or
        (user_choice== 2 and computer_choice == 1) or 
        (user_choice== 3 and computer_choice == 2)):
            
            print("YAY! YOU WON")
            # ASKING FOR ANOTHER GAME TO THE USER 
            more_play = input("Want to play again ? type Y for yes and N for not: ")
            if(more_play=='y' or more_play=='Y'):
                continue
            else:
                break #IF USER WON THEN WE STOPS THE GAME BY STOPING THE LOOP
    
    # IF USER NOT WON AND ALSO IT IS NOT A DRAW THEN ABSOULUTELY COMPUTER WON AND USER LOSE
    else:
        print("OH! You Lose🥺")
         # ASKING FOR ANOTHER GAME TO THE USER 
        more_play = input("Want to play again ? type Y for yes and N for not: ")
        if(more_play=='y' or more_play=='Y'):
                continue
        else:
                break #IF USER LOSE THEN WE STOPS THE GAME BY STOPING THE LOOP

    
    